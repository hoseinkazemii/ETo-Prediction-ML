


def seasonal_split(df, **params):

    verbose = params.get("verbose")
    target_season = params.get("target_season")
    seasonal = params.get("seasonal")

    if seasonal:

        if verbose:
            print(f'Splitting data based on season. Target season is: {target_season}')


        # Subset data based on seasons

        if target_season == "Spring":
            df = df[(79<=df.Jul) & (df.Jul < 172)]

        elif target_season == "Summer":
            df = df[(172<=df.Jul) & (df.Jul < 265)]

        elif target_season == "Fall":
            df = df[(265<=df.Jul) & (df.Jul < 355)]

        elif target_season == "Winter":
            df = df[(355<=df.Jul) | (df.Jul < 79)]

        else:
            raise ValueError("Please choose a season among Winter, Spring, Summer, or Fall")

        return df

    else:
        return df