import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matchups import find_best_weather_condition

teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 
         'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR']

home_team = "SFG"
best_weather_data = []
worst_weather_data = []

for team in teams:
    if team != home_team:
        best_weather, merged_data = find_best_weather_condition(home_team, team)
        worst_weather, neg_merged_data = find_best_weather_condition(team, home_team)
        
        best_weather_data.append({
            'team': team,
            'weather_condition': best_weather,
            'predicted_advantage': merged_data / 100
        })
        
        worst_weather_data.append({
            'team': team,
            'weather_condition': worst_weather,
            'predicted_disadvantage': -neg_merged_data / 100
        })

# Convert the lists to DataFrames
best_weather_df = pd.DataFrame(best_weather_data)
worst_weather_df = pd.DataFrame(worst_weather_data)

# Merge DataFrames
weather_df = pd.merge(best_weather_df, worst_weather_df, on='team')

# Create Stacked Bar Plot
plt.figure(figsize=(14, 8))

sns.barplot(x='team', y='predicted_advantage', data=weather_df, color='midnightblue', alpha=0.8, label='Best Weather')
sns.barplot(x='team', y='predicted_disadvantage', data=weather_df, color='firebrick', alpha=0.7, label='Worst Weather')

# Add Horizontal Line at y=0
plt.axhline(0, color='black', linewidth=1)

# Improve Readability
plt.xticks(rotation=45, ha='right')
plt.title(f"Best and Worst Weather Conditions for {home_team} Against Other Teams")
plt.xlabel('Teams')
plt.ylabel('Predicted Advantage/Disadvantage')

# Improve Legend Placement
plt.legend(title='Weather Impact', loc='upper left', bbox_to_anchor=(1,1))

plt.tight_layout()
plt.show()
