# customer_report.py

# List of customers (name, TeleBirr balance)
customers = [
    ("Almaz", 1500),
    ("Dawit", 700),
    ("Tigist", 200),
    ("Hanna", 1200),
    ("Samuel", 450),
]

# Function to determine customer tier
def tier(balance):
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    return "Basic"

# Counters
premium_count = 0
standard_count = 0
basic_count = 0

print("CUSTOMER REPORT")

# Loop through customers
for name, balance in customers:
    customer_tier = tier(balance)
    print(f"{name}: {customer_tier} ({balance} ETB)")

    if customer_tier == "Premium":
        premium_count += 1
    elif customer_tier == "Standard":
        standard_count += 1
    else:
        basic_count += 1

print("Summary")
print(f"Premium Customers : {premium_count}")
print(f"Standard Customers: {standard_count}")
print(f"Basic Customers   : {basic_count}")