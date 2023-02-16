import numpy as np
from sklearn.impute import SimpleImputer


def split_data_and_deal_with_zeros(df, **params):
	verbose = params.get("verbose")
	years_for_test = params.get("years_for_test")
	strategy_for_zeros = params.get("strategy_for_zeros")
	dealing_with_zeros_whole_dataset = params.get("dealing_with_zeros_whole_dataset")
	how_to_compute_daily_avg = params.get("how_to_compute_daily_avg")
	outlier_quantile = params.get("outlier_quantile")
	correlation_method = params.get("correlation_method")

	if verbose:
		if strategy_for_zeros == 'row_mean':
			print("splitting data, filling zero values for SolRad in the train set with mean...")
		elif strategy_for_zeros == 'drop_column':
			print("splitting data, dropping columns with at least one zero for hourly SolRad...")


	# df.drop(columns=['Day','Month','Year'], axis=1).to_csv('./EDA/final_dataset_for_training.csv', index=False)
	# raise ValueError


	if dealing_with_zeros_whole_dataset:

		if how_to_compute_daily_avg == 'without_zeros':
			df[df.drop(columns=['ETo_sum_day'], axis=1) == 0] = np.nan
			df['SolRad_daily_avg'] = df.drop(columns=['ETo_sum_day','Day','Month','Year'], axis=1).mean(axis=1) #Need to be discussed: We can also do this for the whole dataset 
		
		elif how_to_compute_daily_avg == 'with_zeros':
			df['SolRad_daily_avg'] = df.iloc[:, 0:24].mean(axis=1)
			df[df.drop(columns=['ETo_sum_day'], axis=1) == 0] = np.nan

		for col in df.columns:		
			df[col].fillna(df['SolRad_daily_avg'], inplace=True)


		df.drop(columns=['SolRad_daily_avg'], axis=1, inplace=True)


		# #Drop VIF > 10:
		# df.drop(columns=['100.0','200.0','300.0','400.0','500.0',
  #                '800.0','900.0','1000.0','1100.0',
  #                '1200.0','1300.0','1400.0','1500.0','1600.0',
  #                '1700.0','2100.0','2200.0','2300.0','2400.0'], axis=1, inplace=True)


		#Keep Features with the highest correlations:
		if correlation_method == 'pearson_':
			df.drop(columns=['100.0','200.0','300.0','400.0','500.0',
	                 '600.0','700.0','1200.0',
	                 '1300.0','1400.0','1700.0','1800.0',
	                 '1900.0','2000.0','2100.0','2200.0','2300.0','2400.0'],
	                  axis=1, inplace=True)

		elif correlation_method == 'mutual_info':
			df.drop(columns=['100.0','200.0','300.0','400.0','500.0',
	                 '600.0','700.0',
	                 '1400.0','1500.0','1600.0','1700.0','1800.0',
	                 '1900.0','2000.0','2100.0','2200.0','2300.0','2400.0'],
	                  axis=1, inplace=True)			


	df_train = df[df['Year'] <= df.Year.max() - years_for_test]
	df_train = df_train[df_train['ETo_sum_day'] <= df_train['ETo_sum_day'].quantile(outlier_quantile)]


	if (strategy_for_zeros == 'row_mean') and (dealing_with_zeros_whole_dataset == False):

		if how_to_compute_daily_avg == 'without_zeros':
			df_train[df_train.drop(columns=['ETo_sum_day'], axis=1) == 0] = np.nan
			df_train['SolRad_daily_avg'] = df_train.drop(columns=['ETo_sum_day','Day','Month','Year'], axis=1).mean(axis=1) 

		elif how_to_compute_daily_avg == 'with_zeros':
			df_train['SolRad_daily_avg'] = df_train.iloc[:, 0:24].mean(axis=1)
			df_train[df_train.drop(columns=['ETo_sum_day'], axis=1) == 0] = np.nan


		for col in df_train.columns:		
			df_train[col].fillna(df_train['SolRad_daily_avg'], inplace=True)

		df_train.drop(columns=['SolRad_daily_avg'], axis=1, inplace=True)


	elif strategy_for_zeros == 'drop_column':
		df_train[df_train.drop(columns=['ETo_sum_day'], axis=1) == 0] = np.nan
		df_train = df_train.dropna(how='all', axis=1)


	df_test = df[df['Year'] > df.Year.max() - years_for_test]

	X_train = df_train.drop(columns=['ETo_sum_day','Day','Month','Year'], axis=1)
	X_test = df_test.drop(columns=['ETo_sum_day','Day','Month','Year'], axis=1)

	y_train = df_train['ETo_sum_day']
	y_test = df_test['ETo_sum_day']


	return X_train, X_test, y_train, y_test