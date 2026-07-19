from datetime import datetime, timedelta
import random
# today = datetime.now()

# print(today)

# print(today.year)
# print(today.month)
# print(today.day)

# start = datetime(2024, 1, 1)

# print(start)

# print(start + timedelta(days=10))

# print(today - start)

def date_added_calculation():
    start = datetime(2024,1,1)
    today = datetime.now()
    difference = today - start
    new_added_date = start + timedelta(days = random.randint(0,difference.days))
    return new_added_date

print(date_added_calculation())