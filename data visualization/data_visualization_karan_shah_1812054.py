import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv(r'C:\Users\USer\Desktop\EXP6\temporal.csv')
print(df.head(10))
describe_data=df.describe()
print(describe_data)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

format_dict = {'data science':'${0:,.2f}', 'Mes':'{:%m-%Y}', 'machine learning':'{:.2%}'}
df['Mes'] = pd.to_datetime(df['Mes'])   # Month column is of datetime format  
df.head().style.format(format_dict)     # i am applying the style for visualization

# task 1 popularity of AI in terms of date 

plt.plot(df['Mes'], df['data science'], label='data science')
plt.plot(df['Mes'], df['machine learning'], label='machine learning')
plt.plot(df['Mes'], df['deep learning'], label='deep learning')
plt.xlabel('Date')
plt.ylabel('Popularity')
plt.title('Popularity of AI terms by date')
plt.grid(True)
plt.legend()
plt.show()

# task 2 scatter plot ( create multiple graphics in one image )

fig, axes = plt.subplots(1, 2, sharey=True, figsize=(8, 4))
sns.scatterplot(x="Mes", y="deep learning", hue="categorical", data=df, ax=axes[0])
axes[0].set_title('Deep Learning')
sns.scatterplot(x="Mes", y="machine learning", hue="categorical", data=df, ax=axes[1])
axes[1].set_title('Machine Learning')
plt.show()

# task 3  Violin Plot 

sns.catplot(x='categorical', y='data science', kind='violin', data=df)
plt.show()

# task 4  heatmap ( it shows all the correlation bwtween variable and dataset )

sns.heatmap(df.corr(), annot=True, fmt='.2f')
plt.show()

# task 5 pair plot 

sns.pairplot(df)
plt.show()

# task 6 joint plot 

sns.jointplot(x='data science', y='machine learning', data=df)
plt.show()



