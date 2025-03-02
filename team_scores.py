import pandas as pd

df = pd.read_csv('datasets/concated_full_dataset.csv')

# Group by team and weather pattern
team_weather_stats = df.groupby(['Team', 'Weather Classified']).agg(
    offensive_score=('R', 'sum'),
    defensive_score=('RA', 'sum')
).reset_index()

# Print the results to see the offensive and defensive scores by weather pattern
print(team_weather_stats)

# Optional: Pivot the data if you want to see each team's offensive and defensive scores for each weather pattern
pivoted_stats = team_weather_stats.pivot(index='Team', columns='Weather Classified', values=['offensive_score', 'defensive_score'])

# Print the pivoted table to view the scores by weather pattern for each team
print(pivoted_stats)

team_weather_stats.to_csv('datasets/team_scores.csv', index=False)
pivoted_stats.to_csv('datasets/pivoted_team_score.csv', index=False)
