def current_balance():
    balance = total_credits() - total_debits()
    print(f"Your current balance is {balance}.  Sound about right?")
    
def total_debits():
    """
    Function to get the total amount of charges / debits
    """
    charge = int(input("Uh-oh.  Spending money.  How much did you spend? "))
    if charge >= 0:
        print("Okay, you should be fine.  Your new balance is ", current_balance() - charge)
    else:
        print("Something's not right.  Are you sure you put in a positive number? ")
        print("Please try again: ")
    return 

def total_credits():
    """
    Function to get the total amount of deposits
    """
    amount = int(input("Whoo-hoo!  Deposits!  How much are you depositing? "))
    if amount >= 0:
        print("Good news!  Your current balance is" , current_balance() + amount)
    else:
        print("You're not adding enough money.  Keep depositing or go broke!")
    return 


print("-----------Welcome to Budget Bank!--------------")
print("\n")
print("------------(The Bank That Cares)---------------")
def main_menu():
    """
    Main Menu function to allow the user to navigate the 
    front-page list of choices
    """
    print("Please choose from the following menu: ")
    print("1. View balance")
    print("2. Record a debit / withdraw")
    print("3. Record a credit / deposit")
    print("4. Exit program")
    print("\n")
    answer = int(input("From the selections above, how may we serve you today? "))
    while answer <= 4:
        if answer == 1:
            current_balance()
        elif answer == 2:
            total_debits()
        elif answer == 3:
            total_credits()
        elif answer == 4:
            print("Welp, thanks for stopping by, and see you next time!")
            exit
        elif not answer.isdigit():
            print("While easy, 'ABC' ain't 123 - we'll need an actual number between 1 and 4 to continue.")
        return
main_menu()

# #------------------------------------
# def total_credits():
#     """
#     Function to get the total amount of deposits
#     """
#     amount = int(input("Whoo-hoo!  Deposits!  How much are you depositing? "))
#     total = 0
#     if amount >= 0 and current_balance >= 0:
#         total += amount
#         print("Good news!  Your current balance is" , current_balance + amount)
#     else:
#         print("You're not adding enough money.  Keep depositing or go broke!")
#     return total

# total_credits()
# #-------------------------------------
# def total_debits():
#     """
#     Function to get the total amount of charges / debits
#     """
#     charge = int(input("Uh-oh.  Spending money.  How much did you spend? "))
#     total = 0
#     if charge >= 0 and charge <= current_balance:
#         total += charge
#         print("Okay, you should be fine.  Your new balance is ", current_balance - charge)
#     else:
#         print("Something's not right.  Are you sure you put in a positive number? ")
#         print("Please try again: ")
#         total_debits()
#     return total

# total_debits()

# #---------------------------------------
# def current_balance():
#     return total_credits - total_debits

# #---------------------------------------
