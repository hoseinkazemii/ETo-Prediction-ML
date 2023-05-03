import pickle


def save_X_y(X_train, X_test, y_train, y_test, **params):
    verbose = params.get("verbose")

    if verbose:
        print("Saving X and ys...")

    dict_tmp = {"X_train": X_train, "X_test": X_test, "y_train": y_train, "y_test": y_test}

    with open('./Data/X_y/X_ys.pickle', 'wb') as f:
        pickle.dump(dict_tmp, f)