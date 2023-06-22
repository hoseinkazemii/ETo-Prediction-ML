import pandas as pd

def load_data_for_X_y(**params):
	
	verbose = params.get("verbose")
	data_path_test_run = params.get("data_path_test_run")

	if verbose:
		print("Loading the data...")

	df = pd.read_csv(data_path_test_run+'final_dataset.csv')
	
	df.dropna(axis=0, inplace=True, how='any',\
	 subset=['100','200','300','400','500','600','700','800','900'\
	 ,'1000','1100','1200','1300','1400','1500','1600','1700','1800','1900'\
	 ,'2000','2100','2200','2300','2400'\
	 ,'Jul','NetRad','ETo_sum_day','Max_Temp','Min_Temp','Avg_Temp','RelHum_Avg'])
	
	# Create a list of columns to check
	columns_to_check_zero = ['100','200','300','400','500','600','700','800','900'\
	 ,'1000','1100','1200','1300','1400','1500','1600','1700','1800','1900'\
	 ,'2000','2100','2200','2300','2400']

	# Filter the dataframe to include only rows where the specified columns are not all zero
	df = df.loc[~(df[columns_to_check_zero] == 0).all(axis=1)]

	columns_to_keep = ['Date','StnId','100','200','300','400','500','600','700',
	'800','900','1000','1100','1200','1300','1400','1500','1600','1700','1800',
	'1900','2000','2100','2200','2300','2400','Jul','ETo_sum_day']
	df = df[columns_to_keep]	

	return df