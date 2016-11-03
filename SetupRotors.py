# setup rotors

def setupRotors():
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


    #set up rotor2
    rotor2=[]
    for x in range (0,26):
        positionx = [alphabet[x],x,alpha2[x]]
        rotor2.append(positionx)	

    #set up rotor3
    rotor3=[]
    for x in range (0,26):
        positionx = [alphabet[x],x,alpha3[x]]
        rotor3.append(positionx)
        
    #set up rotor4
    rotor4=[]
    for x in range (0,26):
        positionx = [alphabet[x],x,alpha4[x]]
        rotor4.append(positionx)

    #set up reflector
    reflector=[]
    for x in range (0,26):
        positionx = [alphabet[x],backwards[x]]
        reflector.append(positionx)
    
    #return rotors
    return rotor1, rotor2, rotor3, rotor4, reflector, numberedAlphabet
    
def chooseRotors(rotor1,rotor2,rotor3,rotor4):
    #starting rotors
    rotorName = [rotor1,rotor2,rotor3,rotor4]
    rotorIdentifier = [1,2,3,4]
    rotorChoice= dict(zip(rotorIdentifier,rotorName))
    print("select todays rotors (from 1,2,3,4)")
    rotorA = rotorChoice[int(input("rotor A:"))]
    rotorB = rotorChoice[int(input("rotor B:"))]
    rotorC = rotorChoice[int(input("rotor C:"))]

    #starting rotor positions
    print("select today's starting letters")
    start_position1=numberedAlphabet[input("Position 1:")]
    start_position2=numberedAlphabet[input("Position 2:")]
    start_position3=numberedAlphabet[input("Position 3:")]
    return rotorA, rotorB, rotorC, start_position1, start_position2, start_position3
    
def plaintextInput():
    #setup plaintext
    message = input("plaintext message to encode: ")
    message = message.lower()
    plaintext = [i for i in message if i not in [' ','.',',','!','?']]
    print("plaintext is:", ''.join(plaintext))
    return plaintext
    
def enigmafy(rotorA, rotorB, rotorC, start_position1, start_position2, start_position3, plaintext):
    ciphertext=[]
    #steps through the rotor positions depending on length of plaintext
    #using mod to wrap
    rotorPositions=[]
    for letter in range (0,len(plaintext)):
            i = letter % 26
            start_position1 = (start_position1+1)%26
            if start_position1%26 == 0:
                start_position2 = (start_position2+1)%26
                if start_position2%26 == 0:
                    start_position3 = (start_position3+1)%26
            rotorPositions.append([i,start_position1, start_position2, start_position3])
    #scrambling letters
    for letter in range (0,len(plaintext)):
        positionX = [x for x in rotorPositions[letter]]
        position1, position2, position3 = positionX[1], positionX[2], positionX[3]
        #scramble step 1
        for i in range(0,len(rotorA)):
            if rotorA[(i+position1)%26][0]==plaintext[letter]:
                scramble1 = rotorA[i][2]
        #print(1, plaintext[letter], "becomes", scramble1)
        #scramble step 2
        for i in range(0,len(rotorB)):
            if rotorB[(i+position2)%26][0]==scramble1:
                #print(rotorA[i])
                scramble2 = rotorB[i][2]
        #print(2, scramble1, "becomes", scramble2)
        #scramble step 3
        for i in range(0,len(rotorC)):
            if rotorC[(i+position3)%26][0]==scramble2:
                #print(rotorA[i])
                scramble3 = rotorC[i][2]
        #print(3, scramble2, "becomes", scramble3)
        #scramble step 4
        for i in range(0,len(reflector)):
            if reflector[i][0]==scramble3:
                #print(rotorA[i])
                reflect = reflector[i][1]
        #print(4,scramble3, "reflected to", reflect)
        #scramble step 5
        for i in range(0,len(rotorC)):
            if rotorC[(i-position3)%26][2]==reflect:
                #print(rotorA[i])
                scramble4 = rotorC[i][0]
        #print(5, reflect, "becomes", scramble4)
        #scramble step 6
        for i in range(0,len(rotorB)):
            if rotorB[(i-position2)%26][2]==scramble4:
                #print(rotorA[i])
                scramble5 = rotorB[i][0]
        #print(6, scramble4, "becomes", scramble5)
        #scramble step7
        for i in range(0,len(rotorA)):
            if rotorA[(i-position1)%26][2]==scramble5:
                #print(rotorA[i])
                scramble6 = rotorA[i][0]
        #print(7, scramble5, "becomes", scramble6)
        
        
        ciphertext.append(scramble6)
    #print(ciphertext)
    print("ciphertext is:", ''.join(ciphertext))
    return ciphertext

def encodeMessage(rotorA, rotorB, rotorC, start_position1, start_position2, start_position3):
    encodeMsg = input('message to encode? y/n')
    if encodeMsg is 'y':
        plaintext = plaintextInput()
        ciphertext = enigmafy(rotorA, rotorB, rotorC, start_position1, start_position2, start_position3, plaintext)
        encodeMessage(rotorA, rotorB, rotorC, start_position1, start_position2, start_position3)
    elif encodeMsg is 'n':
        return False
    else:
        encodeMessage(rotorA, rotorB, rotorC, start_position1, start_position2, start_position3)


        
input('Setup the Rotors')    
rotor1, rotor2, rotor3, rotor4, reflector, numberedAlphabet = setupRotors()
rotorA, rotorB, rotorC, start_position1, start_position2, start_position3 = chooseRotors(rotor1,rotor2,rotor3,rotor4)
encodeMessage(rotorA, rotorB, rotorC, start_position1, start_position2, start_position3)
#encodeTry = encodeMessage()