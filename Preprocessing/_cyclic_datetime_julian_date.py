import numpy as np

def _cyclic_datetime_julian_date(df, col):

    df[col + '_sin'] = np.sin(2 * np.pi * df[col]/365)
    # df[col + '_cos'] = np.cos(2 * np.pi * df[col]/365)

    return df