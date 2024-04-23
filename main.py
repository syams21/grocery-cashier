import pandas as pd
import transaction
import update_stock

data = pd.read_excel("items.xlsx")

def show_menu():
    print("\n======= MENU =======")
    print("[1] Transaction")
    print("[2] Update Stock")
    print("[3] Exit Program")

def main():
    while True:
        show_menu()
        option = int(input("Enter your option: "))

        if option == 1:
            transaction.main()
        elif option == 2:
            update_stock.main()
        elif option == 3:
            exit()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
