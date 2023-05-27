list_of_keys = ["key1", "key2", "key3"]
list_of_values = [100, 200, 300]

my_dict = {}
for x in range(len(list_of_keys)):
    key = list_of_keys[x]
    value: int = list_of_values[x]
    my_dict[key] = value

print(my_dict.items())
