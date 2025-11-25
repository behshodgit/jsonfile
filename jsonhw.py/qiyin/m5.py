import json
with open("social_users.json",'r',encoding="utf-8") as f:
    data=json.load(f)

social_users=data.get("users")
l=list(filter(lambda x:len(x["social"])>=2,social_users))
name=[i["name"]for i in l]
print(name )