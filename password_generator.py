version = 1

def Main():
    startup()
    site = getSite()
    print("")
    password = getPass()
    print("")
    generated_password = createPass(site, password)
    outputPass(generated_password)
    print("")
    endProgram()

def startup():
    print("Hello, welcome to the password generator thingy..!")
    print("")
    print("Current version: " + str(version))
    print("")
    print("")

def getSite():
    return str(input("Please enter the name of the website you would like to find the password for: "))

def getPass():
    return str(input("Please type in your main password: "))

def createPass(site, password):
    length = (len(site)+len(password))//2
    main_array = createArray(site, password)
    hash_array = changeArray(main_array)
    return str(createHash(hash_array, length))

def createArray(site, password):
    completeArray= []
    count1 = 0
    count2 = 1
    for i in (site + password):
        completeArray.append(i)
    for letter in site:
        if count1 < len(completeArray):
            completeArray[count1] = letter
            count1 = count1 + 2
    for letter in password:
        if count2 < len(completeArray):
            completeArray[count2] = letter
            count2 = count2 + 2
    return completeArray

def changeArray(array):
    array = lowerArray(array)
    array = shuffleArray(array)
    array = capitaliseArray(array)
    return array

def createHash(array, length):
    array = bitArray(array)
    array = invertArray(array)
    array = flipArray(array)
    array = stringArray(array)
    array = cutArray(array, length)
    array = addLetterArray(array)
    array = addNumberArray(array)
    return "".join(array)

def bitArray(array):
    count = 0
    for letter in array:
        number = ord(letter)
        array[count] = str(bin(number)[2:].zfill(16))
        count = count + 1
    return array

def invertArray(array):
    count = 0
    for byte in array:
        array[count] = invertByte(byte)
        count = count + 1
    return array

def invertByte(byte):
    count = 0
    byte = list(byte)
    for bit in byte:
        if bit == '1':
            byte[count] = '0'
        else:
            byte[count] = '1'
        count = count + 1
    byte = "".join(byte)
    return byte

def flipArray(array):
    count = 0
    for number in array:
        array[count] = flipByte(number)
        count = count + 1
    return array

def stringArray(array):
    count = 0
    for byte in array:
        byte = int(byte, 2)
        byte = byte // 2
        byte = chr(byte)
        array[count] = byte
        count = count + 1
    return array

def cutArray(array, length):
    if length > 16:
        length = 16
    return array[0:length-1]

def addLetterArray(array):
    number = int(len(array)/16)*20 + 97
    array.append(chr(number))
    array.append(chr(number+2))
    array.append(chr(number+2))
    array.append(chr(number+4))
    return array

def addNumberArray(array):
    number = len(array)
    array.append(str(number))
    array.append(str(number//2))
    array.append(str(number*2))
    return array

def flipByte(byte):
    count = 0
    byte = list(byte)
    for bit in byte:
        if isPrime(count):
            if bit == '1':
                byte[count] = '0'
            else:
                byte[count] = '1'
        count = count + 1
    byte = "".join(byte)
    return byte
        
    
def isPrime(n):
    i = 2
    if n < 2:
        return False
    while i < n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True
    
def lowerArray(array):
    count = 0
    for letter in array:
        array[count] = letter.lower()
        count = count + 1
    return array

def shuffleArray(array):
    length = len(array) - 1
    count = 2
    count2 = 1
    count3 = 0
    newArray = []
    while count <= length:
        newArray.append(array[count])
        count = count + 3
    while count2 <= length:
        newArray.append(array[count2])
        count2 = count2 + 2
    while count3 <= length:
        newArray.append(array[count3])
        count3 = count3 + 3
    return newArray

def capitaliseArray(array):
    count = 0
    while count < len(array):
        array[count] = array[count].upper()
        count = count + 3
    return array
    
def outputPass(password):
    print("Password is: " + password)

def endProgram():
    input("Press enter to close program!")

if __name__ == '__main__':
    Main()

    
    
