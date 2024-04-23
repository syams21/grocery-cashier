import pandas as pd

data = pd.read_excel("items.xlsx")

def main():
    global data

    id_input = int(input("Item id: "))
    quantity_input = int(input("Quantity: "))

    if 'id' in data.columns:
        item_target = data.loc[data["id"] == id_input]
        item_stock = item_target.iloc[0]["stock"]
        item_price = item_target.iloc[0]["price"]

        if not item_target.empty:
            if quantity_input <= item_stock:
                total_price = item_price * quantity_input

                print("Total price: ", total_price)

                payment_input = int(input("Payment amount: "))
                change_amount = payment_input - total_price
                
                if payment_input >= total_price:
                    print("\nTransaction successful.")
                    print("Change: ", change_amount)

                    data.loc[data["id"] == id_input, "stock"] = item_stock - quantity_input
                    
                    data.to_excel("items.xlsx", index=False)
                    data = pd.read_excel("items.xlsx") # reread data
                    item_target = data.loc[data["id"] == id_input]

                    print("\nItem has been updated.")
                    print(item_target)
                
                else:
                    print("Payment amount is not enough.")

            else:
                print("Insufficient stock:")
                print(item_target)

        else:
            print("Data not found.")

    else:
        print("Column 'id' not found in DataFrame.")