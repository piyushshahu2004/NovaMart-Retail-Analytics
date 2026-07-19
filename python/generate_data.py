import pandas as pd
import random
from datetime import datetime, timedelta

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

category_products = {
    "Electronics": ["HP Pavilion 15", "Dell Inspiron 14", "Lenovo IdeaPad Slim 3", "Asus Vivobook 15", "Samsung Galaxy A56", "HP Victus", "Dell XPS 13", "Lenovo ThinkPad E14", "Asus ROG Strix", "Samsung Galaxy Tab S10"],
    "Furniture": ["Office Chair", "Study Table", "Wooden Wardrobe", "Queen Size Bed", "Bookshelf", "Coffee Table", "TV Unit", "Dining Table", "Sofa Set", "Computer Desk"],
    "Grocery": ["Amul Butter 500g", "Tata Salt 1kg", "Fortune Sunflower Oil 1L", "Parle-G Biscuits", "Aashirvaad Atta 5kg", "Maggi Noodles", "Tata Tea Gold", "Amul Milk 1L", "Fortune Rice", "Sugar 1kg"],
    "Clothing": ["Levi's 511 Jeans", "Raymond Formal Shirt", "Gucci Leather Belt", "Lacoste Polo T-Shirt", "Balenciaga Hoodie", "Nike Track Pants", "Formal Trousers", "Casual Shirt", "Denim Jacket", "Cotton T-Shirt"],
    "Sports": ["Nike Football", "Puma Running Shoes", "Adidas Cricket Bat", "HRX Yoga Mat", "Decathlon Backpack", "Badminton Racket", "Skipping Rope", "Gym Gloves", "Basketball", "Dumbbell Set"]
}

category_suppliers = {
    "Electronics": ["Tech Distributors Ltd.","Digital World Pvt Ltd","Smart Devices India"],
    "Furniture": ["HomeStyle Furnishings","Modern Furniture Co.","Urban Living"],
    "Grocery": ["FreshMart Supplies","Daily Needs Wholesale","ABC Foods"],
    "Clothing": ["Fashion Hub","StyleWear Distributors","Elite Garments"],
    "Sports": ["Active Sports Ltd.","FitGear India","Champion Sports Supply"]
}

def price_calculation(minimum_price, maximum_price):
    return random.randint(minimum_price, maximum_price)

def stock_calculation(minimum_stock, maximum_stock):
    return random.randint(minimum_stock, maximum_stock)

def discount_calculation(minimum_discount, maximum_discount):
    return random.randint(minimum_discount, maximum_discount)

category_price_range = {
    "Electronics": {"min" : 500,"max" : 120000},
    "Furniture": {"min" : 1500,"max" : 80000},
    "Grocery": {"min" : 20,"max" : 1000},
    "Clothing": {"min" : 300,"max" : 15000},
    "Sports": {"min" : 300,"max" : 50000} 
}

category_stock_range = {
    "Electronics": {"min" : 5,"max" : 80},
    "Furniture": {"min" : 2,"max" : 30},
    "Grocery": {"min" : 100,"max" : 1000},
    "Clothing": {"min" : 20,"max" : 300},
    "Sports": {"min" : 10,"max" : 150} 
}

category_discount_range = {
    "Electronics": {"min" : 5,"max" : 25},
    "Furniture": {"min" : 10,"max" : 40},
    "Grocery": {"min" : 0,"max" : 10},
    "Clothing": {"min" : 10,"max" : 60},
    "Sports": {"min" : 5,"max" : 35} 
}
products = {
    "product_id": [],
    "product_name": [],
    "category": [],
    "brand": [],
    "price":[],
    "stock_quantity": [],
    "discount_percentage" : [],
    "selling_price" : [],
    "supplier" : [],
}
for i in range(1,101):
    current_category = categories[(i-1) % len(categories)]
    minimum_price = category_price_range[current_category]["min"]
    maximum_price = category_price_range[current_category]["max"]
    minimum_stock = category_stock_range[current_category]["min"]
    maximum_stock = category_stock_range[current_category]["max"]
    minimum_discount = category_discount_range[current_category]["min"]
    maximum_discount = category_discount_range[current_category]["max"]
    price = price_calculation(minimum_price, maximum_price)
    stock = stock_calculation(minimum_stock, maximum_stock)
    discount = discount_calculation(minimum_discount, maximum_discount)
    selling_price = round(price - (price * discount / 100), 2)
    products["product_id"].append(i)
    products["product_name"].append(random.choice(category_products[current_category]))
    products["category"].append(current_category)
    products["brand"].append(random.choice(category_brands[current_category]))
    products["price"].append(price)
    products["stock_quantity"].append(stock)
    products["discount_percentage"].append(discount)
    products["selling_price"].append(selling_price)
    products["supplier"].append(random.choice(category_suppliers[current_category]))
products_df = pd.DataFrame(products)                        
print("\nInventory Data:")
print(products_df)
