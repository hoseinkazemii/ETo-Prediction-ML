import logging as log
import pprint

def _log_hyperparameters(**params):
	
	layers = params.get('layers')
	input_activation_func = params.get('input_activation_func')
	hidden_activation_func = params.get('hidden_activation_func')
	final_activation_func = params.get('final_activation_func')
	loss_func = params.get('loss_func')
	epochs = params.get('epochs')
	min_delta = params.get('min_delta')
	patience = params.get('patience')
	batch_size = params.get('batch_size')
	should_early_stop = params.get('should_early_stop')
	should_checkpoint = params.get('should_checkpoint')
	regul_type = params.get('regul_type')
	act_regul_type = params.get('act_regul_type')
	reg_param = params.get('reg_param')
	dropout = params.get('dropout')
	optimizer = params.get('optimizer')
	random_state = params.get('random_state')
	split_size = params.get('split_size')

	log.info(pprint.pformat({'layers': layers,
							'input_activation_func': input_activation_func,
							'hidden_activation_func': hidden_activation_func,
							'final_activation_func': final_activation_func,
							'loss_func': loss_func,
							'epochs': epochs,
							'min_delta': min_delta,
							'patience': patience,
							'batch_size': batch_size,
							'should_early_stop': should_early_stop,
							'should_checkpoint': should_checkpoint,
							'regul_type': regul_type,
							'act_regul_type': act_regul_type,
							'reg_param': reg_param,
							'dropout': dropout,
							'optimizer': optimizer,
							'random_state': random_state,
							'split_size': split_size,
							}))