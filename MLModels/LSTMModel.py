from .BaseMLModel import BaseMLModel
from .LSTM import _log_hyperparameters
from .LSTM import _construct_model
from .LSTM import train_model
from .LSTM import plot

class LSTMModel(BaseMLModel):

	def __init__(self, **params):
		super().__init__(**params)

	def _construct_model(self, df, X_train, **params):
		_log_hyperparameters(**self.__dict__)
		self.model = _construct_model(df, X_train, **self.__dict__)

	def run(self, X_train, X_test, y_train, y_test, **params):		
		self.history = train_model(X_train, X_test, y_train, y_test, **self.__dict__)
		plot(**self.__dict__)
