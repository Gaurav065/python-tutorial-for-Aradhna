# dictionary is a collection of key-value pairs


d1 = {
    "name": "John",
    "age": 30,
    "city": "Melbourne",
    "is_student": False,
}

print(d1['name'])


d2 = dict(series='rtx40', memory=16, price=2000.15, is_available=True)
print(d2)

print(d2.get('Cuda_cores','not found'))


d2['Cuda_cores'] = 10000
print(d2)

d2['series'] = 'rtx50'
print(d2)


d2.pop('Cuda_cores')
print(d2)


del d1['is_student']
print(d1)




# Method	Description
# dict.get(key)	Returns value or None
# dict.keys()	Returns all keys
# dict.values()	Returns all values
# dict.items()	Returns key-value pairs (tuples)
# dict.pop(key)	Removes item by key
# dict.update(dict2)	Merges another dictionary
# dict.clear()	Empties the dictionary
# key in dict	Checks if a key exists