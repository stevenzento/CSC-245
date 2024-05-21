#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the Titanic dataset
titanic_data = pd.read_csv('/mnt/data/titanic.csv')

# 1. Write a Pandas program to print a concise summary of the dataset (titanic.csv).
print("Concise summary of the Titanic dataset:")
print(titanic_data.info())

# 2. Write a Pandas program to extract the column labels, shape and data types of the dataset (titanic.csv).
print("\nColumn labels:")
print(titanic_data.columns)
print("\nShape of the dataset:")
print(titanic_data.shape)
print("\nData types of the dataset:")
print(titanic_data.dtypes)

# 3. Write a Pandas program to create a Pivot table with multiple indexes from the data set of titanic.csv.
pivot_table_multiple_indexes = pd.pivot_table(titanic_data, index=["Sex", "Pclass"], values="Survived", aggfunc='mean')
print("\nPivot table with multiple indexes:")
print(pivot_table_multiple_indexes)

# 4. Write a Pandas program to create a Pivot table and find survival rate by gender on various classes.
pivot_table_survival_by_gender_class = pd.pivot_table(titanic_data, index="Pclass", columns="Sex", values="Survived", aggfunc='mean')
print("\nSurvival rate by gender on various classes:")
print(pivot_table_survival_by_gender_class)

# 5. Write a Pandas program to create a Pivot table and find survival rate by gender.
pivot_table_survival_by_gender = pd.pivot_table(titanic_data, index="Sex", values="Survived", aggfunc='mean')
print("\nSurvival rate by gender:")
print(pivot_table_survival_by_gender)

# 6. Write a Pandas program to create a Pivot table and find survival rate by gender, age wise of various classes.
titanic_data['Age'] = pd.cut(titanic_data['Age'], bins=[0, 10, 30, 60, 80])
pivot_table_survival_by_gender_age_class = pd.pivot_table(titanic_data, index=["Pclass", "Age"], columns="Sex", values="Survived", aggfunc='mean')
print("\nSurvival rate by gender, age wise of various classes:")
print(pivot_table_survival_by_gender_age_class)

# 7. Write a Pandas program to partition each of the passengers into four categories based on their age.
# Note: Age categories (0, 10), (10, 30), (30, 60), (60, 80)
titanic_data['Age_Category'] = pd.cut(titanic_data['Age'], bins=[0, 10, 30, 60, 80], labels=["0-10", "10-30", "30-60", "60-80"])
print("\nPassengers partitioned into four age categories:")
print(titanic_data[['Age', 'Age_Category']].head())

# 8. Write a Pandas program to create a Pivot table and count survival by gender, categories wise age of various classes.
pivot_table_count_survival_gender_age_class = pd.pivot_table(titanic_data, index=["Pclass", "Age_Category"], columns="Sex", values="Survived", aggfunc='count')
print("\nCount survival by gender, categories wise age of various classes:")
print(pivot_table_count_survival_gender_age_class)

# 9. Write a Pandas program to create a Pivot table and find survival rate by gender, age of the different categories of various classes.
pivot_table_survival_rate_gender_age_class = pd.pivot_table(titanic_data, index=["Pclass", "Age_Category"], columns="Sex", values="Survived", aggfunc='mean')
print("\nSurvival rate by gender, age of the different categories of various classes:")
print(pivot_table_survival_rate_gender_age_class)

# 10. Write a Pandas program to create a Pivot table and find survival rate by gender, age of the different categories of various classes. 
# Add the fare as a dimension of columns and partition fare column into 2 categories based on the values present in fare columns
titanic_data['Fare_Category'] = pd.cut(titanic_data['Fare'], bins=[0, titanic_data['Fare'].median(), titanic_data['Fare'].max()], labels=["Low Fare", "High Fare"])
pivot_table_survival_rate_gender_age_class_fare = pd.pivot_table(titanic_data, index=["Pclass", "Age_Category"], columns=["Sex", "Fare_Category"], values="Survived", aggfunc='mean')
print("\nSurvival rate by gender, age of the different categories of various classes with fare as a dimension:")
print(pivot_table_survival_rate_gender_age_class_fare)


# In[ ]:




