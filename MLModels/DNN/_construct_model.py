from ._load_model import _load_model
from ._construct_network import _construct_network

from utils import Logger

def _construct_model(X_train, **params):

	warm_up = params.get('warm_up')
	log = params.get("log")

	input_dim = X_train.shape[1]

	constructed = False
	if warm_up:
		try:
			model = _load_model(**params)
			constructed = True
			log.info("\n\n------------\nA trained model is loaded\n------------\n\n")
		except OSError:
			print ("The model is not trained before. No saved models found")

	if not constructed:
		# Creating the structure of the neural network
		model = _construct_network(input_dim, **params)
		
		# A summary of the model
		stringlist = []
		model.summary(print_fn=lambda x: stringlist.append(x))
		short_model_summary = "\n".join(stringlist)
		log.info(short_model_summary)

	return model