from ._log_hyperparameters import _log_hyperparameters
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.regularizers import l1, l2


def _construct_network(input_dim, **params):
	
	layers = params.get('layers')
	output_dim = params.get('output_dim')
	input_activation_func = params.get('input_activation_func')
	hidden_activation_func = params.get('hidden_activation_func')
	regul_type = params.get('regul_type')
	act_regul_type = params.get('act_regul_type')
	reg_param = params.get('reg_param')
	dropout = params.get('dropout')	
	loss_func = params.get('loss_func')
	optimizer = params.get('optimizer')
		
	l = l2 if regul_type == 'l2' else l1
	actl = l1 if act_regul_type == 'l1' else l2


	model = Sequential()
	
	model.add(Dense(layers[0],
					input_shape = (input_dim,),
					activation = input_activation_func,
					kernel_regularizer = l(reg_param),
					activity_regularizer = actl(reg_param)))
	
	for ind in range(1,len(layers)):
		model.add(Dense(layers[ind],
						activation = hidden_activation_func,
						kernel_regularizer = l(reg_param),
						activity_regularizer = actl(reg_param)))
		model.add(Dropout(dropout))
	
	model.add(Dense(output_dim))
	 
	# Compile model
	model.compile(loss=loss_func,
				  optimizer=optimizer,
				  metrics=['mean_squared_error'])

	return model