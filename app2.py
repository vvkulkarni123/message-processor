transactions = [
    ("Alice", 120),
    ("Bob", 80),
    ("Alice", 90),
    ("Charlie", 150),
    ("Bob", 60),
    ("Alice", 50),
    ("David", 200),
    ("Charlie", 70),
    ("Eve", 110)
]

# Step 1: Calculate each customer's total
totals = {}

for customer, amount in transactions:
    if customer in totals:
        totals[customer] += amount
    else:
        totals[customer] = amount

# Step 2: Sort by total spent in descending order
sorted_customers = sorted(totals.items(), key=lambda x: x[1], reverse=True)

# Step 3: Take the top 3
top_3 = sorted_customers[:3]

# Step 4: Display result
print("Top 3 customers by total spent:")
for customer, total in top_3:
    print(f"{customer}: {total}")