from ._load_data_daily import _load_data_daily
from ._make_datetime_cols import _make_datetime_cols
from ._split_data import _split_data
from ._drop_nulls import _drop_nulls
from ._calculate_ETo import _calculate_ETo
from ._rename_cols import _rename_cols
from ._save_data import _save_data


class ApplyEmpiricalModels():

	def test_empirical_models(self, **params):

		df = _load_data_daily(**params)
		df = _make_datetime_cols(df, **params)
		df = _rename_cols(df, **params)
		df = _drop_nulls(df, **params)
		_save_data(df, **params)
		# _calculate_ETo(**params)
