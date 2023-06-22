


def replace_night_Rso_by_zero(df, **params):

	verbose = params.get('verbose')

	if verbose:
		print('Replacing Rso in night hours with 0...')


	night_hours = ['Rso_1','Rso_2','Rso_3','Rso_4','Rso_5','Rso_6','Rso_21','Rso_22','Rso_23','Rso_24']

	for col in night_hours:
	    df[col].values[:] = 0

	return df