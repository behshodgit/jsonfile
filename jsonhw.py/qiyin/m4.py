import json 
with open("sales.json",'r',encoding="utf-8") as f:
    data=json.load(f)

sales=data.get("sales")

oxir={}
for sale in sales:
    month=sale["month"]
    amount=sale["amount"]

    if month not in oxir:
        oxir[month]=amount
    else:
        oxir[month]+=amount
for key,val in oxir.items():
    print(f"{key} :{val}")




