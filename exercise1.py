"""
Give the data, construct a dictionary in this format:
output = {
    'Biology': ['Alice', 'David'],
    'Chemistry': ['Alice'],
    ...
}
"""
data = {
    'Alice': 'Biology, Maths, Chemistry',
    'Bob': 'Maths, English,Physics',
    'Charlie': 'Maths',
    'David': 'Biology,Chinese'
}

"""
def reverse_dict(input_data):
    # TODO
    return output  # TODO


reverse_dict(input_data=data)
"""

dict1 = {}
for k, v in data.items():
    for subjects in v.split(','):
        if subjects not in dict1:
            dict1[subjects] = [k]
        else:
            dict1[subjects].append(k)

print(dict1)
