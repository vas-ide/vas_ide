import json

string_as_json = '{"answer": "Hello - Docker !"}'
obj = json.loads(string_as_json)

key = "answer"

if key in obj:
    print(obj[key])
else:
    print(f"No information in json file on '{key}'")