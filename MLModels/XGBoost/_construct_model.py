import joblib
from xgboost import XGBRegressor

def _construct_model(**params):

	n_estimators = params.get("n_estimators")
	max_depth = params.get("max_depth")
	# max_leaves = params.get("max_leaves")
	learning_rate = params.get("learning_rate")
	n_jobs = params.get("n_jobs")
	model_directory = params.get("model_directory")
	model_name = params.get("model_name")
	warm_up = params.get("warm_up")

	if warm_up:
		model = joblib.load(model_directory + f"{model_name}/{model_name}.joblib")
		# model = xgboost.Booster()
		# model.load_model(model_directory + f"{model_name}/{model_name}.json")

	else:
		model = XGBRegressor(n_estimators=n_estimators,
										max_depth=max_depth,
										# max_leaves=max_leaves,
										learning_rate = learning_rate,
										verbosity = 2,
		                        		n_jobs=n_jobs)
	return model