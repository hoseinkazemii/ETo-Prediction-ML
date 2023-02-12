


def split_data(df, **params):
	verbose = params.get("verbose")
	years_for_test = params.get("years_for_test")

	if verbose:
		print("splitting data...")
		

	df_train = df[df['Year'] <= df.Year.max() - years_for_test]
	df_test = df[df['Year'] > df.Year.max() - years_for_test]

	X_train = df_train.drop(columns=['ETo_sum_day','Day','Month','Year'], axis=1)
	X_test = df_test.drop(columns=['ETo_sum_day','Day','Month','Year'], axis=1)

	y_train = df_train['ETo_sum_day']
	y_test = df_test['ETo_sum_day']

	return X_train, X_test, y_train, y_test