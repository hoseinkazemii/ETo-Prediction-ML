from ._log_hyperparameters import _log_hyperparameters
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.regularizers import l1, l2


def _construct_network(input_dim, X_train, **params):

	layers = params.get('layers')
	output_dim = params.get('output_dim')
	input_activation_func = params.get('input_activation_func')
	hidden_activation_func = params.get('hidden_activation_func')
	final_activation_func = params.get('final_activation_func')
	regul_type = params.get('regul_type')
	act_regul_type = params.get('act_regul_type')
	reg_param = params.get('reg_param')
	dropout = params.get('dropout')
	loss_func = params.get('loss_func')
	optimizer = params.get('optimizer')
		
	l = l2 if regul_type == 'l2' else l1
	actl = l1 if act_regul_type == 'l1' else l2


	model = Sequential()
	
	model.add(LSTM(layers[0],
					input_shape = (X_train.shape[1], X_train.shape[2]),
					activation = input_activation_func,
					kernel_regularizer = l(reg_param),
					activity_regularizer = actl(reg_param),
					return_sequences = True))
	if len(layers) == 2:

		for ind in range(1,len(layers)):
			model.add(LSTM(layers[ind],
							activation = hidden_activation_func,
							kernel_regularizer = l(reg_param),
							activity_regularizer = actl(reg_param)))
			model.add(Dropout(dropout))
	else:
		for ind in range(1,len(layers)-1):
			model.add(LSTM(layers[ind],
							activation = hidden_activation_func,
							kernel_regularizer = l(reg_param),
							activity_regularizer = actl(reg_param),
							return_sequences = True))
			model.add(Dropout(dropout))

		model.add(LSTM(layers[-1],
						activation = hidden_activation_func,
						kernel_regularizer = l(reg_param),
						activity_regularizer = actl(reg_param)))

	model.add(Dense(output_dim, activation = final_activation_func))

	 
	# Compile model
	model.compile(loss=loss_func,
				  optimizer=optimizer,
				  metrics=['accuracy'])

	return model