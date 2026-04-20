import random as random
def chooseAccount():
    print("Alright, I see.")
    print("We have three main account types:")
    print()

    print("1. Savings")
    print("2. Checking")
    print("3. Investing")
    print()

    #print("Let me ask you a few questions so that I can assist you better!")
    print("Let me know if you wanted to know more about a specific account type!")
    print()

    knowMore = input("Would you like to know more about a specific account type? (yes/no) ").lower()
    print()

    while True:
        if "yes" in knowMore:
            print("1. Savings")
            print("2. Checking")
            print("3. Investing")
            print()
            aChoice = input("Which account type would you like to know more about? ").lower()
            if "savings" in aChoice or "saving" in aChoice or "1" in aChoice:
                print("BankEasy offers customers with two options to choose from. The BankEasy Optimal Savings Account is")
                print("the perfect place to safely keep the money you don't need for daily spending. Whether you're")
                print("building an emergency fund, saving for a vacation, or planning a big purchase, this account")
                print("helps your money grow while keeping it secure and accessible. If you're looking for something smaller,")
                print("the BankEasy Standard Savings Account is perfect for your needs.")
                print()

                while True:
                    move = input("Would you like to learn about the other options? ").lower()
                    if "yes" in move:
                        print("Sounds good, I will return you to the option menu!")
                        print()
                        break

                    elif "no" in move:
                        print("Sounds good, let me return you to the main menu!")
                        print()
                        break

                    else:
                        print("Sorry, please enter a valid input next time.")
                        print()
                        
                if "no" in move:
                    break
                continue

            elif "checking" in aChoice or "2" in aChoice:
                print("BankEasy offers customers with two options to choose from. The BankEasy Standard Checking Account is ")
                print("your go-to account for all things money management. This is the one you use every single day—for coffee, bills,")
                print("online shopping, and getting cash. It's built for convenience and flexibility. If you're looking for a more")
                print("versatile account, BankEasy's Optimal Checking Account is perfect.")
                print()
                while True:
                    move = input("Would you like to learn about the other options? ").lower()
                    print()
                    if "yes" in move:
                        print("Sounds good, I will return you to the option menu!")
                        print()
                        break
                    elif "no" in move:
                        print("Sounds good, let me return you to the main menu!")
                        print()
                        break
                    else:
                        print("Sorry, please enter a valid input next time.")
                        print()
                if "no" in move:
                    break
                continue
            elif "investing" in aChoice or "3" in aChoice:
                print("BankEasy offers two options of Investment Accounts. The first one is the Optimal Investment Account.")
                print("This is where you put your money to work for the long term, helping you build real wealth for")
                print("big goals like retirement or a down payment on a house. We make investing easy,")
                print("even if you're a beginner! If you're looking for a smaller-scaled account, BankEasy's Standard")
                print("Investment Account is perfect for your needs.")
                while True:
                    move = input("Would you like to learn about the other options? ").lower()
                    if "yes" in move:
                        print("Sounds good, I will return you to the option menu!")
                        print()
                        break
                    elif "no" in move:
                        print("Sounds good, let me return you to the main menu!")
                        print()
                        break
                    else:
                        print("Sorry, please enter a valid input next time.")
                        print()
                if "no" in move:
                    break
                continue
            else:
                print("Sorry, please enter a valid input next time.")
        elif "no" in knowMore:
            print("No worries! I will direct you back to the main menu!")
            break
        else:
            print("Sorry, please enter a valid input next time.")
            knowMore = input("Would you like to know more about a specific account type? (yes/no) ").lower()
            if knowMore == "yes":
                continue
            elif knowMore == "no":
                break
            else:
                continue

def findingAccount():
    
    while True:
        finalMove = False
        savingType = input("What is your primary focus? (Saving, checking, or investing) ").lower()

        if "saving" in savingType or "1" in savingType:
            print("Perfect!")
            print("1. Optimal Savings Account")
            print("2. Standard Savings Account")
            type = input("Which account would you like to move forward with? ")
            while True:
                move = input("That is a great account! Would you like me to confirm this one? ").lower()
                if "yes" in move:
                    print("Sounds good! I will set up your account!")
                    finalMove = False
                    return "savings"
                    break
                elif "no" in move:
                    print("Okay, I will direct you back to our main choices.")
                    finalMove = True
                    break
                else:
                    print("Sorry, I didn't get that.")
        elif "checking" in savingType or "2" in savingType:
            print("Perfect!")
            print("1. Optimal Checking Account")
            print("2. Standard Checking Account")
            type = input("Which account would you like to move forward with? ")
            while True:
                move = input("That is a great account! Would you like me to confirm this one? ").lower()
                if "yes" in move:
                    print("Sounds good! I will set up your account!")
                    finalMove = False
                    return "checking"
                    break
                elif "no" in move:
                    print("Okay, I will direct you back to our main choices.")
                    finalMove = True
                    break
                else:
                    print("Sorry, I didn't get that.")
        elif "investing" in savingType or "3" in savingType:
            print("Perfect!")
            print("1. Optimal Investment Account")
            print("2. Standard Investment Account")
            type = input("Which account would you like to move forward with? ")
            while True:
                move = input("That is a great account! Would you like me to confirm this one? ").lower()
                if "yes" in move:
                    print("Sounds good! I will help you set up your account!")
                    finalMove = False
                    return "investing"
                    break
                elif "no" in move:
                    print("Okay, I will direct you back to our main choices.")
                    finalMove = True
                    break
                else:
                    print("Sorry, I didn't get that.")
        else:
            print("Sorry, please try again by entering one of our choices")
        if finalMove:
            continue
        else:
            break
    
    #savingReason = input("What are you saving for? ()")

