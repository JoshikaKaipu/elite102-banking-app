import random  #the random and string modules are imported
import string

def wholeFunction():
    def makePW(passLength):  #define a function makePW that takes the password length as a parameter
        upper = input("Would you like uppercase characters?(y/n) ").lower()  #prompt the user for what they would like
        lower = input("Would you like lowercase characters?(y/n) ").lower()
        digits = input("Would you like digits?(y/n) ").lower()
        symbols = input("Would you like symbols?(y/n) ").lower()
        chars = []   #creates a list for the characters
        sybmbolChars = ["!", "@", "#", "$", "&"]  #a list for the symbols is created
        lengthCount = 1  #the count of the password is initialized as 1 
        while True:   #a while loop continues until the length meets the password length wanted
            if lengthCount>passLength:   #the loop breaks if length is greater than the password length
                    break
            if lower == "y":   #if lowercase letters were wanted, a random letter is generated and added to the final password
                letterOne = random.choice(string.ascii_lowercase)
                chars.append(letterOne)
                lengthCount+=1
                if lengthCount>passLength:   #the loop breaks if the length is greater than the passoword length
                    break

            if upper == "y":   #if uppercase letters were wanted, a random letter is generated and added to the final password
                letterTwo = random.choice(string.ascii_uppercase)
                chars.append(letterTwo)
                lengthCount+=1
                if lengthCount>passLength:   #the loop breaks if the length is greater than the passoword length
                    break

            if digits == "y":  #if numbers were wanted, a random number is generated and added to the final password
                digit = str(random.randint(0,9))
                chars.append(digit)
                lengthCount+=1
                if lengthCount>passLength:   #the loop breaks if the length is greater than the passoword length
                    break

            if symbols == "y": #if symbol were wanted, a random symbol is generated and added to the final password
                symbol = random.choice(sybmbolChars) 
                chars.append(symbol)
                lengthCount+=1
                if lengthCount>passLength:   #the loop breaks if the length is greater than the passoword length
                    break
        
        random.shuffle(chars)   #shuffle in the random module is used to shuffle the characters in the final password
        finalPW = ""
        for char in chars:      #the final characters are iterated through and stored in finalPW
            finalPW=finalPW+char
        
        return finalPW
    
    move = True
    while move == True:
        try:   #try and except are used to handle invalid inputs
            passLength = int(input("How long do you want your password to be? "))  #the user is prompted for the password length
            final = makePW(passLength)
            move=False
        except:
            print("Sorry, please try again with a numerical input!")
    
    return final

