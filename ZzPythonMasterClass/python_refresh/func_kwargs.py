def named(**kwargs):
    print(f'**kwargs: {kwargs}')

print(named(name="Bob", age=25))

### 
def print_user(**kwargs):
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

declarated = {"name": "car", "age": 25, "job": "program"}
languajes = {"java": 6, "sql": 8, "python": 10, "javascript": 9}

print_user(**declarated)
print_user(**languajes)

"""
def post(url, data=None, json = None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs) 
"""