# python .\python\generate_data.py
# # import pandas as pd

# # print("Welcome to NovaMart Retail Analytics!")

# # data = {
# #     "Product": ["Laptop", "Mouse", "Keyboard"],
# #     "Price": [65000, 800, 2500],
# #     "Stock": [25, 150, 75]
# # }

# # df = pd.DataFrame(data)

# # print("\nInventory Data:")
# # print(df)
import pandas as pd
print("Welcome to NovaMart Retail Analytics!")
products = {
    "product_id": [],
    "product_name": []
}

for i in range(1,101):
    products["product_id"].append(i)
    products["product_name"].append(f"Product {i}")
pr = pd.DataFrame(products)
print("\nInventory Data:")
print(pr)