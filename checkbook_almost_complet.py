def current_balance():
    with open ('numbers.txt') as f:
        file_content = f.readlines()
        cleaner = [f.replace('\'', '') for f in file_content]
        cleaned_file = [float(f.replace('\n','')) for f in file_content]                                                     
        balance = sum(cleaned_file)
        print(f"Your current balance is {balance}.  Hope this helps, and come again!")
    
def total_debits():
    with open('numbers.txt', 'a') as f:
        file_content = f.readlines()
        cleaner = [f.replace('\''), '') for f in file_content]
        clean = [float(f.replace('\n', '')) for f in file_content]
        balance = sum(current_balance() + clean)
        print(f"Your balance is now {balance}.")

def total_credits():
    with open('numbers.txt', 'a') as f:
        file_content = f.readlines()
        cleaner = [f.replace("\'", '' for f in file_content]
        cleaned = [float(f.replace('\n', '')) for f in file_content]
        balance = sum(current_balance() + cleaned)
        print(f"Your current balance is now {balance}.")

print("-----------Welcome to Budget Bank--------------")
print("\n")
print("------------(The Bank That Cares)--------------")
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
    answer = int(input("How may we help you today? "))
    while True:
        if answer == 1:
            current_balance()
            main_menu
        elif answer == 2:
            total_debits()
            main(menu)
        elif answer == 3:
            total_credits()
            main(menu)
        elif answer == 4:
            print("Welp, we loved serving you, and see you next time!")
            exit
        elif not answer.isdigit():
            print("While easy, 'ABC' ain't 123 - we'll need an actual number between 1 and 4 to continue.")
        return
main_menu()

