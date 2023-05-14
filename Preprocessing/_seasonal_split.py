


def _seasonal_split(df_test, **params):

    verbose = params.get("verbose")
    target_season = params.get("target_season")


    if verbose:
        print(f'Splitting data based on season. Target season is: {target_season}')


    # Subset data based on seasons

    if target_season == "Spring":
        df_test = df_test[(79<=df_test.Jul) & (df_test.Jul < 172)]

    elif target_season == "Summer":
        df_test = df_test[(172<=df_test.Jul) & (df_test.Jul < 265)]

    elif target_season == "Fall":
        df_test = df_test[(265<=df_test.Jul) & (df_test.Jul < 355)]

    elif target_season == "Winter":
        df_test = df_test[(355<=df_test.Jul) | (df_test.Jul < 79)]

    else:
        raise ValueError("Please choose a season among Winter, Spring, Summer, or Fall")


    return df_test