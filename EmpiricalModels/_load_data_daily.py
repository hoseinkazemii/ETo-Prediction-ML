import pandas as pd
import glob


def _load_data_daily(**params):
	
	data_path_daily_for_empirical = params.get("data_path_daily_for_empirical")
	verbose = params.get("verbose")

	if verbose:
		print("loading dataset...")


	df = pd.DataFrame()

	for file_name in glob.glob(data_path_daily_for_empirical + '*.csv'):
	    x = pd.read_csv(file_name, low_memory=False)
	    df = pd.concat([df, x], axis=0)

	return df