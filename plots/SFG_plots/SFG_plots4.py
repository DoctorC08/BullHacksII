import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import gaussian_kde

from plots.weather_classification import classify_weather, classify_weather2
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

all_teams = list(teams.keys())

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
    "Weather Classified"
]

df['Weather Classified'] = df.apply(lambda row: classify_weather(row['Temperature (°C)'], row['Humidity (%)'], row['Wind Speed (m/s)']), axis=1)


# Filter data for the team 'SFG' (San Francisco Giants)
sfg_data = df[df['Team'] == 'SFG']

# Extract the 'R' and 'RA' columns
runs_scored = sfg_data['R']
runs_allowed = sfg_data['RA']

# Use Gaussian KDE to calculate point density
xy = np.vstack([runs_scored, runs_allowed])
kde = gaussian_kde(xy)
density = kde(xy)

# Normalize density values to control point size
min_density = min(density)
max_density = max(density)
size_factor = 500  # Adjust the size factor for scaling
point_sizes = size_factor * (density - min_density) / (max_density - min_density)  # Normalize and scale the sizes

# Create the joint plot with scatter and marginal KDE plots
g = sns.jointplot(data=sfg_data, x='R', y='RA', hue='Weather Classified', kind='scatter', palette='Set2',
                  height=8, marker='o', marginal_kws={'fill': True})

# Scatter plot point sizes based on density
g.ax_joint.scatter(runs_scored, runs_allowed, s=point_sizes, color=g.ax_joint.collections[0].get_facecolor(), edgecolors='black', alpha=0.7)

# Add titles and labels
g.figure.suptitle('San Francisco Giants: Runs Scored vs. Runs Allowed by Weather Condition', fontsize=16)
g.set_axis_labels('Runs Scored (R)', 'Runs Allowed (RA)', fontsize=12)

g.ax_joint.set_xlim(left=0)
g.ax_joint.set_ylim(bottom=0)

# Show the plot
plt.tight_layout()
plt.show()
