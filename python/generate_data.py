import pandas as pd

print("Welcome to NovaMart Retail Analytics!")

data = {
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Price": [65000, 800, 2500],
    "Stock": [25, 150, 75]
}

df = pd.DataFrame(data)

print("\nInventory Data:")
print(df)