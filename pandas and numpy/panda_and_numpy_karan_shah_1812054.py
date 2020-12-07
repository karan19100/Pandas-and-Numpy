import pandas as pd
import numpy as np

df= pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','Life expectancy '])
print(df)
ck= df.loc[df['Year'] == 2015]
finalAnswer= ck.loc[ck['Life expectancy '].max() == ck['Life expectancy ']]
print(finalAnswer)








# task 1 final

# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv')
# print(df)
# df = df.loc[df['Country'] == 'Afghanistan']
# country = df['Country'][1]
# life_expectancy = df['Life expectancy '].mean()
# final_ans = [country, life_expectancy]
# print(final_ans)


# task 2 final 

# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','Life expectancy '])
# print(df)
# ck = df.loc[df['Status'] == 'Developing']
# finalAnswer = ck.loc[ck['Life expectancy '].max() == ck['Life expectancy ']]
# print(finalAnswer)


# task 3 final     

# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','Life expectancy '])
# print(df)
# ck = df.loc[df['Status'] == 'Developed']
# print(ck)
# finalAnswer = ck.loc[ck['Life expectancy '].max() == ck['Life expectancy ']]
# print(finalAnswer)


# task 4 final

# df = pd.read_csv(r'C:\Users\USer\Desktop\EXP5\Life Expectancy Data.csv',usecols = ['Country','Year','Status','Adult Mortality'])
# print(df)
# finalAnswer= df.loc[df['Adult Mortality'].max() == df['Adult Mortality']]
# print(finalAnswer)

