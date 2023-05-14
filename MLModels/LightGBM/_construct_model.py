import joblib
from lightgbm import LGBMRegressor
def _construct_model(**params):

	n_estimators = params.get("n_estimators")
	max_depth = params.get("max_depth")
	num_leaves = params.get("num_leaves")
	learning_rate = params.get("learning_rate")
	metric = params.get("metric")
	model_directory = params.get("model_directory")
	model_name = params.get("model_name")
	warm_up = params.get("warm_up")
	n_jobs = params.get("n_jobs")


	if warm_up:
		model = joblib.load(model_directory + f"{model_name}/{model_name}.joblib")
		# model = xgboost.Booster()
		# model.load_model(model_directory + f"{model_name}/{model_name}.json")

	else:
		model = LGBMRegressor(max_depth = max_depth,
							  num_leaves = num_leaves,
							  learning_rate = learning_rate,
							  n_estimators = n_estimators,
							  n_jobs = n_jobs,
							  metric = metric,)

	return model