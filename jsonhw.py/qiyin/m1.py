import json

with open("orders.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

orders = data.get("orders")


customer_totals = {}

for order in orders:
    customer = order["customer"]
    amount = order["amount"]
    

    if customer not in customer_totals:
        customer_totals[customer] = amount
    else:
        customer_totals[customer] += amount 


for customer, total in customer_totals.items():
    print(f"{customer}: {total}")
