
from tqdm import tqdm
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
    print(team)