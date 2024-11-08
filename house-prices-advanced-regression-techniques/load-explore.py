##Practice Skills
##Creative feature engineering 
##Advanced regression techniques like random forest and gradient boosting


import pandas as pd

#load train dataset
train = pd.read_csv("train.csv")

#Understanding the dataset
print(train.head(10))
print(train.dtypes)
print(train.info())

#Check for missing values