import pickle


def load_X_y(**params):
    verbose = params.get("verbose")
    
    if verbose:
        print("Loading X and ys...")


    with open('./Data/X_y/X_ys.pickle', 'rb') as f:
        dataset_dict = pickle.load(f)


    X_train, X_test, y_train, y_test = \
        dataset_dict["X_train"], dataset_dict["X_test"],\
        dataset_dict["y_train"], dataset_dict["y_test"]

    return X_train, X_test, y_train, y_test