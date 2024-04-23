import pandas as pd

data = pd.read_excel("items.xlsx")

def main():
    global data

    id_update = int(input("item id: "))
    stock_update = int(input("stock: "))

    if 'id' in data.columns:
        item_target = data.loc[data["id"] == id_update]

        if not item_target.empty:
            if stock_update >= 0 and stock_update != item_target.iloc[0]["stock"]:
                data.loc[data["id"] == id_update, "stock"] = stock_update
                data.to_excel("items.xlsx", index=False)
                data = pd.read_excel("items.xlsx")  # reread data
                item_target = data.loc[data["id"] == id_update]
                print("\nItem has been updated.")
                print(item_target)

            elif stock_update < 0:
                print("Stock cannot be negative.")
                
            else:
                print("Stock did not change.")

        else:
            print("Data not found.")

    else:
        print("Column 'id' not found in DataFrame.")
