from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler

def scaler(X_train, X_test, **params):
	verbose = params.get("verbose")
	scaling_method = params.get("scaling_method")

	if verbose:
		print("scaling data...")

	if scaling_method == 'min_max':
		x_scaler = MinMaxScaler(feature_range = (0,1)).fit(X_train)
		X_train = x_scaler.transform(X_train)
		x_scaler = MinMaxScaler(feature_range = (0,1)).fit(X_test)
		X_test = x_scaler.transform(X_test)
	
	elif scaling_method == 'standard':
		x_scaler = StandardScaler().fit(X_train)
		X_train = x_scaler.transform(X_train)
		x_scaler = StandardScaler().fit(X_test)
		X_test = x_scaler.transform(X_test)

	elif scaling_method == 'robust':
		x_scaler = StandardScaler().fit(X_train)
		X_train = x_scaler.transform(X_train)
		x_scaler = StandardScaler().fit(X_test)
		X_test = x_scaler.transform(X_test)


	return X_train, X_test