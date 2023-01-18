import json

x = json.load(open('json_example.json'))
print(x, type(x))

s = """{
"employees":[
    {"firstName":"John", "lastName":"Doe", "age": 18},
    {"firstName":"Anna", "lastName":"Smith", "age": 25},
    {"firstName":"Peter", "lastName":"Jones", "age": 52}
]
}"""

x = json.loads(s)
print(x, type(x))

d = {
    'u': 5,
    "z": 3,
    'y': [
        3, 4, 5, 6, {'asd': "dsa", "yui": 'iuy'}
    ]
}

json.dump(d, open('json_example_output.json', mode='w'), indent=2)
s = json.dumps(d, indent=2)
print(s, type(s))