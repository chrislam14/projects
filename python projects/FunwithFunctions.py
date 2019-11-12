#Author: Christopher Lam 29545944

import math


#Function 1

def cylinderVolume(radius:float, height:float)-> float:
    '''returns the volume of a cylinder given the radius and height
    '''
    volume = radius**(2)*math.pi*height #formula for the volume of a cylinder
    return volume

assert (cylinderVolume(1, 10) == 31.41592653589793)
assert (cylinderVolume(4, 2) == 100.53096491487338)
assert (cylinderVolume(2.4, 9) == 162.8601631620949)

#Function 2

def formatNumber(number:float)-> str:
    '''takes a number as an input and return a string that formats
    the number with commas separating the thousands. Decimals are ignored.
    '''
    formatresult = '{:,}'.format(number) #formats the number with commas appropriately
    formatStr = str(formatresult)
    return formatStr
    
assert (formatNumber(1024) == '1,024')
assert (formatNumber(0.3) == '0.3')
assert (formatNumber(123456789.1234) == '123,456,789.1234')
assert (formatNumber(999) == '999')

#Function 3

def securePassword(password:str)-> bool:
    '''take a string and return True if the password is secure
    and False if the password is not secure.
    A secure password has the following features:
    At least 8 characters
    Contains one upper case letter
    Contains one lower case letter
    Contains one number
    Contains one symbol
    '''
    checker = [0,0,0,0,0] #checker 
    symbols = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=",
               "`","~","[","{","]","}","|","\\",":",";","\"","'",",",
               "<",".",">","?","/"]
    security = False
    for l in password:
        if l.isupper(): #checks for an uppercase
            checker[0] = 1
        elif l.islower(): #checks for a lowercase
            checker[1] = 1
        elif l.isnumeric(): #checks for number
            checker[2] = 1
        for s in symbols: #checks for symbols
            if l == s:
                checker[3] = 1
    if len(password) >= 8: #checks if password is 8 or longer
        checker[4] = 1
    if checker == [1,1,1,1,1]:
        security = True
    return security

assert(securePassword('helloworld') == False)
assert(securePassword('Hel!0123') == True)
assert(securePassword('Aa1!') == False)
assert(securePassword('Aa1!!!!!!') == True)

#Function 4

def middleValue(a:float, b:float, c:float)-> float:
    '''returns the 2nd value of a, b, and c in their sorted order.
    '''
    numberlist = [a,b,c]
    sortednumberlist = sorted(numberlist) #sorts the value from lowest to highest
    return sortednumberlist[1] #chooses the middle value of the list

assert(middleValue(1, 2, 3) == 2)
assert(middleValue(4, 8, 3) == 4)
assert(middleValue(-4, 0, -2) == -2)
assert(middleValue( 3.2, 7, 4.8) == 4.8)

#Function 5

def isBinary(number:int)-> bool:
    '''returns true if number consists of only 1's and 0's
    '''
    result = True
    binarystring = str(number)
    for i in binarystring:
        if i != '1' and i != '0': #checks if the digit in the number is not 1 or 0
            result = False
    return result

assert (isBinary(101010) == True)
assert (isBinary(100002) == False)
assert (isBinary(1) == True)
assert (isBinary(12345) == False)

#Function 6

def scramble(word:str)-> str:
    '''replaces each individual capitalized letter with the letter to
    the right on the keyboard and return the result
    '''
    ALPHABET = "abcdefghijklmnopqrstuvwxyz " #alphabet table
    ALPHASCRAMBLED = "snvfrghjoklazmpqwtdyibecux " #shifted alphabet according to key positions on the keyboard
    table = str.maketrans (ALPHABET.upper(), ALPHASCRAMBLED.upper())
    scrambledResult = word.translate(table)
    return scrambledResult

assert (scramble('PYTHON') == 'QUYJPM')
assert (scramble('HELLO WORLD') == 'JRAAP EPTAF')
assert (scramble('ICS RULES') == 'OVD TIARD')

#Function 7

def removeChars(phrase:str, remove:str)-> str:
    '''remove all instances of every character
    of remove from phrase and return the result.
    '''
    resultStr = phrase
    for c in remove:
        resultStr = resultStr.replace(c, "") #replaces the unwanted characters with blank spaces 
    return resultStr

assert(removeChars('abcde', 'b') == 'acde')
assert(removeChars('hello there', 'er') == 'hllo th')
assert(removeChars('Computer Science', 're p') == 'ComutScinc')
assert(removeChars('1 Fish, 2 Fish', '1,') == ' Fish 2 Fish')

#Function 8

def isPalindrome(phrase:str)-> bool:
    '''returns True if phrase is a palindrome,
    a string that is the same forwards and backwards,
    and False otherwise.
    '''
    result = True
    phrase = phrase.replace(" ", "") #removes whitespaces so they do not get in the way
    phrase = phrase.lower()  #makes the string all lowercase so capitalization does not get in the way
    for i in range(len(phrase)):
        if phrase[i] != phrase[-i - 1]: #examines if the characters are the same
            result = False     
    return result

assert(isPalindrome('Race car') == True)
assert(isPalindrome('hey hey') == False)
assert(isPalindrome('tacoCat') == True)

