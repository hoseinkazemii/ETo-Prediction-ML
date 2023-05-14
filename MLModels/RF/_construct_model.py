import joblib
from sklearn.ensemble import RandomForestRegressor

def _construct_model(**params):

	max_depth = params.get("max_depth")
	min_samples_split = params.get("min_samples_split")
	min_samples_leaf = params.get("min_samples_leaf")
	max_features = params.get("max_features")
	verbose_rf = params.get("verbose_rf")
	n_jobs = params.get("n_jobs")
	n_estimators = params.get("n_estimators")
	model_directory = params.get("model_directory")
	model_name = params.get("model_name")
	warm_up = params.get("warm_up")

	if warm_up:
		model = joblib.load(model_directory + f"{model_name}/{model_name}.joblib")

	else:
		model = RandomForestRegressor(n_estimators=n_estimators,
									max_depth=max_depth,
	                        		min_samples_split=min_samples_split,
	                        		min_samples_leaf=min_samples_leaf,
	                        		max_features=max_features,
	                        		bootstrap=True,
	                        		n_jobs=n_jobs, 
	                        		verbose=verbose_rf)

	return model