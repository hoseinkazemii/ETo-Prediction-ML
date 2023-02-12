def _save_model(**params):
	
	GRU_model_directory = params.get('GRU_model_directory')
	model_name = params.get("model_name")
	model = params.get("model")

	save_address = f"{GRU_model_directory}/"

	model.save(save_address + f"{model_name}-SavedModel.h5", save_format = 'h5')
	