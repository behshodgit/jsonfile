import json
with open("students.json",'r',encoding="utf-8") as f:
    data=json.load(f)
s=data.get("students")
for i in s:
    print(i["name"],sum(i["grades"])/len(i["grades"]))