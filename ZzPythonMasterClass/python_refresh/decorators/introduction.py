## Search Function

def search_people(sequence:list, expected, finder) -> list:
    result = []
    for p in sequence:
        if finder(p) < expected:
            result.append(p)
    if result:
        return result
    raise RuntimeError(f'Could not finds an element with {expected}')


def finder(element):
    return element["age"]


people = [
    {"name": "jorge", "age": 23},
    {"name": "dardo", "age": 31},
    {"name": "pedro", "age": 42},
    {"name": "maria", "age": 31},
]

try:
    result = search_people(people, 15, finder=finder)
    print(f'result: {result}')
except RuntimeError as e:
    print(f'error: {e}')

