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


def reverse_dict(x):
    dict1 = {}
    for k, v in data.items():
        for subjects in v.replace(' ','').split(','):
            if subjects not in dict1:
                dict1[subjects] = [k]
            else:
                dict1[subjects].append(k)
    return dict1
print(reverse_dict(data))
