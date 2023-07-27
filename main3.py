import json

# a = str({'name': 'John Doe', 'age': 30, 'address': {'street': '123 Main St', 'city': 'Anytown', 'state': 'CA', 'zip_code': '12345'}})
# d = json.dumps(eval(a), indent=4)
# print(d)


a = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip_code": "12345"
    }
}

b = {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip_code': '12345'
    }
}

assert a == b

