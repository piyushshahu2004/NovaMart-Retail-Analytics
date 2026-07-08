import random

categories = [
    "Electronics",
    "Furniture",
    "Grocery",
    "Clothing",
    "Sports"
]

for i in range(10):
    print(random.choice(categories))