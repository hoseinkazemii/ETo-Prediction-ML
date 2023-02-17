#Loading dependencies
from .BaseMLModel import BaseMLModel
from .Lasso import _log_hyperparameters
from .Lasso import _construct_model
from .Lasso import train_model

class LassoModel(BaseMLModel):

	def __init__(self, **params):
		super().__init__(**params)

	def _construct_model(self, *args, **kwargs):
		_log_hyperparameters(**self.__dict__)
		self.model = _construct_model(**self.__dict__)

	def run(self, X_train, X_test, y_train, y_test, *args, **kwargs):		
		train_model(X_train, X_test, y_train, y_test, **self.__dict__)