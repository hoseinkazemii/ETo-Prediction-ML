import pandas as pd


def _drop_nulls(df, **params):
	verbose = params.get("verbose")

	if verbose:
		print("dropping or filling nulls...")

	print(df.shape)
	# df.interpolate(method='linear',inplace=True,subset=['Jul','NetRad','ETo','Max_Temp','Min_Temp','Avg_Temp','RelHum_Avg'])
	df = df.dropna(subset=['Jul','NetRad','ETo','Max_Temp','Min_Temp','Avg_Temp','RelHum_Avg'])
	print(df.shape)
	raise ValueError
	return df