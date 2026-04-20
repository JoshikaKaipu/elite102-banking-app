import cbFunctions as cbFunc
def mainFunction():
    print("Hello! Welcome to the BankEasy Chatbot!")
    name = input("What is your name? ")

    print(f"Hello {name}, it's so nice to meet you!")

    age = int(input("How old are you? "))

    print(f"{age}! That's pretty cool, isn't it!")
    print("How can I assist you today? ")
    while True:
        print("Options: ")
        print("1. Help Choose an Account")
        print("2. Help Set up an New Account")
        print("3. Frequently Asked Questions")
        print("4. Exit the conversation")

        userChoice = int(input("How would you like to continue? "))
        if userChoice == 1:
            print("Perfect!")
            cbFunc.chooseAccount()
            print(f"More information will be sent to you soon! Thank you for choosing BankEasy {name}! Please reach out if you have any further questions!")
            print("Thank you!")
        elif userChoice == 2:
            cbFunc.accountSetUp()
            print(f"Thank you for choosing BankEasy {name}! Your account will be activated in the next 2 days.")
            print("Please be looking account for an email with further instructions.")
        elif userChoice == 3:
            print("Nice!")
            cbFunc.freqAskQuestions()
            print("Thank you for choosing BankEasy!")
        elif userChoice == 4:
            print(f"Bye {name}! Let me know if you have any other questions later on!")
            break
        else:
            print("Sorry, please enter a valid input next time!")