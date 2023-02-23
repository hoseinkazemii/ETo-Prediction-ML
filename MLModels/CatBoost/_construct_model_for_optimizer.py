from catboost import CatBoostRegressor
import optuna


def _construct_model_for_optimizer(trial, **params):

	iterations = params.get("iterations")
	learning_rate = params.get("learning_rate")
	depth = params.get("depth")
	l2_leaf_reg = params.get("l2_leaf_reg")
	loss_function = params.get("loss_function")
	allow_writing_files = params.get("allow_writing_files")
	eval_metric = params.get("eval_metric")
	task_type = params.get("task_type")
	random_seed = params.get("random_seed")
	verbose_cb = params.get("verbose_cb")
	boosting_type = params.get("boosting_type")
	thread_count = params.get("thread_count")


	param = {"iterations" : trial.suggest_int("iterations", iterations[0], iterations[1]),
	"learning_rate" : trial.suggest_float("learning_rate", learning_rate[0], learning_rate[1], log=True),
	"depth" : trial.suggest_int("depth", depth[0], depth[1]),
	"l2_leaf_reg" : l2_leaf_reg,
	"allow_writing_files" : allow_writing_files,
	"eval_metric" : eval_metric,
	"task_type" : task_type,
	"random_seed" : random_seed,
	"verbose" : verbose_cb,
	"boosting_type" : trial.suggest_categorical("boosting_type", boosting_type),
	"thread_count" : thread_count,
	}


	model = CatBoostRegressor(**param)

	return model