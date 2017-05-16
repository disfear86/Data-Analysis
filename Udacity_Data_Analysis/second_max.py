import numpy as np
import pandas as pd

df = pd.DataFrame({
    'a': [4, 5, 3, 1, 2],
    'b': [20, 10, 40, 50, 30],
    'c': [25, 20, 5, 15, 10]
})

def second(col):
    sort_col = col.sort_values(ascending=False)
    return sort_col.iloc[1]


def second_largest(df):
    '''
    returns the second-largest value of each
    column of the DataFrame.
    '''

    return df.apply(second)

print second_largest(df)
