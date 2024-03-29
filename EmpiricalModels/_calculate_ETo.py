from utils import Logger
from ._seasonal_split import _seasonal_split
from ._add_elevation import add_elevation
from ._add_latitude import add_latitude
from ._split_data import _split_data
from .RegressionReport import evaluate_regression

import pandas as pd
import os
import math
from datetime import datetime


def _calculate_ETo(**params):

	data_path_test_run = params.get("data_path_test_run")
	empirical_method = params.get("empirical_method")
	logger = params.get('logger')
	verbose = params.get("verbose")
	model_name = params.get("model_name")
	# outlier_margin = params.get("outlier_margin")
	seasonal = params.get('seasonal')

	
	if verbose:
		print("Using empirical equations to calculate ETo...")

	model_name = model_name + empirical_method

	now = datetime.now().strftime("%Y%m%d%H%M")

	report_directory = \
		os.path.join(".", 'reports', model_name, f"{now}")
	if not os.path.exists(report_directory):
		os.makedirs(report_directory)

	log = Logger(address = f"{report_directory}/Log.log")

	df_test = pd.read_csv(data_path_test_run+'final_dataset.csv')

	df_test.dropna(axis=0, inplace=True, how='any',\
	 subset=['100','200','300','400','500','600','700','800','900'\
	 ,'1000','1100','1200','1300','1400','1500','1600','1700','1800','1900'\
	 ,'2000','2100','2200','2300','2400'\
	 ,'Jul','NetRad','ETo_sum_day','Max_Temp','Min_Temp','Avg_Temp','RelHum_Avg'])

	# Create a list of columns to check
	columns_to_check_zero = ['100','200','300','400','500','600','700','800','900'\
	 ,'1000','1100','1200','1300','1400','1500','1600','1700','1800','1900'\
	 ,'2000','2100','2200','2300','2400']

	# Filter the dataframe to include only rows where the specified columns are not all zero
	df_test = df_test.loc[~(df_test[columns_to_check_zero] == 0).all(axis=1)]

	columns_to_keep = ['StnId','Jul','NetRad','Max_Temp','Min_Temp','Avg_Temp','RelHum_Avg','ETo_sum_day','Day','Month','Year']
	df_test = df_test[columns_to_keep]


	df_test = add_elevation(df_test, **params)
	df_test = add_latitude(df_test, **params)


	# df_test = df_test[df_test['ETo_sum_day'] <= outlier_margin]

	# Split data based on different seasons

	df_test = _split_data(df_test, **params)

	if seasonal:
		df_test = _seasonal_split(df_test, **params)

	y_pred_test = []
	y_test = list(df_test['ETo_sum_day'])

	if empirical_method == "HS":
		
		Gsc = 0.082

		for i in df_test.index:
			
			latitude = df_test.loc[i,'Latitude']
			phi = (latitude*math.pi)/180
			J = df_test.loc[i,'Jul']
			T_avg = df_test.loc[i,'Avg_Temp']
			T_max = df_test.loc[i,'Max_Temp']
			T_min = df_test.loc[i,'Min_Temp']

			dr = 1+0.033*math.cos((2*math.pi*J)/365)
			delta = 0.409*math.sin(((2*math.pi*J)/365)-1.39)
			omega = math.acos(-math.tan(phi)*math.tan(delta))
			Ra = 0.408*((24*60)/math.pi)*Gsc*dr*\
				(omega*math.sin(phi)*math.sin(delta)+\
				math.cos(phi)*math.cos(delta)*math.sin(omega))

			ETo = 0.408*0.0023*Ra*(T_avg+17.8)* pow((T_max - T_min), 0.5)

			y_pred_test.append(ETo)

	elif empirical_method == "PT":
		

		for i in df_test.index:

			T_max = df_test.loc[i,'Max_Temp']
			T_min = df_test.loc[i,'Min_Temp']
			Elevation = df_test.loc[i,'Elevation']
			Rn = df_test.loc[i,'NetRad']

			T_mean = (T_max + T_min)/2
			e0 = 0.6108 * math.exp((17.27*T_mean) / (T_mean+237.3))
			Delta = (4099*e0) / (pow((T_mean+237.3), 2))
			Beta = 101.3 * (pow(((293-0.0065*Elevation)/293), 5.26))
			Gamma = 0.00163 * (Beta / 2.45)

			ETo = 0.0864*1.26*((Delta)/(Delta+Gamma))*(Rn/2.45)

			y_pred_test.append(ETo)

	elif empirical_method == "R":
				
		for i in df_test.index:

			T_avg = df_test.loc[i,'Avg_Temp']
			RH = df_test.loc[i,'RelHum_Avg']

			ETo = 0.00006 * pow((T_avg+25), 2) * (100 - RH)

			y_pred_test.append(ETo)



	evaluate_regression(
	label = f'OnTest',
	y_test = y_test,
	y_pred_test = y_pred_test,
	model_name = model_name,
	logger = log,
	report_directory = report_directory)