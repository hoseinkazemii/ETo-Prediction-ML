import logging as log
import pprint

def _log_hyperparameters(**params):

	n_estimators = params.get("n_estimators")
	max_depth = params.get("max_depth")
	max_leaves = params.get("max_leaves")
	num_leaves = params.get("num_leaves")
	learning_rate = params.get("learning_rate")
	n_jobs = params.get("n_jobs")

	log.info(pprint.pformat({'n_estimators': n_estimators,
							'max_depth': max_depth,
							'max_leaves': max_leaves,
							'learning_rate': learning_rate,
							'n_jobs': n_jobs,
							'max_depth': max_depth,		
							}))