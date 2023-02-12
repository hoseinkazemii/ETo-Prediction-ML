from sklearn.preprocessing import MinMaxScaler

def scaler(X_train, X_test, **params):
	verbose = params.get("verbose")

	if verbose:
		print("scaling data...")

	x_scaler = MinMaxScaler(feature_range = (0,1)).fit(X_train)
	X_train = x_scaler.transform(X_train)
	x_scaler = MinMaxScaler(feature_range = (0,1)).fit(X_test)
	X_test = x_scaler.transform(X_test)

	return X_train, X_test