import json
with open("categories.json",'r',encoding='utf-8')as f:
    data=json.load(f)
s=data.get("categories")
maxi=0
name=''
for key,val in s.items():
    if maxi<len(val):
        maxi=len(val)
        name=key
print(name)