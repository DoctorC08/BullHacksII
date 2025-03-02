import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import gaussian_kde

df = pd.read_csv('datasets/concated_full_dataset.csv')

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

# Create the plot with varying point sizes
plt.figure(figsize=(12, 6))

# Scatter plot with point sizes based on density
sns.scatterplot(data=sfg_data, x='R', y='RA', hue='Weather Classified', 
                size=point_sizes, sizes=(20, 200))

pd.set_option('display.max_columns', None)

print(sfg_data.head)

# Adding titles and labels
plt.title('San Francisco Giants: Runs Scored vs. Runs Allowed by Weather Condition (Density-based Sizes)', fontsize=16)
plt.xlabel('Runs Scored (R)', fontsize=12)
plt.ylabel('Runs Allowed (RA)', fontsize=12)

# Optional: Rotate x and y axis labels for better readability
plt.xticks(rotation=45)
plt.yticks(rotation=45)

# Show the legend with weather classification labels
plt.legend(title='Weather Condition')

# Show the plot
plt.tight_layout()
plt.show()
