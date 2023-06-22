import numpy as np
import joblib

from utils import evaluate_regression


def train_model(X_train, X_test, y_train, y_test,**params):

	log = params.get("log")
	model = params.get('model')
	verbose = params.get('verbose')
	model_name = params.get("model_name")
	report_directory = params.get("report_directory")
	warm_up = params.get("warm_up")
	model_directory = params.get("model_directory")

	if verbose:
		if warm_up:
			print("Loading the pretrained model...")
		
		elif not warm_up:
			print ("Trying to fit to the data...")


	if not warm_up:
		model.fit(X_train, y_train)
		joblib.dump(model, model_directory + f"{model_name}/{model_name}.joblib")

	y_pred_train = model.predict(X_train)
	y_pred_test = model.predict(X_test)

	evaluate_regression(
		# [f'OnTrain', X_train, y_train, y_pred_train],
		[f'OnTest', X_test, y_test, y_pred_test],
		model = model,
		model_name = model_name,
		logger = log,
		report_directory = report_directory)