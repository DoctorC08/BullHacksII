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
    "WSN": {"team": "Washington Nationals", "city": "Washington, D.C."},
    "WSH": {"team": "Washington Nationals", "city": "Washington, D.C."}
}

stadium_orientation = {
    "ARI": 359.7491679,
    "ATL": 157.64687,
    "BAL": 31.33978546,
    "BOS": 44.17424096,
    "CHC": 37.61572884,
    "CIN": 122.3427354,
    "CLE": 359.2547923,
    "COL": 4.962490772,
    "CHW": 127.0606723,
    "DET": 151.2270493,
    "HOU": 343.1738414,
    "KCR": 46.71018194,
    "LAA": 44.17136547,
    "LAD": 26.4845402,
    "MIA": 128.1321885,
    "MIL": 128.8537047,
    "MIN": 90.50394579,
    "NYM": 13.99114182,
    "NYY": 75.61766684,
    "OAK": 54.51116326,
    "PHI": 10.07051968,
    "PIT": 116.5764243,
    "SDP": 359.7374753,
    "SEA": 49.30884076,
    "SFG": 85.1519466,
    "STL": 62.69629144,
    "TBR": 49,
    "TEX": 32.80283371,
    "TOR": 344.0904107,
    "WSN": 28.94819353, 
    "WSH": 28.94819353
}

def clean_data(data):
    # cleaning dates
    date_pattern = r'^[A-Za-z]+, [A-Za-z]{3} \d{1,2}$'
    data = data[data['Date'].str.match(date_pattern)]

    # Checking keys
    if not data['Tm'].isin(teams.keys()).all():
        print("not all teams in keys...")
        raise Exception
    

    return data