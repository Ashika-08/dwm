import re
from datetime import datetime

# Raw data
data = [
    [1, 21, "1L", "Male", "31.05.1992", "No"],
    [2, 35, "100000", "Male", "10-05-2002", "No"],
    [3, 26, "45000", "Male", "Aug 5, 2000", "Yes"],
    [4, 45, "", "Male", "", "Yes"],
    [5, 67, "10000", "Female", "31.03.1986", "Yes"],
    [6, "", "10000", "Female", "10/5/1987", "No"],
    [7, 32, "5$", "Female", "31.05.1992", "Yes"],
    [8, 31, "5 Dollars", "Male", "10-05-2002", "No"],
    [9, "", "10000", "Female", "Aug 5, 2000", "Yes"],
    [10, 42, "15000", "Female", "Sep 12'2000", "Yes"],
    [11, "", "25000", "Female", "31.03.1986", "Yes"],
    [12, 32, "35000", "Male", "10/5/1987", "Yes"],
    [13, 35, "150000", "Female", "Sep 12'2000", "Yes"],
    [14, 35, "35000", "Male", "31.03.1986", "No"],
]

# Function to convert various income formats to a standardized numeric format
def standardize_income(income):
    if 'L' in income:
        return 100000  # Assuming 1L is 100000
    income = re.sub(r'[^\d]', '', income)
    return int(income) if income else 0

# Function to standardize date format to YYYY-MM-DD
def standardize_date(dob):
    for fmt in ('%d.%m.%Y', '%d-%m-%Y', '%b %d, %Y', '%b %d\'%Y', '%m/%d/%Y'):
        try:
            return datetime.strptime(dob, fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    return None  # Return None if the date format is unrecognized

# Extract ages and incomes for statistical calculation
ages = [row[1] for row in data if row[1] != ""]
incomes = [standardize_income(row[2]) for row in data if row[2] != ""]

# Calculate mean and median for Age and Income
mean_age = sum(ages) / len(ages)
mean_income = sum(incomes) / len(incomes)
median_age = sorted(ages)[len(ages) // 2]
median_income = sorted(incomes)[len(incomes) // 2]

# Fill missing Age with mean value
for row in data:
    if row[1] == "":
        row[1] = round(mean_age)
    row[2] = standardize_income(row[2])
    row[4] = standardize_date(row[4]) if row[4] else None

# Calculate the proportion of people who buy
buy_count = sum(1 for row in data if row[5] == "Yes")
total_count = len(data)
buy_proportion = buy_count / total_count

# Output the cleaned data and statistical measures
print("Cleaned Data:")
for row in data:
    print(row)

print("\nStatistical Measures:")
print(f"Mean Age: {mean_age:.2f}")
print(f"Mean Income: {mean_income:.2f}")
print(f"Median Age: {median_age}")
print(f"Median Income: {median_income}")
print(f"Proportion of Buys: {buy_proportion:.2f}")
