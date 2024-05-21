#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data
data = pd.read_csv('/mnt/data/company_sales_data.csv')

# Exercise 1: Read Total profit of all months and show it using a line plot
plt.figure(figsize=(10, 6))
plt.plot(data['month_number'], data['total_profit'])
plt.xlabel('Month Number')
plt.ylabel('Total profit')
plt.title('Company Profit per Month')
plt.show()

# Exercise 2: Get total profit of all months and show line plot with the following Style properties
plt.figure(figsize=(10, 6))
plt.plot(data['month_number'], data['total_profit'], color='red', linestyle='dotted', marker='o', linewidth=3, markerfacecolor='red')
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.title('Company Profit per Month with Style')
plt.legend(['Profit'], loc='lower right')
plt.show()

# Exercise 3: Read all product sales data and show it using a multiline plot
plt.figure(figsize=(10, 6))
for column in data.columns[1:-2]:  # excluding month_number and total_profit
    plt.plot(data['month_number'], data[column], label=column)
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Sales Data for Each Product')
plt.legend()
plt.show()

# Exercise 4: Read toothpaste sales data of each month and show it using a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['month_number'], data['toothpaste'])
plt.xlabel('Month Number')
plt.ylabel('Toothpaste units sold')
plt.title('Toothpaste Sales Data')
plt.grid(True, linestyle='--')
plt.show()

# Exercise 5: Read face cream and facewash product sales data and show it using the bar chart
plt.figure(figsize=(10, 6))
bar_width = 0.3
plt.bar(data['month_number'] - bar_width/2, data['facecream'], width=bar_width, label='Face Cream')
plt.bar(data['month_number'] + bar_width/2, data['facewash'], width=bar_width, label='Face Wash')
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Face Cream and Face Wash Sales Data')
plt.legend()
plt.show()

# Exercise 6: Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
plt.figure(figsize=(10, 6))
plt.bar(data['month_number'], data['bathingsoap'], color='blue')
plt.xlabel('Month Number')
plt.ylabel('Bathing Soap units sold')
plt.title('Bathing Soap Sales Data')
plt.savefig('/mnt/data/bathing_soap_sales_data.png')
plt.show()

# Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges
plt.figure(figsize=(10, 6))
plt.hist(data['total_profit'], bins=10, color='blue', edgecolor='black')
plt.xlabel('Profit Range')
plt.ylabel('Frequency')
plt.title('Profit Distribution')
plt.show()

# Exercise 8: Calculate total sale data for last year for each product and show it using a Pie chart
total_sales = data.drop(columns=['month_number', 'total_profit']).sum()
plt.figure(figsize=(10, 6))
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Total Sales Distribution')
plt.show()

# Exercise 9: Read Bathing soap and facewash of all months and display it using the Subplot
fig, ax = plt.subplots(2, 1, figsize=(10, 12))
ax[0].plot(data['month_number'], data['bathingsoap'], marker='o')
ax[0].set_title('Bathing Soap Sales Data')
ax[1].plot(data['month_number'], data['facewash'], marker='o')
ax[1].set_title('Facewash Sales Data')
for a in ax:
    a.set_xlabel('Month Number')
    a.set_ylabel('Units Sold')
    a.grid(True)
plt.tight_layout()
plt.show()

# Exercise 10: Read all product sales data and show it using the stack plot
plt.figure(figsize=(10, 6))
plt.stackplot(data['month_number'], data.iloc[:, 1:-2].T, labels=data.columns[1:-2])
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Sales Data Stack Plot')
plt.legend(loc='upper left')
plt.show()


# In[ ]:




