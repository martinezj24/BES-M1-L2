
# Task 1: Merge Two Dcitonaries

dict_1 = {
'pie': 'apple',
'ice_cream': 'moose tracks',
'cobbler': 'peach',
'cake': None
}

dict_2 = {
'dinner': 'turkey',
'ice_cream': 'vanilla',
'appetizer': 'soup',
'cobbler': 'peach'
}

def merge_dictionaries(dict_1, dict_2):
    dict_1.update(dict_2)
    return dict_1

print(merge_dictionaries(dict_1, dict_2))

# Time Complexity:
# O(m), update() method processes each key-value pair in dict_2, where 'm' is the number of key-value pairs

#Space:
# dict_1 is directly modified so the space complexity is O(1) since no copy is made

