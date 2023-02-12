import pandas as pd

def rename_drop_cols(df, **params):
	verbose = params.get('verbose')

	if verbose:
		print('renaming the cols, dropping unnecessaries, and converting to datetime...')

	df.drop(['CIMIS Region', 'qc', 'qc.1', 'Jul'], axis=1, inplace=True)
	
	df.rename(columns={'Stn Id': 'StnId', 'Stn Name': 'StnName',
					   'Sol Rad (W/sq.m)': 'SolRad', 'PM ETo (mm)': 'ETo',
					   'Hour (PST)': 'Hour'}, inplace=True)

	df['Date'] = df['Date'].apply(pd.to_datetime)

	return df