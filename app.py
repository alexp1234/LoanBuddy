from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle
import numpy as np
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
	names=['loan_amnt', 'term', 'int_rate', 'emp_length', 'home_ownership', 'annual_inc', 'verification_status', 'purpose', 'dti', 'delinq_2yrs', 'fico_range_low', 'inq_last_6mths', 'mths_since_last_delinq', 'mths_since_last_record', 'open_acc', 'pub_rec', 'revol_bal', 'revol_util', 'total_acc', 'collections_12_mths_ex_med', 'mths_since_last_major_derog', 'loan_status' ]
	dataset=pd.read_csv("data/DTrain.csv", names=names)
	dataset = dataset.fillna(0)
	dataset = dataset.iloc[1:]
	X = dataset.iloc[:, :-1].values
	y = dataset.iloc[:, 21].values

	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
	from sklearn.preprocessing import StandardScaler
	scaler = StandardScaler()
	scaler.fit(X_train)
	X_train = scaler.transform(X_train)
	X_test = scaler.transform(X_test)
	from sklearn.neighbors import KNeighborsClassifier
	classifier = KNeighborsClassifier(n_neighbors=183)
	classifier.fit(X_train, y_train)
	y_pred = classifier.predict(X_test)

	if request.method == 'POST':
		loan_amnt = request.form['loan_amnt']
		term = request.form['term']
		int_rate = request.form['int_rate']
		emp_length = request.form['emp_length']
		home_ownership = request.form['home_ownership']
		annual_inc = request.form['annual_inc']
		verification_status = request.form['verification_status']
		purpose = request.form['purpose']
		dti = request.form['dti']
		delinq_2yrs = request.form['delinq_2yrs']
		fico_range_low = request.form['fico_range_low']
		inq_last_6mths = request.form['inq_last_6mths']
		mths_since_last_delinq = request.form['mths_since_last_delinq']
		mths_since_last_record = request.form['mths_since_last_record']
		open_acc = request.form['open_acc']
		pub_rec = request.form['pub_rec']
		revol_bal = request.form['revol_bal']
		revol_util = request.form['revol_util']
		total_acc = request.form['total_acc']
		collections_12_mths_ex_med = request.form['collections_12_mths_ex_med']
		mths_since_last_major_derog = request.form['mths_since_last_major_derog']

		data = np.array([loan_amnt, term, int_rate, emp_length, home_ownership, annual_inc, verification_status, purpose, dti, delinq_2yrs, fico_range_low, inq_last_6mths, mths_since_last_delinq, mths_since_last_record, open_acc, pub_rec, revol_bal, revol_util, total_acc, collections_12_mths_ex_med, mths_since_last_major_derog])
		data = data.reshape(1,-1)
		my_prediction = classifier.predict(data)
	return render_template('result.html', prediction= my_prediction)








	if __name__ == '__main__':
		app.run(debug=True)