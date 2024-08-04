"""
02-08-2024 21:42:03
Authorise: Beijing JinJiLong
Note: This is the data pre-processing against
"""

import pandas as pd

df = pd.read_csv('Data/nolableAccDataLabeled_Tag3_Cow638_2021-03-04.csv', header=None)

# print(df[0])

timestamp = df[0]
# Convert each value in the column to its binary representation
binary_timestamp = timestamp.apply(lambda x: ' '.join(format(ord(char), '08b') for char in x))

# Replace the original column with the binary column
df[0] = binary_timestamp

# Print the updated DataFrame
print(df[0])