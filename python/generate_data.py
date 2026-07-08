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
categories = [
    "Electronics",
    "Furniture",
    "Grocery",
    "Clothing",
    "Sports"
]
category_brands = {
    "Electronics": ["Asus", "HP", "Dell", "Samsung", "Lenevo"],
    "Furniture": ["Godrej", "Nilkamal", "IKEA", "Damro", "Pepperfry"],
    "Grocery": ["TATA", "Amul", "Dinshaw", "Parle", "Fortune"],
    "Clothing": ["Gucchi", "Lacoste", "Levis", "Balenciaga", "Raymond"],
    "Sports": ["Puma", "Adidas", "Nike", "HRX", "Decathalon"]
}
products = {
    "product_id": [],
    "product_name": [],
    "category": [],
    "brand": []
}
for i in range(1,101):
    products["product_id"].append(i)
    products["product_name"].append(f"Product {i}")
    products["category"].append(categories[(i-1) % len(categories)])
    products["brand"].append(category_brands[categories[(i-1) % len(categories)]][(i-1) % len(categories)]) # "(i-1) % len(categories)" instead of this we can write 0  also for selecting first brand name fromm each category
products_df = pd.DataFrame(products)                        
print("\nInventory Data:")
print(products_df)