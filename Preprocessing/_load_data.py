import glob
import pandas as pd


def load_data(**params):
	data_path_hourly = params.get("data_path_hourly")
	verbose = params.get("verbose")

	if verbose:
		print("loading the dataset...")
		
	df = pd.DataFrame()

	for file_name in glob.glob(data_path_hourly + '*.csv'):
	    x = pd.read_csv(file_name, low_memory=False)
	    df = pd.concat([df, x], axis=0)


	return df