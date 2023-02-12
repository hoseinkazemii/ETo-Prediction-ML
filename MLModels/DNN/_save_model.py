def _save_model(**params):
	
	DNN_model_directory = params.get('DNN_model_directory')
	model_name = params.get("model_name")
	model = params.get("model")

	save_address = f"{DNN_model_directory}/"

	model.save(save_address + f"{model_name}-SavedModel.h5", save_format = 'h5')
	