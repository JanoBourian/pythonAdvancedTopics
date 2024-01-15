import json 

rows = []
results = [(1, 'roboAdvisor', 'RoboAdvisor VIT'), (2, 'smartCash', 'Liquidez inteligente Vector MXN')]
for values in results:
    i, j, k = values
    res = {
        "id": i,
        "name": j,
        "description": k
    }
    rows.append(res)

data_products = json.dumps(rows, indent=4, sort_keys=True, default=str)
print(f"Type: {type(rows)}")
print(f"Type: {type(data_products)}") #AWS lambda uses str to return correctly a request