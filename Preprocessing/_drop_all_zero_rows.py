

def drop_all_zero_rows(df, **params):

	verbose = params.get("verbose")
	SolRad_daily = params.get("SolRad_daily")

	if verbose:
		print("Droppping rows contaning zeros from 8 to 17...")

	if SolRad_daily:

		df = df[df['SolRad_daily_avg']!=0]

	else:

		df = df[((df["800"] != 0) & \
		(df["900"] != 0) & \
		(df["1000"] !=0) & \
		(df["1100"] != 0) & \
		(df["1200"] != 0) & \
		(df["1300"] != 0)) & \
		(df["1400"] != 0) & \
		(df["1500"] != 0) & \
		(df["1600"] != 0) & \
		(df["1700"] != 0)]


	return df