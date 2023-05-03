import os
import numpy as np
import pandas as pd
import pprint
import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error as MAE
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import r2_score


def R2(y_test, y_pred_test):
	# return r2_score(y_test, y_pred_test)
	return np.corrcoef(y_test, y_pred_test)[0][1]**2

def CorCoef(y_test, y_pred_test):
	return np.corrcoef(y_test, y_pred_test)[0][1]

def evaluate_regression(label, y_test, y_pred_test, **params):
	'''Report regression results
	
	*args should be lists of [label, y_test, y_pred_test]
	y_test and y_pred_test must be list or 1d numpy array
	'''

	report_directory = params.get('report_directory')
	model_name = params.get('model_name')
	logger = params.get('logger')
	
	# Saving into csv file
	report = pd.DataFrame()
	report['Actual'] = y_test
	report['Predicted'] = y_pred_test
	report['Error'] = report['Actual'] - report['Predicted']

	report.to_csv(report_directory + "/" + f'{model_name}-{label}.csv')
	
	corcoef_ = CorCoef(y_test, y_pred_test)
	r2_ = R2(y_test, y_pred_test)
	mse_ = MSE(y_test, y_pred_test)
	mae_ = MAE(y_test, y_pred_test)


	# Reporting the quantitative results
	report_str = f"{label}, CorCoef= {corcoef_:.4f}, "\
					f"R2= {r2_:.4f}, RMSE={mse_**0.5:.4f}, "\
						f"MSE={mse_:.4f}, MAE={mae_:.4f}, "
	
	logger.info(report_str)
	print(report_str)