import pandas as pd

teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 
         'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR']

pd.set_option('display.max_columns', None)

# Load the dataset
df = pd.read_csv('datasets/team_scores.csv')

def find_best_weather_condition(team_abrv1, team_abrv2):
    # Get the data for each team
    team1_data = df[df['Team'] == team_abrv1]
    team2_data = df[df['Team'] == team_abrv2]
    
    # Merge the data on the Weather condition
    merged_data = pd.merge(team1_data[['Weather Classified', 'offensive_score', 'defensive_score']], 
                           team2_data[['Weather Classified', 'offensive_score', 'defensive_score']], 
                           on='Weather Classified', suffixes=('_team1', '_team2'))
    
    

    # Calculate the score difference for each weather condition
    merged_data['score_diff_team1'] = merged_data['offensive_score_team1'] - merged_data['defensive_score_team1']
    merged_data['score_diff_team2'] = merged_data['offensive_score_team2'] - merged_data['defensive_score_team2']
    
    # Calculate the net score for team1 (the difference we care about)
    # merged_data['net_score_team1'] = merged_data['score_diff_team1'] - merged_data['score_diff_team2']
    merged_data['net_score_team1'] = merged_data['offensive_score_team1'] + merged_data['defensive_score_team2'] - merged_data['offensive_score_team2'] - merged_data['defensive_score_team1']

    
    # Find the weather condition with the best score for team1
    best_weather = merged_data.loc[merged_data['net_score_team1'].idxmax(), 'Weather Classified']
    # print(merged_data)
    # Return the best weather condition
    return best_weather, merged_data['net_score_team1'].max()

def calculate_score(team_abrv):
    # Get the data for each team
    team1_data = df[df['Team'] == team_abrv]
    
    

    # Calculate the score difference for each weather condition
    team1_data['score_diff_team1'] = team1_data['offensive_score'] - team1_data['defensive_score']
    
    # Calculate the net score for team1 (the difference we care about)
    
    # Find the weather condition with the best score for team1
    # print(merged_data)
    # Return the best weather condition
    return team1_data['score_diff_team1']

if __name__ == '__main__':
    # home_team = "NYY"
    # for team in teams:
    #     if team != home_team:
    #         best_weather, score = find_best_weather_condition(home_team, team)
    #         worst_weather, neg_score = find_best_weather_condition(team, home_team)
    #         # print(f"The best weather condition for {home_team} to play against {team} is: {best_weather} and the predicted advantage is {score}")
    #         print(f"best weather condition ({team}): {best_weather} predicted advantage is {score / 100}")
    #         print(f"worst weather condition ({team}): {worst_weather} predicted disadvantage is -{neg_score / 100}")
    # calculate_score("SFG")
    print(calculate_score("OAK"))
    

