#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load the breast cancer dataset
cancer = load_breast_cancer()

# Question 0: How many features does the breast cancer dataset have?
def question_0():
    return cancer.data.shape[1]

# Question 1: Convert the dataset to a DataFrame
def question_1():
    df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
    df['target'] = cancer.target
    return df

# Question 2: Class distribution
def question_2():
    target_series = pd.Series(cancer.target).value_counts()
    target_series.index = ['benign', 'malignant']
    return target_series

# Question 3: Split the DataFrame into X and y
def question_3():
    df = question_1()
    X = df.iloc[:, :-1]
    y = df['target']
    return X, y

# Question 4: Split X and y into training and test sets
def question_4():
    X, y = question_3()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
    return X_train, X_test, y_train, y_test

# Question 5: Fit a k-nearest neighbors (knn) classifier
def question_5():
    X_train, X_test, y_train, y_test = question_4()
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)
    return knn

# Question 6: Predict the class label using the mean value for each feature
def question_6():
    df = question_1()
    knn = question_5()
    mean_values = df.mean()[:-1].values.reshape(1, -1)
    return knn.predict(mean_values)

# Question 7: Predict the class labels for the test set X_test
def question_7():
    X_train, X_test, y_train, y_test = question_4()
    knn = question_5()
    return knn.predict(X_test)

# Question 8: Find the score (mean accuracy) of your knn classifier
def question_8():
    X_train, X_test, y_train, y_test = question_4()
    knn = question_5()
    return knn.score(X_test, y_test)

# Testing the functions
print("Question 0:", question_0())
print("Question 1:", question_1().head())
print("Question 2:", question_2())
print("Question 3:", question_3())
print("Question 4:", question_4())
print("Question 5:", question_5())
print("Question 6:", question_6())
print("Question 7:", question_7())
print("Question 8:", question_8())


# In[ ]:




