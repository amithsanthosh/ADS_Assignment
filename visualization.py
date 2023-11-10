import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\amith s\Downloads\archive\shopping_trends.csv")
df_sales = pd.read_csv("vgsales.csv")
"""Plotting line graph using given data"""


global_sales_per_year = df_sales.groupby('Year')['Global_Sales'].sum()
EU_sales_per_year = df_sales.groupby('Year')['EU_Sales'].sum()

# Plotting the line graph
plt.figure(figsize=(10, 6))
plt.plot(global_sales_per_year.index, global_sales_per_year.values, marker='o', linestyle='-')
plt.plot(EU_sales_per_year.index, EU_sales_per_year.values, marker='o', linestyle='-')
#plt.xticks()
# print(df)
# Adding labels and title
plt.xlabel('Year', fontsize=14)
plt.ylabel('Sales (in millions)', fontsize=14)
plt.title('Global and EU Sales per Year', fontsize=16)
plt.grid(True)

# Setting x-axis ticks to display every year
plt.xticks(global_sales_per_year.index[::3])

# Adding a legend
plt.legend()

# Display the plot
plt.show()


payment_method_column = df['Payment Method']

print(payment_method_column)

"""Plotting piechart using given data"""
plt.figure(figsize = (22, 7))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#00FF00']


counts = df["Payment Method"].value_counts()
explode = (0, 0, 0, 0, 0.0, 0.06)

counts.plot(kind = 'pie', fontsize = 12, colors = colors, explode = explode, autopct = '%1.1f%%')
plt.xlabel('Size', weight = "bold", color = "#2F0F5D", fontsize = 14, labelpad = 20)
plt.axis('equal')
plt.legend(labels = counts.index, loc = "best")
plt.show()


"""Plotting histogram using given data"""
plt.figure(figsize = (22, 7))
plt.hist(df['Age'], bins = 20, edgecolor = 'k')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()