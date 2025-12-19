import json
data = {
    "name " : "sam",
    "is" : True
}
with open("json.json","w")as f:
    json.dump(data,f,indent=4,sort_keys =True)