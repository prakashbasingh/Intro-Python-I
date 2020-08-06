#JS objects
# Swift dictionaries
# Java Hasmaps?

# init an empty dict
d = {}

# one primary ise-case is to associate keys with values
# Dicts provide very efficient fetching of keys
# Dicts provide very de-duplication functionality since they never store duplicates of any keys

# create a dict with two key-value pairs
e = {"foo": 12, 11: "bar"}

# print out the value 12 from the dict
print(e["foo"])
print(e[11])

# iterate through dict key-value pairs
for key in e:
    print(key, e[key])

# iterate through key-valu pairs
for key, val in e.items():
    print(key, val)
    print(f"key is {key} and value is {val}")

# the `items` method on dicts is similar to the enumerate function for lists in that both give you access to index-value/key-value