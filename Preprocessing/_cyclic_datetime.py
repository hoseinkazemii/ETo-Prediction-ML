import numpy as np

def _cyclic_datetime(df, col, max_val):

    df[col + '_sin'] = np.sin(2 * np.pi * df[col]/max_val)
    df[col + '_cos'] = np.cos(2 * np.pi * df[col]/max_val)

    return df