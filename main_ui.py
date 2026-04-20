import generatePassword as gp
import banking_app as ba
import questions as q

move = True
while move == True:
    print("Hello! Welcome to the Bank!")
    print()
    print("Choose one of the options below!")
    print()
    print("1. Create an Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Questions")
    print("6. Exit")

    userChoice = int(input("Enter your choice: "))

    if userChoice == 1:
        print("Awesome! Let's get a few details before we get started!")
        print()
        print("Step 1: Name")
        accountName = input("What is your name? ")
        print()
        print("Step 2: Password")
        print()
        print("Options:")
        print()
        print("1. Input Password")
        print("2. Generate Password")
        print()
        pwOption = int(input("Enter your choice: "))
        if pwOption == 1:
            password = input("What is your password? ")
        elif pwOption == 2:
            password = gp.wholeFunction()
            print(f"Your password is {password}")

        ba.createAccount(accountName, password)

    elif userChoice == 2:
        username = input("What is your name? ")
        password = input("What is your password? ")
        accountFound = ba.login(username, password)
        if accountFound == True:
            print("Login Successful!")
            ba.checkBalance(username)
        else:
            print("Login Failed. Please try again.")

    elif userChoice == 3:
        username = input("What is your name? ")
        password = input("What is your password? ")
        accountFound = ba.login(username, password)
        if accountFound == True:
            print("Login Successful!")
            amount = round(float(input("How much would you like to deposit? ")),2)
            ba.deposit(username, amount)
        else:
            print("Login Failed. Please try again.")

    elif userChoice == 4:
        username = input("What is your name? ")
        password = input("What is your password? ")
        accountFound = ba.login(username, password)
        if accountFound == True:
            print("Login Successful!")
            amount = round(float(input("How much would you like to withdraw? ")),2)
            ba.withdraw(username, amount)
        else:
            print("Login Failed. Please try again.")

    elif userChoice == 5:
        q.mainFunction()

    elif userChoice == 6:
        break

    else:
        print("Sorry, please enter a valid number!")


        #print("Sorry, please try again!")


