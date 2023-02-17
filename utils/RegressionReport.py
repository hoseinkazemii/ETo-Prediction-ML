import os
import numpy as np
import pandas as pd
import pprint
import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error as MAE
from sklearn.metrics import mean_squared_error as MSE


# def MAPE(y_true, y_pred):
# 	y_true = np.array(y_true)
# 	y_pred = np.array(y_pred)
	
# 	if np.all(y_true):
# 		return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
# 	else:
# 		return np.nan

def R2(y_true, y_pred):
	return np.corrcoef(y_true, y_pred)[0][1]**2

def CorCoef(y_true, y_pred):
	return np.corrcoef(y_true, y_pred)[0][1]

def evaluate_regression(*args, **params):
	'''Report regression results
	
	*args should be lists of [label, x, y_true, y_pred]
	x MUST be pandas dataframe
	y_true and y_pred must be list or 1d numpy array
	'''

	report_directory = params.get('report_directory')
	model_name = params.get('model_name')
	logger = params.get('logger')


	for ls in args:
		label, x, y_true, y_pred = ls
		
		# Saving into csv file
		if (not model_name == "DNN") and (not model_name == "LSTM"):
			report = pd.DataFrame()
			report['Actual'] = y_true
			report['Predicted'] = y_pred
			report['Error'] = report['Actual'] - report['Predicted']

			report.to_csv(report_directory + "/" + f'{model_name}-{label}.csv')

			corcoef_ = CorCoef(y_true, y_pred)
			r2_ = R2(y_true, y_pred)
			mse_ = MSE(y_true, y_pred)
			mae_ = MAE(y_true, y_pred)
			# mape_ = MAPE(y_true, list(y_pred))


		elif model_name == "DNN":
			corcoef_ = CorCoef(y_true, np.ravel(y_pred))
			r2_ = R2(y_true, np.ravel(y_pred))
			mse_ = MSE(y_true, np.ravel(y_pred))
			mae_ = MAE(y_true, np.ravel(y_pred))
			# mape_ = MAPE(y_true, list(np.ravel(y_pred)))
		
		elif model_name == "LSTM":
			y_pred = np.reshape(y_pred, (y_pred.shape[0],))
			corcoef_ = CorCoef(y_true, y_pred)
			r2_ = R2(y_true, y_pred)
			mse_ = MSE(y_true, y_pred)
			mae_ = MAE(y_true, y_pred)
			# mape_ = MAPE(y_true, list(y_pred))

		
		# Reporting the quantitative results
		report_str = f"{label}, CorCoef= {corcoef_:.4f}, "\
						f"R2= {r2_:.4f}, RMSE={mse_**0.5:.4f}, "\
							f"MSE={mse_:.4f}, MAE={mae_:.4f}, "
		
		logger.info(report_str)
		print(report_str)