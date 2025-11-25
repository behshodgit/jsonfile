import json

with open("products.json","r",encoding="utf-8")as f:
    data=json.load(f)

for product in data["products"]:
    print(f"{product["name"]}:{product["price"]}")