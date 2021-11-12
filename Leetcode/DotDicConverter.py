"""
28/09/2021
CIGP Machine Learning Engineer Internship assessment

Create a function to convert any dictionary from json_file notation to "dot notation"
your code must be efficient and must not use any library.
"""

"""
References:
    - https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary/41274937#41274937
    - https://www.sqlpac.com/en/documents/python-handling-dictionaries-with-dot-notation.html
    - https://www.py4u.net/discuss/1151024
    - https://www.geeksforgeeks.org/python-convert-nested-dictionary-into-flattened-dictionary/
"""

import json

# Load JSON file
with open('test_dictionary_regular.json') as json_file:
    data = json.load(json_file)


class dotdictconverter(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


# class ClsProps:
#     def __init__(self, data):
#         self.__dict__ = data
#
# props = ClsProps(data)
# print(props.re)


# mydict = {'val': 'it works'}
# nested_dict = {'val': 'nested works too'}
# mydict = dotdictconverter(mydict)
# print(mydict.val)
# # 'it works'
#
# mydict.nested = dotdictconverter(nested_dict)
# print(mydict.nested.val)

dotdict = dotdictconverter(data)
print(dotdict.name)

dotdict.re = dotdictconverter(dotdict.re)
print(dotdict.re.primStrat)

for key1, value1 in dotdict.re.items():
    print(key1.replace('%s', 're' + '%s'))


# a function for converting regular nested dictionary into flattened dictionary ("Dot Notation")
# by default separator '.'
def dot_dict(dict_data, separator='.', prefix=''):
    return {prefix + separator + k if prefix else k: v
            for kk, vv in dict_data.items()
            for k, v in dot_dict(vv, separator, kk).items()
            } if isinstance(dict_data, dict) else {prefix: dict_data}


# initialising_dictionary
ini_dict = {'geeks': {'Geeks': {'for': 7}},
            'for': {'geeks': {'Geeks': 3}},
            'Geeks': {'for': {'for': 1, 'geeks': 4}}}

# printing initial dictionary
print("regular_dictionary", str(data))

# printing final dictionary
print("dot_dictionary", str(dot_dict(data)))


with open('data.json', 'w') as fp:
    json.dump(dot_dict(data), fp, indent=4)


