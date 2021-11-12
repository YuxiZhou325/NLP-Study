"""
28/09/2021
CIGP Machine Learning Engineer Internship assessment
"""
"""
References:
    - https://www.programcreek.com/python/example/96/re.IGNORECASE
    - https://www.kite.com/python/answers/how-to-use-re.sub()-in-python
    
"""

# Using list comprehension in Python, remove the above suffixes from the following company names (lower and upper case).
import re

list = [
    'Atlantia SpA',
    'Amazon.com',
    'Banco Bilbao Vizcaya Argentaria SA',
    'Carl Zeiss Meditec AG',
    'Antofagasta PLC',
    'Bunzl plc',
    'SK Hynix Inc',
    'Hang Seng Bank Ltd',
    'Salesforce.Com',
    'Kia Motors Corp',
    'Zurich Insurance Group AG',
]

suffixes = [
    'Inc',
    'LTD',
    'SA',
    'AG',
    '.com',
    'Corp',
    'Group',
    'SPA',
    'PLC',
]

# print([re.sub(suffixes, r'', item) for item in list])

# printing original list
print("The original list : " + str(list))

# Suffix removal from String list
# using list comprehension + endswith()
# res = [ele for ele in list if not ele.endswith()]
res = []
for item in list:
    # item = item.lower()
    # print(item)
    for suffix in suffixes:
        # suffix = suffix.lower()
        # use endswith() for mathing the suffixes
        if item.endswith(suffix):
            # print(item)
            # re = re.IGNORECASE
            # use re.sub for replace suffixes for null (thus remove suffixes)
            # use re.IGNORECASE for case insensitive
            new_item = re.sub(suffix, r'', item, re.IGNORECASE)
            res.append(new_item)

# printing result

print("List&Dictionary after removal of suffix elements : " + str(res))
