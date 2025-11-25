import json
with open("products.json",'r',encoding="utf-8") as f:
    data=json.load(f)

products=data.get('products')

eng_kop=max(products,key=lambda x:x["price"])


print(f"{eng_kop["name"]}:{eng_kop["price"]}")
