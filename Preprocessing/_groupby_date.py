# from ._replace_night_solrads_by_zero import replace_night_solrads_by_zero

import pandas as pd

def groupby_date(df, **params):

	verbose = params.get('verbose')


	if verbose:
		print('groupby date and widening the dataset, saving the final dataset....')

	ETo_tmp = df.groupby(['Date','StnId'], sort=False).ETo.sum()
	Jul_tmp = df.groupby(['Date','StnId'], sort=False).Jul.mean()
	# Lat_tmp = df.groupby(['Date','StnId'], sort=False).Latitude.mean()

	df = df.pivot(columns='Hour', index=['Date','StnId'], values='SolRad')
	df.fillna({100.0:0, 200.0:0, 300.0:0, 400.0:0, 500.0:0, 600.0:0,\
				2000.0:0, 2100.0:0, 2200.0:0, 2300.0:0, 2400.0:0}, inplace=True)
	# df.dropna(inplace=True)

	df['ETo_sum_day'] = ETo_tmp
	df['Jul'] = Jul_tmp
	# df['Latitude'] = Lat_tmp


	# df = replace_night_solrads_by_zero(df,**params)

	df.to_csv('./Data/Final_Dataset/final_dataset.csv')
	df = pd.read_csv('./Data/Final_Dataset/final_dataset.csv')
	df.sort_values(by=['StnId', 'Date'], axis=0, ascending=[True,True], inplace=True)

	df.to_csv('./Data/Final_Dataset/final_dataset.csv', index=False)
	raise ValueError
	
	return df