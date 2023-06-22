


def replace_night_solrads_by_zero(df, **params):

	verbose = params.get('verbose')

	if verbose:
		print('Replacing SolRad in night hours with 0...')


	night_hours = [100,200,300,400,500,600,2100,2200,2300,2400]

	for col in night_hours:
	    df[col].values[:] = 0

	return df