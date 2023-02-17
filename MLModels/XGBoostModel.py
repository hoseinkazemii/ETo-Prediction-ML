#Loading dependencies
from .BaseMLModel import BaseMLModel
from .XGBoost import _log_hyperparameters
from .XGBoost import _construct_model
from .XGBoost import train_model

class XGBoostModel(BaseMLModel):

	def __init__(self, **params):
		super().__init__(**params)

	def _construct_model(self, *args, **kwargs):
		_log_hyperparameters(**self.__dict__)
		self.model = _construct_model(**self.__dict__)

	def run(self, X_train, X_test, y_train, y_test, *args, **kwargs):		
		train_model(X_train, X_test, y_train, y_test, **self.__dict__)