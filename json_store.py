# storage/json_store.py week-8

import json

data = {"name": "Ram", "marks": 90}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    print(json.load(f))