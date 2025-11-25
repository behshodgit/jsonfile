import json
with open("contacts.json",'r',encoding="utf-8") as f:
    data=json.load(f)
s=[i["phone"]for i in data["contacts"]]
print(s)