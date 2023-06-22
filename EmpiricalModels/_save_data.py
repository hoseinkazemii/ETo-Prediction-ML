


def _save_data(df, **params):

	verbose = params.get("verbose")

	if verbose:
		print("Saving the test dataset for empirical models...")

	df = df[df['Year'] >= 2018]

	# df.drop('Date', axis=1, inplace=True)

	df.sort_values(by=['StnId', 'Year', 'Month', 'Day'], axis=0, ascending=[True,True,True,True], inplace=True)

	df.to_csv('./Data/Final_Dataset/' + 'final_dataset.csv', index=False)