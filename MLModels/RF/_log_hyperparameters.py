import logging as log
import pprint

def _log_hyperparameters(**params):

	n_estimators = params.get("n_estimators")
	max_depth = params.get("max_depth")
	min_samples_leaf = params.get("min_samples_leaf")
	min_samples_split = params.get("n_estimators")
	max_features = params.get("max_features")
	n_jobs = params.get("n_jobs")
	random_state = params.get("random_state")
	log = params.get("log")

	log.info(pprint.pformat({'n_estimators': n_estimators,
							'max_depth': max_depth,
							'min_samples_leaf': min_samples_leaf,
							'min_samples_split': min_samples_split,
							'max_features': max_features,
							'n_jobs': n_jobs,
							'random_state': random_state,
							}))