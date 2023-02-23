#Loading dependencies
import optuna

from .BaseMLModel import BaseMLModel
from .CatBoost import _log_hyperparameters
from .CatBoost import _construct_model
from .CatBoost import _construct_model_for_optimizer
from .CatBoost import train_model


class CatBoostModel(BaseMLModel):

	def __init__(self, **params):
		super().__init__(**params)

	def _construct_model(self, X_train, X_test, y_train, y_test):
		_log_hyperparameters(**self.__dict__)
		self.model = _construct_model(**self.__dict__)

	def _input_X_y(self, X_train, X_test, y_train, y_test):
		self.X_train, self.X_test, self.y_train, self.y_test = X_train, X_test, y_train, y_test

	def run(self, trial):
		self.model = _construct_model_for_optimizer(trial, **self.__dict__)
		self.mean_squared_error = train_model(**self.__dict__)
		return self.mean_squared_error

	def optimize(self, n_trials=5):
		study = optuna.create_study(direction='minimize')
		study.optimize(self.run, n_trials=5)    
		return study.best_trial