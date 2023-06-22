from ._load_data import load_data
from ._rename_drop_cols import rename_drop_cols
from ._groupby_date import groupby_date
from ._handle_zeros import handle_zeros
from ._calculate_daily_Rso import calculate_daily_Rso
from ._load_data_for_X_y import load_data_for_X_y
from ._seasonal_split import seasonal_split
from ._split_data import split_data
from ._scaler import scaler
from ._save_X_y import save_X_y

import numpy as np


class PreprocessData():

	def preprocess_and_save_data(self, **params):

		# One-time Run-1:
		# df = load_data(**params)
		# df = rename_drop_cols(df, **params)
		# df = groupby_date(df, **params)
		# df = calculate_daily_Rso(df, **params)

		# Run-2:
		df = load_data_for_X_y(**params)
		df = seasonal_split(df, **params)
		df = handle_zeros(df, **params)
		X_train, X_test, y_train, y_test = split_data(df, **params)
		X_train, X_test = scaler(X_train, X_test, y_train, y_test, **params)
		save_X_y(X_train, X_test, y_train, y_test, **params)