import json

with open("data/raw/sample.json", "r") as f:
    data = json.load(f)

for stu in data["students"]:
    print(stu["name"])