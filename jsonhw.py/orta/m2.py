import json
with open("users1.json",'r',encoding="utf-8") as f:
    data=json.load(f)

s=data.get("users")

l=list(filter(lambda x:x["role"]=="admin",s))

s=[i["name"]for i in l]
print(s)