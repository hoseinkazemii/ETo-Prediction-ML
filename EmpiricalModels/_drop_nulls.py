import pandas as pd


def _drop_nulls(df, **params):
	verbose = params.get("verbose")

	if verbose:
		print("dropping nulls...")

	df = df.dropna(subset=['Jul','NetRad','ETo','Max_Temp','Min_Temp','Avg_Temp','RelHum_Avg'])

	return df