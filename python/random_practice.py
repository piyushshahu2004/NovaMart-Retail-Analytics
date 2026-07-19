import pandas as pd
import random
from datetime import datetime, timedelta

# x = datetime.now()

# # Prints each item on a new line
# print(x.day, x.strftime("%b"), x.year)

def date_added_calculation():
    dates = datetime.now()
    start_date = datetime.now(2024,1, 1)
    current_date = dates.day, dates.strftime("%b"), dates.year
    return current_date, start_date

print(date_added_calculation())