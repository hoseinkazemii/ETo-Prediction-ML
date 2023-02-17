from sklearn.linear_model import Lasso

def _construct_model(**params):

	alpha = params.get("alpha")
	max_iter = params.get("max_iter")
	tol = params.get("tol")

	model = Lasso(alpha=alpha,
                  max_iter=max_iter, tol=tol)

	return model