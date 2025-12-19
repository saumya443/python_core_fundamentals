import json
json_Str = '{"name":"saumya","is":true}'
py_obj = json.loads(json_Str)
print(type(py_obj), py_obj)