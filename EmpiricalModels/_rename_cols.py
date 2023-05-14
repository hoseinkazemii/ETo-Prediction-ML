


def _rename_cols(df, **params):

	verbose = params.get("verbose")

	if verbose:
		print("renaming columns...")

	df.rename(columns={'Stn Id': 'StnId', 'Stn Name': 'StnName',
					   'PM ETo (mm)': 'ETo','Max Air Temp (C)': 'Max_Temp', 'Net Rad (W/sq.m)': 'NetRad',
					   'Min Air Temp (C)': 'Min_Temp','Avg Air Temp (C)': 'Avg_Temp','Avg Rel Hum (%)': 'RelHum_Avg'}, inplace=True)

	return df