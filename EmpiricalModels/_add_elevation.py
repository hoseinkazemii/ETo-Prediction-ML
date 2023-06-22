

def add_elevation(df, **params):

	verbose = params.get("verbose")

	if verbose:
		print("Adding elevation to the dataset...")

	df['Elevation'] = ''

	# Create a dictionary for mapping
	value_map = {
	87: -15.24,
	103: 28.0416,
	106: 160.02,
	125: 152.4,
	193: 15.24,
	202: 77.724,
	217: 218.8464,
	236: 1299.972,
	240: 433.1208,
	241: 68.2752,
	243: -3.048,
	252: 65.2272,
	257: 680.9232,
	261: 836.0664,
	262: 33.8328,
	263: 6.7056,
	264: 1492.9104}

	# Assign values based on dictionary mapping
	df['Elevation'] = df['StnId'].map(value_map)

	return df