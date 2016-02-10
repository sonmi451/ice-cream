#bombe is a brute force crack at the enigma encoding
#enigma.louisedade.co.uk/howitworks.html
#www.counton.org/explorer/codebreaking/enigma-cipher.php

#test with
#nothing apparently...

###########################################################
#functions
def bombeIt():
	for r in range(0,len(cog)):
		iterationX=[]
		countup1,countup2,countup3=0,0,0
		startposition1,startposition2,startposition3 = countup1,countup2,countup3
		bombeCycle=0
		for x in range(0,17576):
			#print(bombeCycle)
			startposition1=countup1+bombeCycle
			rotorPositions=[]
			for z in range (0,(len(ciphertext))):
				i = z % 26
				startposition1 = (startposition1+1)%26
				if startposition1%26 == 0:
					startposition2 = (startposition2+1)%26
					if startposition2%26 == 0:
						startposition3 = (startposition3+1)%26
				rotorPositions.append([i,startposition1, startposition2, startposition3])
				#startposition1=(startposition1+1)%26
			#print(rotorPositions)
			bombeCycle+=1
			#scrambling letters
			rotorA,rotorB,rotorC=cog[r][0],cog[r][1],cog[r][2]
			for z in range (0,len(ciphertext)):
				positionX = [x for x in rotorPositions[z]]
				position1, position2, position3 = positionX[1], positionX[2], positionX[3]
				for i in range(0,len(rotorA)):
					if rotorA[(i+position1)%26][0]==ciphertext[z]:
						scramble1 = rotorA[i][2]
				for i in range(0,len(rotorB)):
					if rotorB[(i+position2)%26][0]==scramble1:
						scramble2 = rotorB[i][2]
				for i in range(0,len(rotorC)):
					if rotorC[(i+position3)%26][0]==scramble2:
						scramble3 = rotorC[i][2]
				for i in range(0,len(reflector)):
					if reflector[i][0]==scramble3:
						reflect = reflector[i][1]
				for i in range(0,len(rotorC)):
					if rotorC[(i-position3)%26][2]==reflect:
						scramble4 = rotorC[i][0]
				for i in range(0,len(rotorB)):
					if rotorB[(i-position2)%26][2]==scramble4:
						scramble5 = rotorB[i][0]
				for i in range(0,len(rotorA)):
					if rotorA[(i-position1)%26][2]==scramble5:
						scramble6 = rotorA[i][0]
				#print(rotorA[z][0], rotorA[z][1], rotorA[z][2])
				#if z < cribStart:
				#	iterationX.append(scramble6)
				if z >= cribStart and scramble6 != crib[z]:
					#print("next iteration")
					break
				else:
					iterationX.append(scramble6)
					#print(iterationX)
					#print(''.join(iterationX[cribStart:]))
			#print(iterationX[cribStart:])    
			#print(''.join(iterationX[cribStart:]), crib)
			if (''.join(iterationX[cribStart:])) == testCrib:
				#print(''.join(iterationX))
				print(crib)
				print("stop")
				if rotorA == rotor1:
					rotorX = "Rotor 1"
				elif rotorA == rotor2:
					rotorX = "Rotor 2"
				elif rotorA == rotor3:
					rotorX = "Rotor 3"
				elif rotorA == rotor4:
					rotorX = "Rotor 4"
				if rotorB == rotor1:
					rotorY = "Rotor 1"
				elif rotorB == rotor2:
					rotorY = "Rotor 2"
				elif rotorB == rotor3:
					rotorY = "Rotor 3"
				elif rotorB == rotor4:
					rotorY = "Rotor 4"
				if rotorC == rotor1:
					rotorZ = "Rotor 1"
				elif rotorC == rotor2:
					rotorZ = "Rotor 2"
				elif rotorC == rotor3:
					rotorZ = "Rotor 3"
				elif rotorC == rotor4:
					rotorZ = "Rotor 4"
				print("rotor order is:",rotorX,rotorY,rotorZ)
				print("rotor starting positions are:", rotorPositions[0][1]-1,rotorPositions[0][2],rotorPositions[0][3])
				#return
				#commenting out return shows all stops not just first stop (incs "false stops")
			rotorPositions=[]
			iterationX=[]
###########################################################

