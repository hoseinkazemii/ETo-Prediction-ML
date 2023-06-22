
def replace_unusual_Rs(df, **params):

	verbose = params.get("verbose")

	if verbose:
		print("Replacing SolRads by Rso, where SolRad is greater than Rso...")


	df.loc[df['SolRad_daily_avg'] > df['Rso'], 'SolRad_daily_avg'] = df['Rso']

	return df
