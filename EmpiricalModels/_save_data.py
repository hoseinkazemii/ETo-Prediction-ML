


def _save_data(df, **params):

	verbose = params.get("verbose")

	if verbose:
		print("Saving the test dataset for empirical models...")

	df.to_csv('./Data/Final_Dataset/' + 'final_dataset.csv', index=False)