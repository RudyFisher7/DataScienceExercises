import pandas as pd
import sqlalchemy as sql


engine = sql.create_engine('sqlite:///data/database.db')
data_table = pd.read_sql_table('Climate', con=engine)

# Filter to make a table of each season.
spring_climate = data_table[data_table['date'].dt.month.isin([x for x in range(3, 6)])]
summer_climate = data_table[(data_table['date'].dt.month > 5) & (data_table['date'].dt.month < 9)]
autumn_climate = data_table[data_table['date'].dt.month.isin([x for x in range(9, 12)])]
winter_climate = data_table[data_table['date'].dt.month.isin([12, 1, 2])]

seasons = [spring_climate, summer_climate, autumn_climate, winter_climate]

# Get some statistics about each season.
mean_temps = [season['temp_avg_c'].mean() for season in seasons]
max_temps = [season['temp_max_c'].max() for season in seasons]
min_temps = [season['temp_min_c'].min() for season in seasons]
print(mean_temps)
print(max_temps)
print(min_temps)

# Add a month column for grouping.
data_table['month'] = data_table['date'].dt.month

# Get the mean of average temperature in each month across the years.
monthly_means = data_table.groupby('month')['temp_avg_c'].mean()
print(monthly_means)