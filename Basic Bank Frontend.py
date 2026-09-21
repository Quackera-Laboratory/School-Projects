check_account = 567.12
sav_account = 1469.32
#Transfer

def print_page1():
    print("Hello! What would you like to do today? \nChecking? \n   Saving? \n     Withdraw? \n       deposit?")

#intro to program

choice = (input('"Hello What would you like to do today? \nChecking? \n   Saving? \n     Withdraw? \n       deposit? \n \t'))
if choice == 'Checking' or choice == "checking" or choice == 'checkings' or choice == 'Checkings':
    print(f' \n your balance is {check_account}')
    
elif choice == 'Saving' or choice == "saving" or choice == 'savings' or choice == 'Savings':
    print(f' \n your balance is {sav_account}')
    
elif choice == 'Withdraw' or choice == "withdraw" or choice == 'withdrawing' or choice == 'Witherdrawing':
    print(f'which account would you like to withdraw from? Checking or Saving?')
    account = input()

    if account == 'Checking' or account == 'checking' or account == 'check' or account == 'Check':
        print(f' \n how much would you like to withdraw?')
        withdrawn = float(input())
        check_account = check_account - withdrawn
        print(f'\n Your new checking balance is {check_account}')

    elif account == 'Saving' or account == 'saving' or account == 'savings' or account == 'Savings':
        print(f' \n how much would you like to withdraw?')
        withdrawn = float(input())
        sav_account = sav_account - withdrawn
        print(f'\n Your new savings balance is {sav_account}')
elif choice == 'Deposit' or choice == "deposit" or choice == 'deposet' or choice == 'Deposet':
    print(f' \n which account would you like to deposit into? Checking or Saving?')
    account = input()

    if account == 'Checking' or account == 'checking' or account == 'check' or account == 'Check':
        print(f' \n how much would you like to deposit?')
        deposited = float(input())
        check_account = check_account + deposited
        print(f'\n Your new checking balance is {check_account}')

    elif account == 'Saving' or account == 'saving' or account == 'savings' or account == 'Savings':
        print(f' \n how much would you like to deposit?')
        deposited = float(input())
        sav_account = sav_account + deposited
        print(f'\n Your new savings balance is {sav_account}')
        
#first loop
 
choice = (input('"Hello What would you like to do today? \nChecking? \n   Saving? \n     Withdraw? \n       deposit? \n \t'))
if choice == 'Checking' or choice == "checking" or choice == 'checkings' or choice == 'Checkings':
    print(f' \n your balance is {check_account}')
    
elif choice == 'Saving' or choice == "saving" or choice == 'savings' or choice == 'Savings':
    print(f' \n your balance is {sav_account}')
    
elif choice == 'Withdraw' or choice == "withdraw" or choice == 'withdrawing' or choice == 'Witherdrawing':
    print(f'which account would you like to withdraw from? Checking or Saving?')
    account = input()

    if account == 'Checking' or account == 'checking' or account == 'check' or account == 'Check':
        print(f' \n how much would you like to withdraw?')
        withdrawn = float(input())
        check_account = check_account - withdrawn
        print(f'\n Your new checking balance is {check_account}')

    elif account == 'Saving' or account == 'saving' or account == 'savings' or account == 'Savings':
        print(f' \n how much would you like to withdraw?')
        withdrawn = float(input())
        sav_account = sav_account - withdrawn
        print(f'\n Your new savings balance is {sav_account}')
elif choice == 'Deposit' or choice == "deposit" or choice == 'deposet' or choice == 'Deposet':
    print(f' \n which account would you like to deposit into? Checking or Saving?')
    account = input()

    if account == 'Checking' or account == 'checking' or account == 'check' or account == 'Check':
        print(f' \n how much would you like to deposit?')
        deposited = float(input())
        check_account = check_account + deposited
        print(f'\n Your new checking balance is {check_account}')

    elif account == 'Saving' or account == 'saving' or account == 'savings' or account == 'Savings':
        print(f' \n how much would you like to deposit?')
        deposited = float(input())
        sav_account = sav_account + deposited
        print(f'\n Your new savings balance is {sav_account}')
choice = (input('"Hello What would you like to do today? \nChecking? \n   Saving? \n     Withdraw? \n       deposit? \n \t'))
if choice == 'Checking' or choice == "checking" or choice == 'checkings' or choice == 'Checkings':
    print(f' \n your balance is {check_account}')
    
elif choice == 'Saving' or choice == "saving" or choice == 'savings' or choice == 'Savings':
    print(f' \n your balance is {sav_account}')
    
