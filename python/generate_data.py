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
import random

print("Welcome to NovaMart Retail Analytics!")
categories = [
    "Electronics",
    "Furniture",
    "Grocery",
    "Clothing",
    "Sports"
]
category_brands = {
    "Electronics": ["Asus", "HP", "Dell", "Samsung", "Lenovo"],
    "Furniture": ["Godrej", "Nilkamal", "IKEA", "Damro", "Pepperfry"],
    "Grocery": ["TATA", "Amul", "Dinshaw", "Parle", "Fortune"],
    "Clothing": ["Gucci", "Lacoste", "Levis", "Balenciaga", "Raymond"],
    "Sports": ["Puma", "Adidas", "Nike", "HRX", "Decathlon"]
}

def price_calculation(minimum_price, maximum_price):
    return random.randint(minimum_price, maximum_price)

category_price_range = {
    "Electronics": {"min" : 500,"max" : 120000},
    "Furniture": {"min" : 1500,"max" : 80000},
    "Grocery": {"min" : 20,"max" : 1000},
    "Clothing": {"min" : 300,"max" : 15000},
    "Sports": {"min" : 300,"max" : 50000} 
}

products = {
    "product_id": [],
    "product_name": [],
    "category": [],
    "brand": [],
    "price":[]
}
for i in range(1,101):
    current_category = categories[(i-1) % len(categories)]
    minimum_price = category_price_range[current_category]["min"]
    maximum_price = category_price_range[current_category]["max"]
    price = price_calculation(minimum_price, maximum_price)
    products["product_id"].append(i)
    products["product_name"].append(f"Product {i}")
    products["category"].append(current_category)
    products["brand"].append(random.choice(category_brands[current_category]))
    products["price"].append(price)
products_df = pd.DataFrame(products)                        
print("\nInventory Data:")
print(products_df)
