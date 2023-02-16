import warnings
warnings.filterwarnings("ignore")
import pandas as pd

from Preprocessing import *
from MLModels import *

def run():
	settings = {
	"data_path" : "./Data/",
	"verbose" : True,
	"random_state" : 42,
	"SolRad_threshold": 5,
	"years_for_test": 5,
	"strategy_for_zeros": 'row_mean', # "row_mean" , "drop_column"
	"how_to_compute_daily_avg": 'without_zeros', # "with_zeros" , "without_zeros"
	"dealing_with_zeros_whole_dataset": True,
	"scaling_method": 'robust', # "min_max" , "standard" , "robust"
	"outlier_quantile": 0.99,
	"correlation_method":'pearson_', # "mutual_info" , "pearson_"

	}

	# Step1-Preprocessing:

	df = load_data(**settings)
	df = rename_drop_cols(df, **settings)
	df = groupby_date(df, **settings)
	df = make_datetime_cols(df, **settings)

	X_train, X_test, y_train, y_test = split_data_and_deal_with_zeros(df, **settings)
	X_train, X_test = scaler(X_train, X_test, **settings)


	# Step2-Training:
	# 2-1: CatBoost

	# cb_settings = {'iterations' : 800,
	# 				'learning_rate' : 0.05,
	# 				'depth' : 9,
	# 				'l2_leaf_reg' : 0.001,
	# 				'loss_function' : 'RMSE',
	# 				'allow_writing_files' : False,
	# 				'eval_metric' : "RMSE",
	# 				'task_type' : 'CPU',
	# 				'verbose_cb' : 400,
	# 				'boosting_type' : 'Ordered',
	# 				'thread_count' : -1,
	# 				"model_name" : "CatBoost",}


	# myCatBoostModel = CatBoostModel(**{**cb_settings,
	# 	                                          **settings})
	# myCatBoostModel._construct_model()
	# myCatBoostModel.run(X_train, X_test, y_train, y_test)

	# 2-2: RandomForest

	# rf_settings = {'n_estimators' : 100,
	# 				'max_depth' : 200,
	# 				'min_samples_split' : 2,
	# 				'min_samples_leaf' : 1,
	# 				'max_features' : 'auto',
	# 				'n_jobs' : -1,
	# 				"verbose_rf" : 2,
	# 				"model_name" : "RF",

	# 				}

	# myRFModel = RFModel(**{**rf_settings,
	# 									**settings})
	# myRFModel._construct_model()
	# myRFModel.run(X_train, X_test, y_train, y_test)

	# 2-3: DNN

	# DNN_settings = {'DNN_model_directory' : './SavedModels/DNN',
	# 		  'layers' : [10,30,20],
	# 		  'input_activation_func' : 'relu',
	# 		  'hidden_activation_func' : 'relu',
	# 		  'loss_func' : 'mean_squared_error',
	# 		  'epochs' : 2,
	# 		  'min_delta' : 0.00001,
	# 		  'patience' : 10,
	# 	      'batch_size' : 32,
	# 		  'should_early_stop' : False,
	# 		  'should_checkpoint' : False,
	# 	      'regul_type' : 'l2',
	# 		  'act_regul_type' : 'l1',
	# 		  'reg_param' : 0.01,
	# 		  'dropout' : 0.2,
	# 		  'optimizer' : 'adam',
	# 		  'random_state' : 42,
	# 		  'split_size' : 0.2,
	# 		  'output_dim' : 1,
	# 		  'warm_up' : False,
	# 		  'model_name' : 'DNN',}

			  
	# myDNNModel = DNNModel(**{**DNN_settings,
	# 										**settings})
	# myDNNModel._construct_model(X_train)
	# myDNNModel.run(X_train, X_test, y_train, y_test)

	# 2-4: LSTM

	# LSTM_settings = {'LSTM_model_directory' : './SavedModels',
	# 		  'layers' : [15,30],
	# 		  'input_activation_func' : 'relu',
	# 		  'hidden_activation_func' : 'relu',
	# 		  'final_activation_func' : 'sigmoid',
	# 		  'loss_func' : 'binary_crossentropy',
	# 		  'epochs' : 10,
	# 		  'min_delta' : 0.00001,
	# 		  'patience' : 10,
	# 	      'batch_size' : 32,
	# 		  'should_early_stop' : False,
	# 		  'should_checkpoint' : False,
	# 	      'regul_type' : 'l2',
	# 		  'act_regul_type' : 'l1',
	# 		  'reg_param' : 0.01,
	# 		  'dropout' : 0.2,
	# 		  'optimizer' : 'adam',
	# 		  'random_state' : 42,
	# 		  'split_size' : 0.2,
	# 		  'output_dim' : 1,
	# 		  'warm_up' : False,
	# 		  'model_name' : 'LSTM',}

	# myLSTMModel = LSTMModel(**{**LSTM_settings,
	# 										**settings})
	# X_train, X_test = reshape_X(X_train, X_test, **settings)
	# myLSTMModel._construct_model(df_all, X_train)
	# myLSTMModel.run(X_train, X_test, y_train, y_test)

	# 2-5: GRU

	# GRU_settings = {'GRU_model_directory' : './SavedModels',
	# 		  'layers' : [15,30],
	# 		  'input_activation_func' : 'relu',
	# 		  'hidden_activation_func' : 'relu',
	# 		  'final_activation_func' : 'sigmoid',
	# 		  'loss_func' : 'binary_crossentropy',
	# 		  'epochs' : 30,
	# 		  'min_delta' : 0.00001,
	# 		  'patience' : 10,
	# 	      'batch_size' : 32,
	# 		  'should_early_stop' : False,
	# 		  'should_checkpoint' : False,
	# 	      'regul_type' : 'l2',
	# 		  'act_regul_type' : 'l1',
	# 		  'reg_param' : 0.01,
	# 		  'dropout' : 0.2,
	# 		  'optimizer' : 'adam',
	# 		  'random_state' : 42,
	# 		  'split_size' : 0.2,
	# 		  'output_dim' : 1,
	# 		  'warm_up' : False,
	# 		  'model_name' : 'GRU',}

	# myGRUModel = GRUModel(**{**GRU_settings,
	# 										**settings})
	# X_train, X_test = reshape_X(X_train, X_test, **settings)
	# myGRUModel._construct_model(df_all, X_train)
	# myGRUModel.run(X_train, X_test, y_train, y_test)







if __name__ == "__main__":
	run()
