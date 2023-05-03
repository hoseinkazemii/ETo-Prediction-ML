from tensorflow.keras.models import load_model

def _load_model(**params):
	
	should_checkpoint = params.get('should_checkpoint')
	GRU_model_directory = params.get('GRU_model_directory')
	model_name = params.get('model_name')

	# load json and create model
	if should_checkpoint:
		model_type = 'BestModel'
	else:
		model_type = 'SavedModel'

	model = load_model(GRU_model_directory + "/" + f"{model_name}-{model_type}.h5")

	return model
