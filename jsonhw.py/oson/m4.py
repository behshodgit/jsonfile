import json
with open("people.json","r",encoding="utf-8")as f:
    data=json.load(f)
d=data.get("people")
s=max(d,key=lambda x:x["age"])
print(s["name"])
