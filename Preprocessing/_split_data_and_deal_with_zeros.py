import pandas as pd
import numpy as np

from ._cyclic_datetime_julian_date import _cyclic_datetime_julian_date


def split_data_and_deal_with_zeros(**params):
	#For preparing the dataset for the first run change the arguements to (df, **params). Also, change it in "PreprocessData.py"
	# Also, comment this line: df = pd.read_csv(data_path_daily_for_run+'final_dataset.csv') or df = pd.read_csv(data_path_hourly_for_run+'final_dataset.csv')
	
	verbose = params.get("verbose")
	train_test_strategy = params.get("train_test_strategy")
	training_stations = params.get("training_stations")
	test_stations = params.get("test_stations")
	years_for_test = params.get("years_for_test")
	strategy_for_zeros = params.get("strategy_for_zeros")
	dealing_with_zeros_whole_dataset = params.get("dealing_with_zeros_whole_dataset")
	how_to_compute_daily_avg = params.get("how_to_compute_daily_avg")
	outlier_quantile = params.get("outlier_quantile")
	dropping_cols_strategy = params.get("dropping_cols_strategy")
	correlation_method = params.get("correlation_method")
	SolRad_daily = params.get("SolRad_daily")
	data_path_hourly = params.get("data_path_hourly")
	data_path_daily = params.get("data_path_daily")
	data_path_hourly_for_run = params.get("data_path_hourly_for_run")
	data_path_daily_for_run = params.get("data_path_daily_for_run")

	if verbose:
		if strategy_for_zeros == 'row_mean':
			print("splitting data, filling zero values for SolRad in the train set with mean...")
		elif strategy_for_zeros == 'drop_column':
			print("splitting data, dropping columns with at least one zero for hourly SolRad...")


	# df.drop(columns=['Day','Month'], axis=1).to_csv('./FeatureSelection/final_dataset_for_training.csv', index=False)
	# raise ValueError('Created final_dataset_for_training.csv For the feature selction methods, including CatBoost feature\
	# 	importance and different correlation methods')



	if SolRad_daily:
		df = pd.read_csv(data_path_daily_for_run+'final_dataset.csv')
		df['SolRad_daily_avg'] = df.iloc[:,1:25].sum(axis=1)/24
		df = df[['StnId','SolRad_daily_avg','ETo_sum_day','Jul','Day','Month','Year']]
		df = _cyclic_datetime_julian_date(df, 'Jul')


	elif not SolRad_daily:
		df = pd.read_csv(data_path_hourly_for_run+'final_dataset.csv')

		if dealing_with_zeros_whole_dataset:

			if how_to_compute_daily_avg == 'without_zeros':
				df[df.drop(columns=['StnId','ETo_sum_day'], axis=1) == 0] = np.nan
				df['SolRad_daily_avg'] = df.drop(columns=['StnId','ETo_sum_day'], axis=1).mean(axis=1)
			
			elif how_to_compute_daily_avg == 'with_zeros':
				df['SolRad_daily_avg'] = df.iloc[:, 1:25].mean(axis=1)
				df[df.drop(columns=['StnId','ETo_sum_day'], axis=1) == 0] = np.nan


			for col in df.columns:		
				df[col].fillna(df['SolRad_daily_avg'], inplace=True)


			df.drop(columns=['SolRad_daily_avg'], axis=1, inplace=True)


			if dropping_cols_strategy=='feature_importance':

		  		#Keep Features with highest Feature Importance:
		  		df.drop(columns=['100','200','300','400','500','1100',
					'1200','1400','1500','1600','1700','1800',
					'1900','2000','2100','2200','2300','2400'],
					axis=1, inplace=True)	
				

			elif dropping_cols_strategy=='correlation':

	  			#Keep Features with highest correlation with ETo_sum_day
				if correlation_method == 'pearson_':
					df.drop(columns=['100','200','300','400','500','600',
			                 '1300','1400','1500','1600','1700','1800',
			                 '1900','2000','2100','2200','2300','2400'],
			                  axis=1, inplace=True)

				elif correlation_method == 'mutual_info':
					df.drop(columns=['100','200','300','400','500',
			                 '600','700','1400','1500','1600','1700','1800',
			                 '1900','2000','2100','2200','2300','2400'],
			                  axis=1, inplace=True)


				elif correlation_method == 'spearman_':
					# This is same as 'pearson_' correlation
					df.drop(columns=['100','200','300','400','500','600',
			                 '1300','1400','1500','1600','1700','1800',
			                 '1900','2000','2100','2200','2300','2400'],
			                  axis=1, inplace=True)	



	#training dataset
	if train_test_strategy == "yearly":
		df_train = df[df['Year'] <= df.Year.max() - years_for_test]

	elif train_test_strategy == "station_based":
		df_train = df[df['StnId'].isin(training_stations)]
		


	#dropping outliers
	df_train = df_train[df_train['ETo_sum_day'] <= df_train['ETo_sum_day'].quantile(outlier_quantile)]


	if (strategy_for_zeros == 'row_mean') and (dealing_with_zeros_whole_dataset == False):

		if how_to_compute_daily_avg == 'without_zeros':
			df_train[df_train.drop(columns=['StnId','ETo_sum_day'], axis=1) == 0] = np.nan
			df_train['SolRad_daily_avg'] = df_train.drop(columns=['StnId','ETo_sum_day','Day','Month','Year'], axis=1).mean(axis=1) 

		elif how_to_compute_daily_avg == 'with_zeros':
			df_train['SolRad_daily_avg'] = df_train.iloc[:, 1:25].mean(axis=1)
			df_train[df_train.drop(columns=['StnId','ETo_sum_day'], axis=1) == 0] = np.nan


		for col in df_train.columns:		
			df_train[col].fillna(df_train['SolRad_daily_avg'], inplace=True)

		df_train.drop(columns=['SolRad_daily_avg'], axis=1, inplace=True)


	elif strategy_for_zeros == 'drop_column':
		df_train[df_train.drop(columns=['ETo_sum_day'], axis=1) == 0] = np.nan
		df_train = df_train.dropna(how='all', axis=1)


	if train_test_strategy == "yearly":
		df_test = df[df['Year'] > df.Year.max() - years_for_test]

	elif train_test_strategy == "station_based":
		df_test = df[df['StnId'].isin(test_stations)]
		# df_test = df[~df['StnId'].isin(training_stations)]


	if SolRad_daily:	
		X_train = df_train.drop(columns=['ETo_sum_day','Day','Month','Year','Jul'], axis=1)
		X_test = df_test.drop(columns=['ETo_sum_day','Day','Month','Year','Jul'], axis=1)

	else:
		X_train = df_train.drop(columns=['Date','StnId','ETo_sum_day'], axis=1)
		X_test = df_test.drop(columns=['Date','StnId','ETo_sum_day'], axis=1)

	y_train = df_train['ETo_sum_day']
	y_test = df_test['ETo_sum_day']

	return X_train, X_test, y_train, y_test