import numpy as np

def reshape_X(X_train, X_test, **params):
	verbose = params.get("verbose")

	if verbose:
		print("reshaping X_train and X_test for LSTM input layer...")

	X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
	X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

	return X_train, X_test