# solution of task 1.1
import pandas as pd

# read csv data file with pandas
df = pd.read_csv('G:\JobApply\BayWaRe\Plant_1_Generation_Data.csv')

# view the data frame
print(df.head())

# view TOTAL_YIELD column
print(df.TOTAL_YIELD)

# check if there is missing values in TOTAL_YIELD column
print(df['TOTAL_YIELD'].isna().any())

# view missing values in TOTAL_YIELD column
print(df['TOTAL_YIELD'].isnull())

# group the dataframe according to the inverter id
grouped_df = df.groupby('SOURCE_KEY', as_index='False')

# print(grouped_df.head())

# grouped_df.to_csv('G:\JobApply\BayWaRe\out.csv')

# df['TOTAL_YIELD'].isnull() / df.groupby('SOURCE_KEY')['TOTAL_YIELD'].transform('sum')

# calculate the total yield for each inverter
# grouped_df['TOTAL_YIELD'].sum()

# calculate the total rows for each inverter
print(grouped_df['TOTAL_YIELD'].count())

# calculate the % of missing data for each inverter
null_data = 0
for row in grouped_df['TOTAL_YIELD']:
    if df['TOTAL_YIELD'].isnull().any():
        null_data += 1
    print(null_data)

# print(null_data / grouped_df['TOTAL_YIELD'].count())



# df['TOTAL_YIELD'].isnull().count() / grouped_df['TOTAL_YIELD'].count()
