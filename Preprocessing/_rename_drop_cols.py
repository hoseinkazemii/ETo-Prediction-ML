import pandas as pd

def rename_drop_cols(df, **params):
	
	verbose = params.get('verbose')
	SolRad_threshold = params.get('SolRad_threshold')

	if verbose:
		print('renaming the cols, dropping unnecessaries, converting to datetime, and dropping nulls...')


	df.drop(['CIMIS Region', 'qc', 'qc.1'], axis=1, inplace=True)
			
	df.rename(columns={'Stn Id': 'StnId', 'Stn Name': 'StnName',
					   'Sol Rad (W/sq.m)': 'SolRad', 'PM ETo (mm)': 'ETo',
					   'Hour (PST)': 'Hour'}, inplace=True)

	df['Date'] = df['Date'].apply(pd.to_datetime)

	# df.interpolate(method='bfill',inplace=True,subset=['SolRad', 'ETo'])

	# df.dropna(inplace=True)

	df.loc[df["SolRad"] <= SolRad_threshold, "SolRad"] = 0

	return df