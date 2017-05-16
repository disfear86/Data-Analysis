import pandas as pd

subway_df = pd.read_csv('nyc_subway_weather.csv')


def correlation(x, y):
    '''
    computes correlation between two
    variables.
    '''
    x_std = (x - x.mean()) / x.std(ddof=0)
    y_std = (y - y.mean()) / y.std(ddof=0)

    correl = (x_std * y_std).mean()
    return correl



if __name__ == "__main__":

    entries = subway_df['ENTRIESn_hourly']
    cumulative_entries = subway_df['ENTRIESn']
    rain = subway_df['meanprecipi']
    temp = subway_df['meantempi']

    print correlation(entries, rain)
    print correlation(entries, temp)
    print correlation(rain, temp)
    print correlation(entries, cumcumulative_entries)
