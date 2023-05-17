import warnings
warnings.filterwarnings("ignore")

from Preprocessing import *
# from MLModels import *
# from EmpiricalModels import *

def run():
	settings = {
	"data_path_hourly" : "./Data/For_The_Final_Run/Train_Set/",
	"data_path_daily" : "./Data/For_The_Final_Run/Train_Set/",
	"data_path_daily_for_empirical": "./Data/For_The_Final_Run/Test_Set/Daily/",
	"data_path_hourly_for_run" : "./Data/Final_Dataset/Hourly_Run/",
	"verbose" : True,
	"random_state" : 42,
	"SolRad_threshold": 0,
	"train_test_strategy": "station_based", # "yearly" , "station_based"
	"seasonal":False,
	"target_season": "Fall", # "Winter" , "Spring" , "Summer" , "Fall"
	# "training_stations": [2,5,6,7,12,13,15,35,39,41,43,44,47,52,64,68,70,71,\
 #  						  75,77,78,80,83,84,88,90,99,104,107,113,114,117,124,126,\
	# 					  129,131,135,136,140,143,144,146,147,148,150,152,153,157,158,160,163,165,\
	# 					  170,171,173,174,178,179,184,191,192,194,195,197,198,199,200,\
 # 						  204,205,206,207,208,210,212,213,214,215,216,219,220,\
	# 					  222,224,225,226,227,229,237,239,242,244,247,248,249,250,\
	# 					  253,254], #FOR Optuna	
	# "test_stations": [91,105,182,187,209,211,218,221,223,228,231,245,251,258,259,260], # FOR Optuna


	"training_stations": [2,5,6,7,12,13,15,35,39,41,43,44,47,52,64,68,70,71,\
  						  75,77,78,80,83,84,88,90,91,99,104,105,107,113,114,117,124,126,\
						  129,131,135,136,140,143,144,146,147,148,150,152,153,157,158,160,163,165,\
						  170,171,173,174,178,179,182,184,187,191,192,194,195,197,198,199,200,\
 						  204,205,206,207,208,209,210,211,212,213,214,215,216,218,219,220,221,\
						  222,223,224,225,226,227,228,229,231,237,239,242,244,245,247,248,249,250,251,\
						  253,254,258,259,260],
	# "test_stations":[87],
	"test_stations":[87,103,106,125,193,202,217,236,240,241,243,252,257,261,262,263,264],


	"years_for_test": 5,
	"include_zeros": True,
	"strategy_for_zeros": 'row_mean', # "row_mean" , "drop_column"
	"dropping_cols_strategy": 'correlation', # "correlation" , "feature_importance"
	"correlation_method":'spearman_', # "mutual_info" , "pearson_" , "spearman_"
	"how_to_compute_daily_avg": 'without_zeros', # "with_zeros" , "without_zeros"
	"scaling_method": 'robust', # "min_max" , "standard" , "robust"
	"outlier_quantile": 0.98,
	"SolRad_daily": True,
	"model_directory":"./SavedModels/",
	"warm_up":True,

	}

	# Step1-Preprocessing:

	myData = PreprocessData()
	myData.preprocess_and_save_data(**settings)


	# Step2-Training:
	# 2-1: CatBoost

	# cb_settings = {'iterations' : 1500, #[1200, 1600], # [low, high]
	# 				'learning_rate' : 0.003, #[0.001, 0.1], # Same as 'iterations'
	# 				'depth' : 9, #[9,11],
	# 				'boosting_type' : 'Ordered', #['Ordered', 'Plain'],
	# 				'l2_leaf_reg' : 0.001,
	# 				'loss_function' : 'RMSE',
	# 				'allow_writing_files' : False,
	# 				'eval_metric' : "RMSE",
	# 				'task_type' : 'CPU',
	# 				'verbose_cb' : 300,
	# 				'thread_count' : -1,
	# 				"model_name" : "CatBoost",}


	# X_train, X_test, y_train, y_test = load_X_y(**settings)

	# myCatBoostModel = CatBoostModel(**{**cb_settings,
	# 	                                          **settings})


	# Training the model
	# myCatBoostModel._construct_model(X_train, X_test, y_train, y_test)
	# myCatBoostModel.run(X_train, X_test, y_train, y_test)


	# Finding the best hyperparameters:
	# myCatBoostModel._input_X_y(X_train, X_test, y_train, y_test)
	# myCatBoostModel.optimize(n_trials=100)


	# 2-2: RandomForest

	# rf_settings = {'n_estimators' : 900,
	# 				'max_depth' : 9,
	# 				'min_samples_split' : 2,
	# 				'min_samples_leaf' : 1,
	# 				'max_features' : 'auto',
	# 				'n_jobs' : -1,
	# 				"verbose_rf" : 2,
	# 				"model_name" : "RF",

	# 				}

	# X_train, X_test, y_train, y_test = load_X_y(**settings)

	# myRFModel = RFModel(**{**rf_settings,
	# 									**settings})
	# myRFModel._construct_model()
	# myRFModel.run(X_train, X_test, y_train, y_test)


	# 2-3: DNN

	# DNN_settings = {'DNN_model_directory' : './SavedModels/DNN',
	# 		  'layers' : [16,32,16],
	# 		  'input_activation_func' : 'relu',
	# 		  'hidden_activation_func' : 'relu',
	# 		  'loss_func' : 'mean_squared_error',
	# 		  'epochs' : 30,
	# 		  'min_delta' : 0.00001,
	# 		  'patience' : 10,
	# 	      'batch_size' : 64,
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
	# 		  'model_name' : 'DNN',}

	# X_train, X_test, y_train, y_test = load_X_y(**settings)
			  
	# myDNNModel = DNNModel(**{**DNN_settings,
	# 										**settings})
	# myDNNModel._construct_model(X_train)
	# myDNNModel.run(X_train, X_test, y_train, y_test)


	# 2-4: LSTM

	# LSTM_settings = {'LSTM_model_directory' : './SavedModels',
	# 		  'layers' : [32,64,32],
	# 		  'input_activation_func' : 'relu',
	# 		  'hidden_activation_func' : 'relu',
	# 		  'final_activation_func' : 'linear',
	# 		  'loss_func' : 'mean_squared_error',
	# 		  'stateful' : False,
	# 		  'epochs' : 50,
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

	# X_train, X_test, y_train, y_test = load_X_y(**settings)

	# myLSTMModel = LSTMModel(**{**LSTM_settings,
	# 										**settings})
	# X_train, X_test = reshape_X(X_train, X_test, **settings)
	# myLSTMModel._construct_model(X_train)
	# myLSTMModel.run(X_train, X_test, y_train, y_test)


	# 2-5: GRU

	# GRU_settings = {'GRU_model_directory' : './SavedModels',
	# 		  'layers' : [15,30],
	# 		  'input_activation_func' : 'relu',
	# 		  'hidden_activation_func' : 'relu',
	# 		  'final_activation_func' : 'linear',
	# 		  'loss_func' : 'mean_squared_error',
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

	# X_train, X_test, y_train, y_test = load_X_y(**settings)

	# myGRUModel = GRUModel(**{**GRU_settings,
	# 										**settings})
	# X_train, X_test = reshape_X(X_train, X_test, **settings)
	# myGRUModel._construct_model(X_train)
	# myGRUModel.run(X_train, X_test, y_train, y_test)


	# 2-6: XGBoost

	# xgb_settings = {'n_estimators' : 1000,
	# 				'max_depth' : 7,
	# 				'max_leaves' : 9,
	# 				'learning_rate' : 0.3,
	# 				'n_jobs' : -1,
	# 				"model_name" : "XGBoost",}

	# X_train, X_test, y_train, y_test = load_X_y(**settings)

	# myXGBoostModel = XGBoostModel(**{**xgb_settings,
	# 	                                          **settings})
	# myXGBoostModel._construct_model()
	# myXGBoostModel.run(X_train, X_test, y_train, y_test)


	# 2-7: Lasso

	# lasso_settings = {'alpha' : 0.001,
	# 				'max_iter' : 1000,
	# 				'tol' : 0.0001,
	# 				'model_name' : "Lasso",}

	# X_train, X_test, y_train, y_test = load_X_y(**settings)

	# myLassoModel = LassoModel(**{**lasso_settings,
	# 	                                          **settings})
	# myLassoModel._construct_model()
	# myLassoModel.run(X_train, X_test, y_train, y_test)


	# 2-8: LightGBM

	# lgbm_settings = {'n_estimators' : 2000,
	# 				'max_depth' : 7,
	# 				'max_leaves' : 9,
	# 				'learning_rate' : 0.01,
	# 				'num_leaves': 30,
	# 				'n_jobs' : -1,
	# 				'metric' : 'rmse',
	# 				"model_name" : "LightGBM",}

	# X_train, X_test, y_train, y_test = load_X_y(**settings)

	# myLightGBMModel = LightGBMModel(**{**lgbm_settings,
	# 	                                          **settings})
	# myLightGBMModel._construct_model()
	# myLightGBMModel.run(X_train, X_test, y_train, y_test)



	# Step3-Empirical Models:
	
	# empirical_settings = {'model_name' : 'Empirical-',
	# "empirical_method": "R", # "HS" , "PT" , "R"

	# 				}


	# myDailyData = ApplyEmpiricalModels()
	# myDailyData.test_empirical_models(**{**empirical_settings,
	# 	                                          **settings})







if __name__ == "__main__":
	run()
