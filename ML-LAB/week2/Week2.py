#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


X = np.arange(10)


# In[3]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
plt.title('title')
plt.xlabel('x')
plt.ylabel('y')
ax.plot(X,X)


# In[4]:


fig1 = plt.figure()
ax1 = fig1.add_axes([0,0,1,1])
plt.title('title')
plt.xlabel('x')
plt.ylabel('y')
ax1.plot(X,X)
ax2 = fig1.add_axes([0.2, 0.5, 0.2, 0.2])
plt.title('title')
plt.xlabel('x')
plt.ylabel('y')
ax2.plot(X,X)


# In[5]:


df = pd.read_csv('./company_sales_data.csv')


# In[6]:


months = df['month_number']
total_profit = df['total_profit']


# In[7]:


plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.plot(months, total_profit)


# In[8]:


plt.plot(months.index, total_profit.values,
         linestyle='dotted', color='red', marker='o', markersize=8, markerfacecolor='red', linewidth=3, label='Total Units')
profits = df['total_profit'].sum()
print(f"Total Profit of the month is : {profits}")
plt.xlabel('Month Number')
plt.ylabel('Total Units')
plt.title('Total Units per Month')
 
 
plt.legend(loc='lower right')
 
plt.show()


# In[9]:


plt.figure(figsize=(10, 6))
for product in df.columns[1:-2]:  # Iterate over all product columns
    plt.plot(df['month_number'], df[product], label=product)
 
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Product Sales Over Time')
plt.legend()
plt.grid(True)
plt.show()


# In[10]:


last_year_sales = df.iloc[1:-2].sum()
plt.figure(figsize=(8, 8))
plt.pie(last_year_sales[1:-2].values, labels=last_year_sales[1:-2].index, autopct='%1.1f%%', startangle=90)
plt.title('Total Sales by Product (Last Year)')
plt.show()
