import json

data_to_serialize = {"name": "red hot chilli peppers", "album": "californication"}
print(type(data_to_serialize))
print(data_to_serialize)
data_json = json.dumps(data_to_serialize)
print(type(data_json))
print(data_json)