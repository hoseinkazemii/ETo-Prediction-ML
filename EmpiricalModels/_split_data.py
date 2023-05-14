


def _split_data(df, **params):
	
	years_for_test = params.get("years_for_test")
	test_stations = params.get("test_stations")	
	train_test_strategy = params.get("train_test_strategy")
	SolRad_daily = params.get("SolRad_daily")
	verbose = params.get("verbose")

	if verbose:
		print("splitting data...")

	if train_test_strategy == "yearly":
		df_test = df[df['Year'] > df.Year.max() - years_for_test]

	elif train_test_strategy == "station_based":
		df_test = df[df['StnId'].isin(test_stations)]

	return df_test