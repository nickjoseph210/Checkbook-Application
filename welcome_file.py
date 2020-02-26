print("-----------Welcome to BANK--------------")
print("\n")
def main_menu():
    print("Please choose from the following menu: ")
    print("1. View balance")
    print("2. Record a debit / withdraw")
    print("3. Record a credit / deposit")
    print("4. Exit program")
    print("\n")
    answer = int(input("How may we help you today?"))
    while answer <= 4:
        if answer == 1:
            balance_check()
        elif answer == 2:
            spend_check()
        elif answer == 3:
            deposit_check()
        elif answer == 4:
            print("Welp, thanks for stopping by, and see you next time!")
            exit
        elif not answer.isdigit():
            print("While easy, 'ABC' ain't 123, so we'll need an actual number between 1 and 4 to continue.")
        return
main_menu()