import pandas as pd

def groupby_date(df, **params):

	verbose = params.get('verbose')
	SolRad_daily = params.get('SolRad_daily')


	if verbose:
		print('groupby date and widening the dataset, saving the final dataset....')

	ETo_tmp = df.groupby('Date').ETo.sum()
	if SolRad_daily:
		Jul_tmp = df.groupby('Date').Jul.mean()

	df = df.reset_index().pivot(columns='Hour', index='Date', values='SolRad')

	df['ETo_sum_day'] = list(ETo_tmp)
	if SolRad_daily:
		df['Jul'] = list(Jul_tmp)

	df.to_csv('./Data/Final_Dataset/final_dataset.csv')
	df = pd.read_csv('./Data/Final_Dataset/final_dataset.csv')

	return df