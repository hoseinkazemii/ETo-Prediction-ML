from .BaseMLModel import BaseMLModel
from .DNN import _log_hyperparameters
from .DNN import _construct_model
from .DNN import train_model

class DNNModel(BaseMLModel):

	def __init__(self, **params):
		super().__init__(**params)

	def _construct_model(self, X_train):
		_log_hyperparameters(**self.__dict__)
		self.model = _construct_model(X_train, **self.__dict__)

	def run(self, X_train, X_test, y_train, y_test):
		self.history = train_model(X_train, X_test, y_train, y_test, **self.__dict__)