elif choice == 'Withdraw' or choice == "withdraw" or choice == 'withdrawing' or choice == 'Witherdrawing':
    print(f'which account would you like to withdraw from? Checking or Saving?')
    account = input()

    if account == 'Checking' or account == 'checking' or account == 'check' or account == 'Check':
        print(f' \n how much would you like to withdraw?')
        withdrawn = float(input())
        check_account = check_account - withdrawn
        print(f'\n Your new checking balance is {check_account}')

    elif account == 'Saving' or account == 'saving' or account == 'savings' or account == 'Savings':
        print(f' \n how much would you like to withdraw?')
        withdrawn = float(input())
        sav_account = sav_account - withdrawn
        print(f'\n Your new savings balance is {sav_account}')
elif choice == 'Deposit' or choice == "deposit" or choice == 'deposet' or choice == 'Deposet':
    print(f' \n which account would you like to deposit into? Checking or Saving?')
    account = input()

    if account == 'Checking' or account == 'checking' or account == 'check' or account == 'Check':
        print(f' \n how much would you like to deposit?')
        deposited = float(input())
        check_account = check_account + deposited
        print(f'\n Your new checking balance is {check_account}')

    elif account == 'Saving' or account == 'saving' or account == 'savings' or account == 'Savings':
        print(f' \n how much would you like to deposit?')
        deposited = float(input())
        sav_account = sav_account + deposited
        print(f'\n Your new savings balance is {sav_account}')
choice = (input('"Hello What would you like to do today? \nChecking? \n   Saving? \n     Withdraw? \n       deposit? \n \t'))
if choice == 'Checking' or choice == "checking" or choice == 'checkings' or choice == 'Checkings':
    print(f' \n your balance is {check_account}')
    
elif choice == 'Saving' or choice == "saving" or choice == 'savings' or choice == 'Savings':
    print(f' \n your balance is {sav_account}')
    
elif choice == 'Withdraw' or choice == "withdraw" or choice == 'withdrawing' or choice == 'Witherdrawing':
    print(f'which account would you like to withdraw from? Checking or Saving?')
    account = input()

    if account == 'Checking' or account == 'checking' or account == 'check' or account == 'Check':
        print(f' \n how much would you like to withdraw?')
        withdrawn = float(input())
        check_account = check_account - withdrawn
        print(f'\n Your new checking balance is {check_account}')

    elif account == 'Saving' or account == 'saving' or account == 'savings' or account == 'Savings':
        print(f' \n how much would you like to withdraw?')
        withdrawn = float(input())
        sav_account = sav_account - withdrawn
        print(f'\n Your new savings balance is {sav_account}')
elif choice == 'Deposit' or choice == "deposit" or choice == 'deposet' or choice == 'Deposet':
    print(f' \n which account would you like to deposit into? Checking or Saving?')
    account = input()

    if account == 'Checking' or account == 'checking' or account == 'check' or account == 'Check':
        print(f' \n how much would you like to deposit?')
        deposited = float(input())
        check_account = check_account + deposited
        print(f'\n Your new checking balance is {check_account}')

    elif account == 'Saving' or account == 'saving' or account == 'savings' or account == 'Savings':
        print(f' \n how much would you like to deposit?')
        deposited = float(input())
        sav_account = sav_account + deposited
        print(f'\n Your new savings balance is {sav_account}')
choice = (input('"Hello What would you like to do today? \nChecking? \n   Saving? \n     Withdraw? \n       deposit? \n \t'))
if choice == 'Checking' or choice == "checking" or choice == 'checkings' or choice == 'Checkings':
    print(f' \n your balance is {check_account}')
    
elif choice == 'Saving' or choice == "saving" or choice == 'savings' or choice == 'Savings':
    print(f' \n your balance is {sav_account}')
    
elif choice == 'Withdraw' or choice == "withdraw" or choice == 'withdrawing' or choice == 'Witherdrawing':
    print(f'which account would you like to withdraw from? Checking or Saving?')
    account = input()

    if account == 'Checking' or account == 'checking' or account == 'check' or account == 'Check':
        print(f' \n how much would you like to withdraw?')
        withdrawn = float(input())
        check_account = check_account - withdrawn
        print(f'\n Your new checking balance is {check_account}')

    elif account == 'Saving' or account == 'saving' or account == 'savings' or account == 'Savings':
        print(f' \n how much would you like to withdraw?')
        withdrawn = float(input())
        sav_account = sav_account - withdrawn
        print(f'\n Your new savings balance is {sav_account}')
elif choice == 'Deposit' or choice == "deposit" or choice == 'deposet' or choice == 'Deposet':
    print(f' \n which account would you like to deposit into? Checking or Saving?')
    account = input()

    if account == 'Checking' or account == 'checking' or account == 'check' or account == 'Check':
        print(f' \n how much would you like to deposit?')
        deposited = float(input())
        check_account = check_account + deposited
        print(f'\n Your new checking balance is {check_account}')

    elif account == 'Saving' or account == 'saving' or account == 'savings' or account == 'Savings':
        print(f' \n how much would you like to deposit?')
        deposited = float(input())
        sav_account = sav_account + deposited
        print(f'\n Your new savings balance is {sav_account}')