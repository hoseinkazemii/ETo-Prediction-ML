import optuna


class Optimizer(param_dict, model, X_train, X_test, y_train, y_test):
    
    def __init__(self, param_dict, model, X_train, X_test, y_train, y_test):

        self.model = model
        self.param_dict = param_dict
        self.X_train, self.X_test, self.y_train, self.y_test = X_train, X_test, y_train, y_test
        
    def optimization_function(self, trial):

        self.dtrain = lgb.Dataset(self.X_train, label=self.y_train)
        gbm = lgb.train(param, dtrain)
        
        preds = gbm.predict(self.X_test)
        pred_labels = np.rint(preds)
        accuracy = sklearn.metrics.accuracy_score(self.y_test, pred_labels)
        return accuracy
    
    
    def optimize(self, direction, n_trials):

        study = optuna.create_study(direction=direction)
        study.optimize(self.optimization_function, n_trials=n_trials)    
        return study.best_trial