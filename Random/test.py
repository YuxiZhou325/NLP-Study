import pandas as pd
import re

n_com = pd.read_excel('file.xlsx', sheet_name='Sheet3')

t_com = pd.read_excel('file.xlsx', sheet_name='T Committee')

# print(n_com)
# print(t_com)

print(n_com.columns)
print(t_com.columns)

n_com_list = n_com['Committee Files']
t_com_list = t_com['File Name']

print(n_com_list)

# diff = n_com_list.str.lower().str.replace('s/+', "")  != t_com_list.str.strip().str.replace('s/+', "")

# print(diff)

print(n_com_list.equals(t_com_list))
print(n_com_list.reset_index(drop=True).equals(t_com_list.reset_index(drop=True)))


# filename = 'result.xlsx'
# f = open(filename, 'w')
#
# headers = 'Unmatched File\n'
# f.write(headers)



