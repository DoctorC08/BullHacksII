import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('datasets/team_scores.csv')

# Create the jointplot with scatter and marginal density plots
sns.jointplot(x='offensive_score', y='defensive_score', data=df, kind='scatter', hue='Weather Classified', palette='viridis', marginal_kws={'fill': True})

# Plot the line y = x
x_values = np.linspace(min(df['offensive_score'].min(), df['defensive_score'].min()), max(df['offensive_score'].max(), df['defensive_score'].max()), 100)
plt.plot(x_values, x_values, color='blue', linestyle='--', label='$y=x$')

# Add labels and title
plt.suptitle('Offensive vs Defensive Scores with Weather Distribution', y=1.02)
plt.xlabel('Offensive Score')
plt.ylabel('Defensive Score')

# Show the plot
plt.show()
