import pandas as pd

# Subway ridership for 5 stations on 10 different days
ridership_df = pd.DataFrame(
    data=[[0, 0, 2, 5, 0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [95, 229, 255, 496, 201],
          [2, 0, 1, 27, 0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
)


def mean_max_riders(data):
    '''
    find the station with the maximum riders on the
    first day, return the mean riders per day for that station and
    the mean ridership overall for comparsion.
    '''
    max_station = data.iloc[0].argmax()
    mean_for_max = data[max_station].mean()
    overall_mean = data.values.mean()

    return overall_mean, mean_for_max

print mean_max_riders(ridership_df)
