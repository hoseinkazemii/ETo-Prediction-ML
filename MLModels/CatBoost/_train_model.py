from utils import evaluate_regression

import numpy as np


def train_model(**params):
	
	log = params.get("log")
	model = params.get('model')
	verbose = params.get('verbose')
	model_name = params.get("model_name")
	report_directory = params.get("report_directory")
	
	X_train, X_test, y_train, y_test = \
		params.get("X_train"),\
		params.get("X_test"), \
		params.get("y_train"), \
		params.get("y_test")


	if verbose:
		print ("Trying to fit to the data...")

	model.fit(X_train, y_train, plot=True)

	y_pred_train = model.predict(X_train)
	y_pred_test = model.predict(X_test)

	mean_squared_error = evaluate_regression([f'OnTrain', X_train, y_train, y_pred_train],
											 [f'OnTest', X_test, y_test, y_pred_test],
											 model = model,
											 model_name = model_name,
											 logger = log,
											 report_directory = report_directory)

	return mean_squared_error