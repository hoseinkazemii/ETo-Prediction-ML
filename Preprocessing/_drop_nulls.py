
def _drop_nulls(df, col, **params):
	df = df[df[col].notna()]

	return df