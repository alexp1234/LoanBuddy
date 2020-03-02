import pandas as pd
import numpy as np
names=['loan_amnt', 'term', 'int_rate', 'emp_length', 'home_ownership', 'annual_inc', 'verification_status', 'purpose', 'dti', 'delinq_2yrs', 'fico_range_low', 'inq_last_6mths', 'mths_since_last_delinq', 'mths_since_last_record', 'open_acc', 'pub_rec', 'revol_bal', 'revol_util', 'total_acc', 'collections_12_mths_ex_med', 'mths_since_last_major_derog', 'loan_status' ]
dataset = pd.read_csv("data/DTrain2.csv", names=names)



dataset = dataset.fillna(0)
dataset = dataset.iloc[1:]

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 21].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

error = []

for i in range(1,151):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error.append(np.mean(pred_i != y_test))
    # Graphing the Error compared to number of neighbors

import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.plot(range(1,151), error, color='red', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=10)
plt.title('Error rate K value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')


# input loan_amount, loan_length, interst_rate, income_verified, gross_income,
# debt_to_income, length_employment, open_cl, total_cl, credit_score, age_of_credit,
# revolving_balance, revolving_utilization, total_limit
# Prediction data goes below
test = np.array([])
test = test.reshape(1,-1)

#Predicting new data based on results 
classifier.predict(test)
print(classifier.predict(test))


