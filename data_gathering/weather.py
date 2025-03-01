import ssl
import pandas as pd
import time

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

from datetime import datetime
from meteostat import Point, Hourly

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


from geopy.geocoders import Nominatim

# Initialize geolocator with a unique user agent
geolocator = Nominatim(user_agent="christopheramao@gmail.com")

def get_coordinates(city):
    time.sleep(1)
    location = geolocator.geocode(city, timeout=10)
    if location:
        return (location.latitude, location.longitude)
    else:
        return "City not found"

def get_weather(date_string, hour_time, abr_name):
    loc = get_coordinates(teams[abr_name]["city"])
    if loc == "City not found":
        return None  # Return None if city coordinates not found

    location = Point(*loc)

    # Set time period
    date_obj = datetime.strptime(f"{date_string} 2023", "%A, %b %d %Y")
    date_list = [date_obj.year, date_obj.month, date_obj.day, int(hour_time)]  
    time = datetime(*date_list)
    start = time
    end = time

    # Get hourly data
    data = Hourly(location, start, end)
    data = data.fetch()

    if not data.empty:
        temp = data['temp'].iloc[0]  # First row (since it's hourly)
        humidity = data['rhum'].iloc[0]
        wdir = data['wdir'].iloc[0] 
        prcp = data['prcp'].iloc[0]
        snow = data['snow'].iloc[0]
        wspd = data['wspd'].iloc[0]
        coco = data['coco'].iloc[0] / 27

        relative_wdir = (wdir - stadium_orientation[abr_name]) % 360
        return temp, humidity, relative_wdir, prcp, snow, wspd, coco
    else:
        return None  # If no data available for that time



if __name__ == '__main__':

    # Initialize weather_data DataFrame with all columns defined
    weather_data = pd.DataFrame(columns=[
        "Temperature (°C)", 
        "Humidity (%)", 
        "Relative Wind Direction (°)", 
        "Precipitation (mm)", 
        "Snow (mm)", 
        "Wind Speed (m/s)", 
        "COCO"
    ])

    # Add data for specific dates and teams
    weather_data.loc["Thursday, Mar 30"] = get_weather("Thursday, Mar 30", 19.0000, "NYY")
    weather_data.loc["Saturday, Apr 1"] = get_weather("Saturday, Apr 1", 7.4000, "NYY")

    print(weather_data)
