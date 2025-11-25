import json 
with open("courses.json",'r',encoding='utf-8') as f:
    data=json.load(f)
courses=data.get("courses")

for key, vals in courses.items():
    total=0
    count=0
    for val in vals:
        total+=val["grade"]
        count+=1
        avg=total/count
    print(f"{key} :{avg}")