def accountSetUp():
    print("Sounds good!")
    while True:
        accountName = (findingAccount()).lower()
        if "savings" in accountName or "1" in accountName:
            faultCount = 0
            while True:
                firstName = input("What is your first name? ")
                lastName = input("What is your last name? ")
                dob = input("What is your date of birth? ")
                ssn = input("Please state the last 4 numbers of your ssn: ")
                print(f"First Name: {firstName}")
                print(f"Last Name: {lastName}")
                print(f"Date of Birth: {dob}")
                move = input("Is the above information correct? ").lower()
                if "yes" in move:
                    print("Perfect!")
                    print("I will now proceed to ask you set of security questions to validate your account set up.")
                    wrongCount=0
                    while True:
                        print("You will need to answer all three correctly")
                        secure1 = input("What is your date of birth? ")
                        secure2 = input("What number comes after 2894 ? ")
                        secure3 = input("What state is this unabbreviated (TX) ? ").lower()
                        if "0" in secure1 or "1" in secure1 or "5" in secure1:
                            infoRight = True
                        else:
                            infoRight = False
                        if "2895" in secure2:
                            infoRight = True
                        else:
                            infoRight = False
                        if "texas" in secure3:
                            infoRight = True
                        else:
                            infoRight = False

                        if infoRight:
                            print("Perfect! Let me start the process for your savings account!")
                            saveAcc()
                            break
                        else:
                            wrongCount = wrongCount+1
                            if wrongCount>=3:
                                print("Sorry, you have attempted the questions too many times. You have been locked out. Please try again later.")
                                break
                            else:
                                print("Sorry, you have answered one or more questions wrong. Please try again.")
                    break
                elif "no" in move:
                    print("Hmmm, let me see.")
                    while True:
                        print("Please answer with 'name' or 'account'")
                        unmatch = input("Which part didn't match, the account name or number? ").lower()
                        if "name" in unmatch:
                            print("I see, let me ask direct you back")
                            break
                        elif "account" in unmatch:
                            print("Oh, let me redirect you back.")
                            break
                        else:
                            print("Sorry, let me try to help you with that.")
                            faultCount = faultCount +1
                            break
                    if faultCount <=2:
                        print("Can you please try again? ")
                        continue
                    else:
                        print("Sorry, we do not have an account on that name or number, please try again later.")
                        break
                else:
                    print("Sorry, please try again with valid input next time.")
                    continue
        elif "checking" in accountName or "2" in accountName:
            faultCount = 0
            while True:
                firstName = input("What is your first name? ")
                lastName = input("What is your last name? ")
                dob = input("What is your date of birth? ")
                ssn = input("Please state the last 4 numbers of your ssn: ")
                print(f"First Name: {firstName}")
                print(f"Last Name: {lastName}")
                print(f"Date of Birth: {dob}")
                move = input("Is the above information correct? ").lower()
                if "yes" in move:
                    print("Perfect!")
                    print("I will now proceed to ask you set of security questions to validate your account set up.")
                    wrongCount=0
                    while True:
                        print("You will need to answer all three correctly")
                        secure1 = input("What is your date of birth? ")
                        secure2 = input("What number comes after 2894 ? ")
                        secure3 = input("What state is this unabbreviated (TX) ? ").lower()
                        if "0" in secure1 or "1" in secure1 or "5" in secure1:
                            infoRight = True
                        else:
                            infoRight = False
                        if "2895" in secure2:
                            infoRight = True
                        else:
                            infoRight = False
                        if "texas" in secure3:
                            infoRight = True
                        else:
                            infoRight = False

                        if infoRight:
                            print("Perfect! Let me start the process for your checking account!")
                            checkAcc()
                            break
                        else:
                            wrongCount = wrongCount+1
                            if wrongCount>=3:
                                print("Sorry, you have attempted the questions too many times. You have been locked out. Please try again later.")
                                break
                            else:
                                print("Sorry, you have answered one or more questions wrong. Please try again.")
                    break
                elif "no" in move:
                    print("Hmmm, let me see.")
                    while True:
                        print("Please answer with 'name' or 'account'")
                        unmatch = input("Which part didn't match, the account name or number? ").lower()
                        if "name" in unmatch:
                            print("I see, let me ask direct you back")
                            break
                        elif "account" in unmatch:
                            print("Oh, let me redirect you back.")
                            break
                        else:
                            print("Sorry, let me try to help you with that.")
                            faultCount = faultCount +1
                            break
                    if faultCount <=2:
                        print("Can you please try again? ")
                        continue
                    else:
                        print("Sorry, we do not have an account on that name or number, please try again later.")
                        break
                else:
                    print("Sorry, please try again with valid input next time.")
                    continue
        elif "investing" in accountName or "3" in accountName:
            faultCount = 0
            while True:
                firstName = input("What is your first name? ")
                lastName = input("What is your last name? ")
                dob = input("What is your date of birth? ")
                ssn = input("Please state the last 4 numbers of your ssn: ")
                print(f"First Name: {firstName}")
                print(f"Last Name: {lastName}")
                print(f"Date of Birth: {dob}")
                move = input("Is the above information correct? ").lower()
                if "yes" in move:
                    print("Perfect!")
                    print("I will now proceed to ask you set of security questions to validate your account set up.")
                    wrongCount=0
                    while True:
                        print("You will need to answer all three correctly")
                        secure1 = input("What is your date of birth? ")
                        secure2 = input("What number comes after 2894 ? ")
                        secure3 = input("What state is this unabbreviated (TX) ? ").lower()
                        if "0" in secure1 or "1" in secure1 or "5" in secure1:
                            infoRight = True
                        else:
                            infoRight = False
                        if "2895" in secure2:
                            infoRight = True
                        else:
                            infoRight = False
                        if "texas" in secure3:
                            infoRight = True
                        else:
                            infoRight = False

                        if infoRight:
                            print("Perfect! Let me start the process for your investing account!")
                            investAcc()
                            break
                        else:
                            wrongCount = wrongCount+1
                            if wrongCount>=3:
                                print("Sorry, you have attempted the questions too many times. You have been locked out. Please try again later.")
                                break
                            else:
                                print("Sorry, you have answered one or more questions wrong. Please try again.")
                    break
                elif "no" in move:
                    print("Hmmm, let me see.")
                    while True:
                        print("Please answer with 'name' or 'account'")
                        unmatch = input("Which part didn't match, the account name or number? ").lower()
                        if "name" in unmatch:
                            print("I see, let me ask direct you back")
                            break
                        elif "account" in unmatch:
                            print("Oh, let me redirect you back.")
                            break
                        else:
                            print("Sorry, let me try to help you with that.")
                            faultCount = faultCount +1
                            break
                    if faultCount <=2:
                        print("Can you please try again? ")
                        continue
                    else:
                        print("Sorry, we do not have an account on that name or number, please try again later.")
                        break
                else:
                    print("Sorry, please try again with valid input next time.")
                    continue
        else:
            print("Sorry, please enter a valid input next time.")
            continue

        accNumb = random.randint(10000,99999)
        print(f"Your account number is {accNumb}")
        print("You will be receiving an email soon with more details about your account.")
        break

