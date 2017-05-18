import pandas as pd

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)


def standardize(df):
    '''
    standardize each column of DataFrame.
    '''

    return (df - df.mean()) / df.std(ddof=0)


def standardize_rows(df):
    '''
    standardize each row of DataFrame
    '''
    std = df.sub(df.mean(axis='columns'), axis='index')
    correl = std.div(df.std(axis='columns'), axis='index')
    return correl

print standardize(grades_df)
print
print standardize_rows(grades_df)
