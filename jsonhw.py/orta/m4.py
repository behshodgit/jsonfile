import json
with open("births.json",'r',encoding='utf-8') as f:
    data=json.load(f)
d=data.get("people")

s=list(filter(lambda x:x["birth_year"]>1990,d))

old_year=[i["name"] for i in s]
print(old_year)