def saveAcc():
    print("Okay, for a savings account, I will need you to answer some questions.")
    print("1. School")
    print("2. Family")
    print("3. Emergency Fund")
    print("4. Putting Aside Money for Spending")
    print("5. Earning Interest")
    print("6. Overdraft protection")
    option = input("What is the primary purpose of this account? ")
    print(f"Alright, BankEasy has an account for option {option}.")
    print("It is called, Optimal Savings Account")
    while True:
        move = input("Would you like to move forward with the Optimal Savings Account? ").lower()
        if "yes" in move:
            print("Sounds good! I will add everything to your account.")
            break
        elif "no" in move:
            move = input("We also offer a smaller scaled account for smaller savings called Standard Savings Account. Would you like to continue with this? ").lower()
            while True:
                if "yes" in move:
                    print("Sounds good! I will add everything to your new Standard Savings Account.")
                elif "no" in move:
                    print("Sorry, those are the only options we offer.")
                    while True:
                        move = input("Would you like to continue with this (1) or the other one (2)? ").lower()
                        if "1" in move:
                            print("Perfect! I will add everything to your new Standard Savings Account!")
                            break
                        elif "2" in move:
                            print("Sounds good! I will add everything to your new Optimal Savings Account!")
                            break
                        else:
                            print("Sorry, I didn't get that. Please try again.")
                    break
                else:
                    print("Sorry, I didn't quite get that. Please try again.")

        else:
            print("Sorry, please try again.")
            continue
        break

