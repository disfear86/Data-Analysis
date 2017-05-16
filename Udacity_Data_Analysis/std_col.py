import pandas as pd

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)


def std_one(col):
    return (col - col.mean()) / col.std()


def standardize(df):
    '''
    standardize each column of the DataFrame.
    '''
    return df.apply(std_one)

print standardize(grades_df)
