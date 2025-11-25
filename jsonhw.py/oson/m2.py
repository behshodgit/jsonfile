import json

with open("users.json",'r',encoding="utf-8") as f:
    data=json.load(f)

summa=[i["age"]for i in data["users"]]
print(sum(summa))