def checkAcc():
    print("Okay, for a checking account, I will need you to answer some questions.")
    print("1. Daily Spending")
    print("2. Paying Bills")
    print("3. Accessing Cash")
    print("4. Receiving Income")
    print("5. Transfers")
    print("6. Budgeting and Tracking")
    option = input("What is the primary purpose of this account? ")
    print(f"Alright, BankEasy has an account for options including {option}.")
    print("It is called, Optimal Checking Account")
    while True:
        move = input("Would you like to move forward with the Optimal Checking Account? ").lower()
        if "yes" in move:
            print("Sounds good! I will add everything to your account.")
            break
        elif "no" in move:
            move = input("We also offer a smaller scaled account for smaller transaction called Standard Checking Account. Would you like to continue with this? ").lower()
            while True:
                if "yes" in move:
                    print("Sounds good! I will add everything to your new Standard Checking Account.")
                elif "no" in move:
                    print("Sorry, those are the only options we offer.")
                    while True:
                        move = input("Would you like to continue with this (1) or the other one (2)? ").lower()
                        if "1" in move:
                            print("Perfect! I will add everything to your new Standard Checking Account!")
                            break
                        elif "2" in move:
                            print("Sounds good! I will add everything to your new Optimal Checking Account!")
                            break
                        else:
                            print("Sorry, I didn't get that. Please try again.")
                    break
                else:
                    print("Sorry, I didn't quite get that. Please try again.")

        else:
            print("Sorry, please try again.")
            continue
        break

def investAcc():
    print("Okay, for a investing account, I will need you to answer some questions.")
    print("1. Retirement")
    print("2. Education")
    print("3. General Wealth Building")
    print("4. Major Purchases")
    option = input("What is the primary purpose of this account? ")
    print(f"Alright, BankEasy has an account for options including {option}.")
    print("It is called, Optimal Investment Account")
    while True:
        move = input("Would you like to move forward with the Optimal Investment Account? ").lower()
        if "yes" in move:
            print("Sounds good! I will add everything to your account.")
            break
        elif "no" in move:
            move = input("We also offer a smaller scaled account for smaller transaction called Standard Investment Account. Would you like to continue with this? ").lower()
            while True:
                if "yes" in move:
                    print("Sounds good! I will add everything to your new Standard Investment Account.")
                elif "no" in move:
                    print("Sorry, those are the only options we offer.")
                    while True:
                        move = input("Would you like to continue with this (1) or the other one (2)? ").lower()
                        if "1" in move:
                            print("Perfect! I will add everything to your new Standard Investment Account!")
                            break
                        elif "2" in move:
                            print("Sounds good! I will add everything to your new Optimal Investment Account!")
                            break
                        else:
                            print("Sorry, I didn't get that. Please try again.")
                    break
                else:
                    print("Sorry, I didn't quite get that. Please try again.")

        else:
            print("Sorry, please try again.")
            continue
        break

def freqAskQuestions():
    print("No Problem!")
    print("Please let me know what you need help with!")
    while True:
        print("1. How do I view my account balance?")
        print("2. What is the minimum balance do I need to maintain?")
        print("3. Is Mobile Banking Available?")
        print("4. What are the trasaction charges?")
        print("5. Is there a branch nearby?")
        print("6. What interest rates does the bank offer?")
        print("7. Other")
        ques = input("Which of the above questions do you have (please enter the option key)? ").lower()
        if "1" in ques:
            print("You can view your account balance by requesting an employee at your nearest branch, checking the online bank website, or mobile banking app.")
        elif "2" in ques:
            print("You need to maintain $1,500 or have regular direct deposits to avoid BankEasy's maintenance fee.")
        elif "3" in ques:
            print("Yes, BankEasy offers a mobile app called BankEasy.")
        elif "4" in ques:
            print("BankEasy does not charge for normal deposits which includes manual and online ones. Whereas, other transactions like cashier's checks and money orders have a $20 fee.")
        elif "5" in ques:
            place = input("What city do you live in? ")
            print(f"Yes, there is one on Main Street, {place}")
        elif "6" in ques:
            print("Our optimal accounts offer a 4.9% interest rate. Our standard accounts offer a 3.1% interest rate.")
        elif "7" in ques:
            otherQues = input("No worries, what is your question? ")
            print(f"I will direct your question of {otherQues} to a customer support representative who is online. Please wait.")
        else:
            print("Sorry, I didn't quite get that. Please enter a valid option.")
            continue
        move = input("Do you have any more questions (yes/no)? ").lower()
        if "no" in move:
            break