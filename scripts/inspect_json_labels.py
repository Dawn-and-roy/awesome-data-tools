import json
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(type(data))
print(list(data.keys()))
