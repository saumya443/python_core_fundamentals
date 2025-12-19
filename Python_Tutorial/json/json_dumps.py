import json
py_obj = {"name":"saumya","is":True}
json_str = json.dumps(py_obj)
print(type(json_str), json_str)