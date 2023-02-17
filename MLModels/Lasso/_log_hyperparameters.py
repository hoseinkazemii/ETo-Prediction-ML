import logging as log
import pprint

def _log_hyperparameters(**params):

	alpha = params.get("alpha")
	max_iter = params.get("max_iter")
	tol = params.get("tol")

	log.info(pprint.pformat({'alpha': alpha,
							'max_iter': max_iter,
							'tol': tol,}))