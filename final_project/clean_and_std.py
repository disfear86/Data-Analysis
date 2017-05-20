import pandas as pd


def standarize(data):
    ''' Return correlated data of each input.'''
    return (data - data.mean()) / data.std()


def clean_std(df1, df2, key1, key2, key3):
    ''' Return new cleaned and correlated dataframe
        of the two input dataframes.'''
    # merge input dataframes
    stats = df1.merge(df2, on=key1, how='inner')
    # create new dataframe with the three input keys as columns
    stats_clear = pd.DataFrame(data={key1: stats[key1].values,
                                     key2: stats[key2].values,
                                     key3: stats[key3].values
                                     })
    # update dataframe with mean values
    stats_clear_mean = stats_clear.groupby(key1, as_index=False).mean()
    # remove key1 column so to keep only numerical data
    del_id = stats_clear_mean.drop(key1, 1)
    # use apply method to return correlated dataframe
    stats_std = del_id.apply(standarize)
    return stats_std
