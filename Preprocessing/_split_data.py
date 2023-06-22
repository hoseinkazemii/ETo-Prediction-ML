import pandas as pd
import numpy as np

# from ._replace_unusual_Rs import replace_unusual_Rs


def split_data(df, **params):
	#For preparing the dataset for the first run change the arguements to (df, **params). Also, change it in "PreprocessData.py"
	# Also, comment this line: df = pd.read_csv(data_path_daily_for_run+'final_dataset.csv') or df = pd.read_csv(data_path_hourly_for_run+'final_dataset.csv')
	
	verbose = params.get("verbose")
	train_test_strategy = params.get("train_test_strategy")
	training_stations = params.get("training_stations")
	test_stations = params.get("test_stations")
	years_for_test = params.get("years_for_test")
	outlier_margin = params.get("outlier_margin")
	SolRad_daily = params.get("SolRad_daily")
	# Rso_included = params.get("Rso_included")

	if verbose:
		print("Splitting data...")

	#training dataset
	if train_test_strategy == "station_based":
		df_train = df[df['StnId'].isin(training_stations)]

	# elif train_test_strategy == "yearly":
	# 	df_train = df[df['Year'] <= df.Year.max() - years_for_test]


	#dropping outliers
	df_train = df_train[df_train['ETo_sum_day'] <= outlier_margin]

	if train_test_strategy == "station_based":
		df_test = df[df['StnId'].isin(test_stations)]

	# elif train_test_strategy == "yearly":
	# 	df_test = df[df['Year'] > df.Year.max() - years_for_test]


	if SolRad_daily:

		# if Rso_included:
			# df_train = replace_unusual_Rs(df_train, **params)
			# X_train = df_train.drop(columns=['ETo_sum_day','StnId','Jul'], axis=1)
			# X_test = df_test.drop(columns=['ETo_sum_day','StnId','Jul'], axis=1)

		# else:
		X_train = df_train.drop(columns=['ETo_sum_day','StnId','Jul'], axis=1)
		X_test = df_test.drop(columns=['ETo_sum_day','StnId','Jul'], axis=1)

	else:
		X_train = df_train.drop(columns=['Date','StnId','ETo_sum_day','Jul'], axis=1)
		X_test = df_test.drop(columns=['Date','StnId','ETo_sum_day','Jul'], axis=1)


	y_train = df_train['ETo_sum_day']
	y_test = df_test['ETo_sum_day']

	return X_train, X_test, y_train, y_test