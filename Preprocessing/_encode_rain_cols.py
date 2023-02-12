
def _encode_rain_cols(df, **params):

	df['RainTomorrow'] = df['RainTomorrow'].replace({'No':0, 'Yes':1})
	df['RainToday'] = df['RainToday'].replace({'No':0, 'Yes':1})

	return df