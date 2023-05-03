


def _split_data(df, **params):
	
	years_for_test = params.get("years_for_test")	
	train_test_strategy = params.get("train_test_strategy")
	verbose = params.get("verbose")

	if verbose:
		print("splitting data...")

	if train_test_strategy == "yearly":
		df_test = df[df['Year'] > df.Year.max() - years_for_test]

	return df_test