from ._load_data import load_data
from ._rename_drop_cols import rename_drop_cols
from ._groupby_date import groupby_date
from ._make_datetime_cols import make_datetime_cols
from ._split_data_and_deal_with_zeros import split_data_and_deal_with_zeros
from ._scaler import scaler
from ._save_X_y import save_X_y

import numpy as np


class PreprocessData():

	def preprocess_and_save_data(self, **params):

		# One-time Run-1:
		# df = load_data(**params)
		# df = rename_drop_cols(df, **params)
		# df = groupby_date(df, **params)
		# df = make_datetime_cols(df, **params)

		# Run-2:
		X_train, X_test, y_train, y_test = split_data_and_deal_with_zeros(**params)
		X_train, X_test = scaler(X_train, X_test, y_train, y_test, **params)
		save_X_y(X_train, X_test, y_train, y_test, **params)