ciphertextInput, cribInput, cribStart = input("ciphertext:"), input("crib:"), int(input("crib start position, countup from 0:"))
blanks = []
for x in range(0,cribStart):
	blanks.append('x')
#ciphertextInput = ciphertextInput.lower()
ciphertext= [x for x in ciphertextInput]
makeCrib = [['x' for x in range(0,cribStart)], [x for x in cribInput]]
crib = [x for x in makeCrib for x in x]
crib= ''.join(crib)
testCrib=crib[cribStart:]
#print(ciphertext)
#print(crib)
#print(crib[cribStart:])
#print(''.join(ciphertext))

#making the rotors and reflector
alphaNum=[x for x in range (0,26)]
alphabet=[x for x in ('abcdefghijklmnopqrstuvwxyz')]
alpha1=[x for x in ('ntuabmzjlvwcdefopkqrsghixy')]
alpha2=[x for x in ('deopkqrfsghlvixujwyamnbczt')]
alpha3=[x for x in ('efabklcdghrsijmnvwzxopqtuy')]
alpha4=[x for x in ('goncpqtuybhrsijmdwvefaklzx')]
backwards=[x for x in reversed('abcdefghijklmnopqrstuvwxyz')]
numberedAlphabet= dict(zip(alphabet,alphaNum))

#set up rotor1
rotor1=[]
for x in range(0,26):
	positionx = [alphabet[x],x,alpha1[x]]
	rotor1.append(positionx)
#for i in range(0,(len(rotor1))):
    #print (rotor1[i],)	

#set up rotor2
rotor2=[]
for x in range (0,26):
	positionx = [alphabet[x],x,alpha2[x]]
	#print(positionx)
	rotor2.append(positionx)
#for i in range(0,(len(rotor2))):
    #print (rotor2[i])	

#set up rotor3
rotor3=[]
for x in range (0,26):
	positionx = [alphabet[x],x,alpha3[x]]
	#print(positionx)
	rotor3.append(positionx)
#for i in range(0,(len(rotor3))):
    #print (rotor3[i])	
    
#set up rotor4
rotor4=[]
for x in range (0,26):
	positionx = [alphabet[x],x,alpha4[x]]
	#print(positionx)
	rotor4.append(positionx)	

#set up reflector
reflector=[]
for x in range (0,26):
	positionx = [alphabet[x],backwards[x]]
	#print(positionx)
	reflector.append(positionx)	

#all 64 possible rotor arrangements
rotorArrangements, cog = [], []
rotorA,rotorB,rotorC=0,0,0
while len(rotorArrangements)<64:
	rotorA=(rotorA+1)%4
	if rotorA%4 == 0:
		rotorB=(rotorB+1)%4
		if rotorB%4 == 0:
			rotorC=(rotorC+1)%4
	if [rotorA,rotorB,rotorC] not in rotorArrangements:
	    rotorArrangements.append([rotorA,rotorB,rotorC])
for a in range(0,len(rotorArrangements)):
	if rotorArrangements[a][0] == 0:
		rotorArrangements[a][0] = rotor1
	elif rotorArrangements[a][0] == 1:
		rotorArrangements[a][0] = rotor2
	elif rotorArrangements[a][0] == 2:
		rotorArrangements[a][0] = rotor3
	elif rotorArrangements[a][0] == 3:
		rotorArrangements[a][0] = rotor4
	if rotorArrangements[a][1] == 0:
		rotorArrangements[a][1] = rotor1
	elif rotorArrangements[a][1] == 1:
		rotorArrangements[a][1] = rotor2
	elif rotorArrangements[a][1] == 2:
		rotorArrangements[a][1] = rotor3
	elif rotorArrangements[a][1] == 3:
		rotorArrangements[a][1] = rotor4
	if rotorArrangements[a][2] == 0:
		rotorArrangements[a][2] = rotor1
	elif rotorArrangements[a][2] == 1:
		rotorArrangements[a][2] = rotor2
	elif rotorArrangements[a][2] == 2:
		rotorArrangements[a][2] = rotor3
	elif rotorArrangements[a][2] == 3:
		rotorArrangements[a][2] = rotor4
	cog.append([rotorArrangements[a][0],rotorArrangements[a][1],rotorArrangements[a][2]])

bombeIt()
