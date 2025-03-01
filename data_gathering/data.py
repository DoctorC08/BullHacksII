import pandas as pd
import pybaseball as pyball
import warnings # removing extra warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from tqdm import tqdm

from weather import get_weather
from data_cleaning import clean_data

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def time_to_decimal(time_str):
    # Split time into hours and minutes
    hours, minutes = map(int, time_str.split(':'))
    # Convert minutes to a fraction of an hour and add to hours
    return hours + (minutes / 60)


def gather_team_data(team_abrv):
    data = pd.DataFrame(pyball.batting_stats(2023).columns)
    data = pyball.schedule_and_record(2023, team)
    data['Time'] = data['Time'].apply(time_to_decimal)

    data = clean_data(data)

    columns=[
            "Temperature (°C)", 
            "Humidity (%)", 
            "Relative Wind Direction (°)", 
            "Precipitation (mm)", 
            "Snow (mm)", 
            "Wind Speed (m/s)", 
            "COCO"
        ]
    data[columns] = data.apply(
        lambda row: get_weather(row['Date'], row['Time'], row['Tm'] if row['Home_Away'] == 'Home' else row['Opp']), 
        axis=1, 
        result_type="expand")
    # print(data.head(20))
    data.to_csv(f'datasets/{team}_dataset.csv', index=False)


teams = {
    "ARI": {"team": "Arizona Diamondbacks", "city": "Phoenix, AZ"},
    "ATL": {"team": "Atlanta Braves", "city": "Atlanta, GA"},
    "BAL": {"team": "Baltimore Orioles", "city": "Baltimore, MD"},
    "BOS": {"team": "Boston Red Sox", "city": "Boston, MA"},
    "CHC": {"team": "Chicago Cubs", "city": "Chicago, IL"},
    "CHW": {"team": "Chicago White Sox", "city": "Chicago, IL"},
    "CIN": {"team": "Cincinnati Reds", "city": "Cincinnati, OH"},
    "CLE": {"team": "Cleveland Indians", "city": "Cleveland, OH"},
    "COL": {"team": "Colorado Rockies", "city": "Denver, CO"},
    "DET": {"team": "Detroit Tigers", "city": "Detroit, MI"},
    "HOU": {"team": "Houston Astros", "city": "Houston, TX"},
    "KCR": {"team": "Kansas City Royals", "city": "Kansas City, MO"},
    "LAA": {"team": "Los Angeles Angels", "city": "Anaheim, CA"},
    "LAD": {"team": "Los Angeles Dodgers", "city": "Los Angeles, CA"},
    "MIA": {"team": "Miami Marlins", "city": "Miami, FL"},
    "MIL": {"team": "Milwaukee Brewers", "city": "Milwaukee, WI"},
    "MIN": {"team": "Minnesota Twins", "city": "Minneapolis, MN"},
    "NYM": {"team": "New York Mets", "city": "New York, NY"},
    "NYY": {"team": "New York Yankees", "city": "New York, NY"},
    "OAK": {"team": "Oakland Athletics", "city": "Oakland, CA"},
    "PHI": {"team": "Philadelphia Phillies", "city": "Philadelphia, PA"},
    "PIT": {"team": "Pittsburgh Pirates", "city": "Pittsburgh, PA"},
    "SDP": {"team": "San Diego Padres", "city": "San Diego, CA"},
    "SFG": {"team": "San Francisco Giants", "city": "San Francisco, CA"},
    "SEA": {"team": "Seattle Mariners", "city": "Seattle, WA"},
    "STL": {"team": "St. Louis Cardinals", "city": "St. Louis, MO"},
    "TBR": {"team": "Tampa Bay Rays", "city": "St. Petersburg, FL"},
    "TEX": {"team": "Texas Rangers", "city": "Arlington, TX"},
    "TOR": {"team": "Toronto Blue Jays", "city": "Toronto, ON"},
    "WSH": {"team": "Washington Nationals", "city": "Washington, D.C."}
}

for team in tqdm(teams.keys()):
    gather_team_data(team)