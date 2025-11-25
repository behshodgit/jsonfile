import json
with open("people.json",'r',encoding="utf-8") as f:
    text=json.load(f)


names=[person["name"]for person in text["people"]]
print(names)