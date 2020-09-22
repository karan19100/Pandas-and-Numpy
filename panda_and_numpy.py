import pandas as pd
import numpy as np


# df = pd.read_csv(r'C:\Users\Admin\Desktop\Life Expectancy Data.csv')
# print(df)


# #  Average Life Expectancy over 15 Years in Afghanistan.


# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv')
# print(df)
# df = df.loc[df['Country'] == 'Afghanistan']
# country = df['Country'][1]
# life_expectancy = df['Life expectancy '].mean()
# final_answer = [country, life_expectancy]
# print(final_answer)


# #  Maximum polio in the country over 15years.


df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','Polio'])
print(df)
x=df[df.Polio == df.Polio.max()]
final_answer = [x]
print(final_answer)


# #  Maximum percentage expenditure of the Developing country over 15years.


# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','percentage expenditure'])
# print(df)
# ck = df.loc[df['Status'] == 'Developing']
# finalAnswer = ck.loc[ck['percentage expenditure'].max() == ck['percentage expenditure']]
# print(finalAnswer)


# #  Minimum percentage expenditure of the Developing country over 15years.


# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','percentage expenditure'])
# print(df)
# ck = df.loc[df['Status'] == 'Developing']
# finalAnswer = ck.loc[ck['percentage expenditure'].min() == ck['percentage expenditure']]
# print(finalAnswer)



# #  Maximum percentage expenditure of the Developed country over 15years.


# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','percentage expenditure'])
# print(df)
# ck = df.loc[df['Status'] == 'Developed']
# finalAnswer = ck.loc[ck['percentage expenditure'].max() == ck['percentage expenditure']]
# print(finalAnswer)


# #  Minimum percentage expenditure of the Developed country over 15years.


# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','percentage expenditure'])
# print(df)
# ck = df.loc[df['Status'] == 'Developed']
# finalAnswer = ck.loc[ck['percentage expenditure'].min() == ck['percentage expenditure']]
# print(finalAnswer)


#  Highest Life Expectancy in Developing Country over 15 years.


# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','Life expectancy '])
# print(df)
# ck = df.loc[df['Status'] == 'Developing']
# finalAnswer = ck.loc[ck['Life expectancy '].max() == ck['Life expectancy ']]
# print(finalAnswer)


# # Highest Life Expectancy in Developed Country over 15 years.


# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','Life expectancy '])
# print(df)
# ck = df.loc[df['Status'] == 'Developed']
# finalAnswer = ck.loc[ck['Life expectancy '].max() == ck['Life expectancy ']]
# print(finalAnswer)


## Highest GDP in Developed Country over 15 years.


# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','GDP'])
# print(df)
# ck = df.loc[df['Status'] == 'Developed']
# finalAnswer = ck.loc[ck['GDP'].max() == ck['GDP']]
# print(finalAnswer)


# # Highest Adult Mortality in a particular country over 15 years.


# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','Adult Mortality'])
# print(df)
# finalAnswer= df.loc[df['Adult Mortality'].max() == df['Adult Mortality']]
# print(finalAnswer)


# # Lowest Adult Mortality in a particular country over 15 years.

# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','Adult Mortality'])
# print(df)
# finalAnswer= df.loc[df['Adult Mortality'].min() == df['Adult Mortality']]
# print(finalAnswer)


# # Country with highest Life Expectancy in 2015


# df= pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','Life expectancy '])
# print(df)
# ck= df.loc[df['Year'] == 2015]
# finalAnswer= ck.loc[ck['Life expectancy '].max() == ck['Life expectancy ']]
# print(finalAnswer)



# import pandas as pd
# import numpy as np

# df= pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv')
# print(df)
# ck= df.loc[df['Year'] == 2015]
# finalAnswer= ck.loc[ck['Life expectancy '].max() == ck['Life expectancy ']]
# print(finalAnswer)
