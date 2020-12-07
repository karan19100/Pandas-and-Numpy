import pandas as pd
import numpy as np

df= pd.read_csv(r'C:\Users\USer\Desktop\EXP6\employees.csv')
print(df.head())
print(df.dtypes)
print(df.describe())

#  task 1 mark invalid/ corrupt values as missing

# print('Salary')
# print(df['Salary'].head(10))




# missing_value_formats = ["n.a.","?","NA","n/a", "na", "--"]
# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP6\employees.csv', na_values = missing_value_formats)

# def make_int(i):
#     try:
#         return int(i)
#     except:
#         return pd.np.nan

# # apply make_int function to the entire series using map
# df['Salary'] = df['Salary'].map(make_int)
# print(df['Salary'].head())



# task 2 Marking missing values using isnull and notnull

# print(df['Gender'].isnull().head(10)) # NaN values are marked True
# print(df['Gender'].notnull().head(10)) # non-NaN values are marked True




# returns True on indices for which Gender is not NaN
null_filter = df['Gender'].notnull()
print(df[null_filter].head())

# task 3 

new_df = df.dropna(axis=0)   # drop all rows with NaN values
print(new_df.isnull().values.any())   # check if we have any NaN values in our dataset


new_df = df.dropna(axis = 0, how ='any')  # drop all rows with atleast one NaN 
new_df = df.dropna(axis = 0, how ='all')  # drop all rows with all NaN
new_df = df.dropna(axis = 1, how ='any')  # drop all columns with atleast one NaN
new_df = df.dropna(axis = 1, how ='all')  # drop all columns with all NaN

# df['Salary'].fillna(0)
# df['Gender'].fillna('No Gender')
# df['Salary'].fillna(method='pad')

df['Salary'].replace(to_replace = np.nan, value = 0)









