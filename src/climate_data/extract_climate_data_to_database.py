import pandas as pd
from itertools import product
from tqdm import tqdm
import sqlalchemy as sql
import matplotlib.pyplot as plt


pd.set_option('future.no_silent_downcasting', True)


furl = 'https://en.tutiempo.net/climate/{:02d}-{:d}/ws-726452.html'

months = [x for x in range(1, 13)]
years = [x for x in range(2023, 2025)]


print('Scraping and cleaning web data...')
# tables = [pd.read_html(furl.format(month, year))[0] for year, month in tqdm(product(years, months))]
tables = []
for year, month in tqdm(product(years, months)):
    table = pd.read_html(furl.format(month, year))[0]

    # Remove the monthly statistical rows at the bottom.
    table = table[:-2]

    # Clean up invalid values and convert to numeric datatypes.
    table.replace(['-'], pd.NA, inplace=True)
    table.replace(['o'], 1, inplace=True)
    table[table.columns[-4:]] = table[table.columns[-4:]].fillna(0)
    table[table.columns[-4:]] = table[table.columns[-4:]].astype('int64')
    table = table.apply(pd.to_numeric)
    
    # Add a date column for sorting with other months.
    table['date'] = pd.to_datetime(table['Day'].apply(lambda day: f'{year}-{month:02d}-{day:02d}'))

    tables.append(table)

print('done.\n')

# Combine each month's tables into one table.
data_table = pd.concat(tables, ignore_index=True)

# Rename the columns.
data_table = data_table.rename(
    columns={
        'Day':'day',
        'T':'temp_avg_c',
        'TM':'temp_max_c',
        'Tm':'temp_min_c',
        'SLP':'atmospheric_pressure_at_sea_lvl_hpa',
        'H':'rel_humidity_avg_percent',
        'PP':'total_rainfall_or_snow_melt',
        'VV':'visibility_avg_km',
        'V':'wind_speed_avg_km_p_hr',
        'VM':'sustained_wind_speed_max_km_p_hr',
        'VG':'wind_speed_max_km_p_hr',
        'RA':'did_it_rain',
        'SN':'did_it_snow',
        'TS':'did_it_storm',
        'FG':'was_there_fog',
    }
)

# Reorder the columns.
columns = ['date'] + [column for column in data_table.columns if column != 'date']
data_table = data_table[columns]

# Save to a SQL database.
engine = sql.create_engine('sqlite:///data/database.db')
data_table.to_sql('Climate', con=engine, index=False, if_exists='replace')

# Plot the data.
# data_table.plot(x='Date', y='T')
# plt.title('Average Temperature (C)')
# plt.xlabel('Date')
# plt.ylabel('Avg Temp (C)')
# plt.tight_layout()

# plt.show()