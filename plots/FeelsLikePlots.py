from plots import plot_histogram
from weather_classification import calculate_feels_like
import pandas as pd

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
    # "WSN": {"team": "Washington Nationals", "city": "Washington, D.C."},
    # "WSH": {"team": "Washington Nationals", "city": "Washington, D.C."}
}


all_dataframes = []

# Iterate through each team name
for team in teams.keys():
    # Construct the file path by inserting the team name
    file_path = f'datasets/{team}_dataset.csv'
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Optionally, add a new column to identify the team (if you want)
    df['Team'] = team
    
    # Append the DataFrame to the list
    all_dataframes.append(df)

# Concatenate all the dataframes into one
df = pd.concat(all_dataframes, ignore_index=True)

columns = [
    "Temperature (°C)", 
    "Humidity (%)", 
    "Wind Speed (m/s)", 
    "Feels Like"
]

df['Feels Like'] = df.apply(lambda row: calculate_feels_like(row['Temperature (°C)'], row['Humidity (%)'], row['Wind Speed (m/s)']), axis=1)

percentiles = df['Feels Like'].quantile([0.25, 0.5, 0.75])

# Print the percentiles
print("25th, 50th, and 75th percentiles of 'Feels Like':")
print(percentiles)


# Call the plot_histogram function, passing the DataFrame (df) and columns
plot_histogram(df, columns)
