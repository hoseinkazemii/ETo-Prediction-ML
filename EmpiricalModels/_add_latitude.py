

def add_latitude(df, **params):

	verbose = params.get("verbose")

	if verbose:
		print("Adding latitude to the dataset...")

	df['Latitude'] = ''

	# Create a dictionary for mapping
	value_map = {
	87: 32.806183,
	103: 38.52665,
	106: 38.982581,
	125: 35.205583,
	193: 36.633222,
	202: 35.028281,
	217: 34.269031,
	236: 41.802476,
	240: 33.76,
	241: 33.4625,
	243: 38.249622,
	252: 36.456728,
	257: 35.659128,
	261: 41.533989,
	262: 38.065692,
	263: 41.894592,
	264: 39.777452}

	# Assign values based on dictionary mapping
	df['Latitude'] = df['StnId'].map(value_map)

	return df