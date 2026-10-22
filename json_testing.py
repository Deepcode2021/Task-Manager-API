import json
from datetime import datetime

# id (unique integer), 
# title (required non-empty string), 
# description (optional), 
# completed (boolean default false), 
# created_at (timestamp).

data = {
    "id" : 11,
    "title" : 'nice',
    "descrition": 'yooo',
    "completed": False,
    "time_at" : str(datetime.now())
}
# data = {11,"nice","yoo",True,None}

with open("test.json" , "w")as file:
    json_data = json.dump(data , file , indent=2)

with open("test.json", "r") as file:
    load_data = json.load(file)

print(load_data)