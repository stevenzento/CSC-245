#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# 1. Join the two given dataframes along rows and assign all data
student_data1 = pd.DataFrame({
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
    'marks': [200, 210, 190, 222, 199]
})

student_data2 = pd.DataFrame({
    'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
    'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
    'marks': [201, 200, 198, 219, 201]
})

result1 = pd.concat([student_data1, student_data2], ignore_index=True)
print("Join the two given dataframes along rows:")
print(result1)

# 2. Join the two given dataframes along columns and assign all data
result2 = pd.concat([student_data1, student_data2], axis=1)
print("\nJoin the two given dataframes along columns:")
print(result2)

# 3. Append rows to an existing DataFrame and display the combined data
new_row = pd.DataFrame([{'student_id': 'S6', 'name': 'Scarlette Fisher', 'marks': 205}])
student_data1 = pd.concat([student_data1, new_row], ignore_index=True)
print("\nAppend rows to an existing DataFrame:")
print(student_data1)

# 4. Append a list of dictionaries or series to an existing DataFrame and display the combined data
new_data = [{'student_id': 'S6', 'name': 'Scarlette Fisher', 'marks': 205}]
new_data_df = pd.DataFrame(new_data)
student_data1 = pd.concat([student_data1, new_data_df], ignore_index=True)
print("\nAppend a list of dictionaries to an existing DataFrame:")
print(student_data1)

# 5. Join the two given dataframes along rows and merge with another dataframe along the common column id
exam_data = pd.DataFrame({
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
    'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]
})

combined_data = pd.concat([student_data1, student_data2], ignore_index=True)
merged_result = pd.merge(combined_data, exam_data, on='student_id', how='inner')
print("\nJoin two dataframes along rows and merge with another dataframe:")
print(merged_result)

# 6. Join the two dataframes using the common column of both dataframes
common_join = pd.merge(student_data1, student_data2, on='student_id')
print("\nJoin the two dataframes using the common column:")
print(common_join)

# 7. Join the two dataframes with matching records from both sides where available
matching_join = pd.merge(student_data1, student_data2, on='student_id', how='outer')
print("\nJoin the two dataframes with matching records from both sides where available:")
print(matching_join)

# 8. Join (left join) the two dataframes using keys from left dataframe only
data1 = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'P': ['P0', 'P1', 'P2', 'P3'],
    'Q': ['Q0', 'Q1', 'Q2', 'Q3']
})

data2 = pd.DataFrame({
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
    'R': ['R0', 'R1', 'R2', 'R3'],
    'S': ['S0', 'S1', 'S2', 'S3']
})

left_join = pd.merge(data1, data2, on=['key1', 'key2'], how='left')
print("\nLeft join using keys from left dataframe only:")
print(left_join)

# 9. Join two dataframes using keys from right dataframe only
right_join = pd.merge(data1, data2, on=['key1', 'key2'], how='right')
print("\nRight join using keys from right dataframe only:")
print(right_join)

# 10. Merge two given datasets using multiple join keys
multi_key_join = pd.merge(data1, data2, on=['key1', 'key2'])
print("\nMerge two given datasets using multiple join keys:")
print(multi_key_join)

# 11. Create a new DataFrame based on existing series, using specified argument and override the existing columns names
new_series = pd.Series([100, 200, 300], name='marks')
df_from_series = new_series.to_frame().reset_index().rename(columns={'index': 'student_id'})
print("\nCreate a new DataFrame based on existing series:")
print(df_from_series)

# 12. Create a combination from two dataframes where a column id combination appears more than once in both dataframes
combination_df = pd.merge(data1, data2, on=['key1', 'key2'], how='outer', indicator=True)
print("\nCreate a combination from two dataframes where a column id combination appears more than once in both dataframes:")
print(combination_df[combination_df['_merge'] == 'both'])

# 13. Combine the columns of two potentially differently-indexed DataFrames into a single result DataFrame
data1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])

data2 = pd.DataFrame({
    'C': ['C0', 'C2', 'C3'],
    'D': ['D0', 'D2', 'D3']
}, index=['K0', 'K2', 'K3'])

combined_df = pd.concat([data1, data2], axis=1)
print("\nCombine the columns of two differently-indexed DataFrames:")
print(combined_df)

# 14. Merge two given dataframes with different columns
different_columns_merge = pd.merge(data1, data2, left_index=True, right_index=True, how='outer')
print("\nMerge two given dataframes with different columns:")
print(different_columns_merge)

# 15. Combine two DataFrame objects by filling null values in one DataFrame with non-null values from other DataFrame
df1 = pd.DataFrame({'A': [None, 0, None], 'B': [3, 4, 5]})
df2 = pd.DataFrame({'A': [1, 1, 3], 'B': [3, None, 3]})

filled_df = df1.combine_first(df2)
print("\nCombine two DataFrame objects by filling null values:")
print(filled_df)


# In[ ]:




