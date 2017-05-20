import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from clean_and_std import clean_std

# load csv files
players = pd.read_csv('Master.csv')
hall_of_fame = pd.read_csv('HallOfFame.csv')
salaries = pd.read_csv('Salaries.csv')
batting = pd.read_csv('Batting.csv')


# eliminate stats for players with low batting stats(i.e. pitchers)
batting = batting[batting['RBI'] > 15]

# player born after 1980 dataframe
after_1980 = players[players['birthYear'] > 1980]
# merge with salaries dataframe
after_1980_salaries = after_1980.merge(salaries, on='playerID', how='left')
# extract the top paid 15%
top15 = after_1980_salaries[after_1980_salaries.salary > after_1980_salaries.salary.quantile(.85)]

top_stats = clean_std(top15, batting, 'playerID', 'salary', 'RBI')
# add Hall of Fame boolean column
top_stats['HallOfFame'] = pd.Series([False] * len(top_stats['salary']), dtype=bool)


# hall of fame players
hall_salaries = hall_of_fame.merge(salaries, on='playerID', how='inner')
hall_stats = clean_std(hall_salaries, batting, 'playerID', 'salary', 'RBI')
# add Hall of Fame boolean column
hall_stats['HallOfFame'] = pd.Series([True] * len(hall_stats['salary']), dtype=bool)

# combine dataframes
combine = top_stats.merge(hall_stats, how='outer')
