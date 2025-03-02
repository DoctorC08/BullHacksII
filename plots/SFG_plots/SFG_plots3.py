import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import gaussian_kde

df = pd.read_csv('datasets/concated_full_dataset.csv')

# Filter data for the team 'SFG' (San Francisco Giants)
sfg_data = df[df['Team'] == 'SFG']

# Create the plot with subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Plot Density for Runs Scored (R)
sns.kdeplot(data=sfg_data, x='R', hue='Weather Classified', fill=True, common_norm=False, ax=axes[0], palette='Set2')
axes[0].set_title('Density Distribution of Runs Scored (R) by Weather Condition', fontsize=14)
axes[0].set_xlabel('Runs Scored (R)', fontsize=12)
axes[0].set_ylabel('Density', fontsize=12)

# Plot Density for Runs Allowed (RA)
sns.kdeplot(data=sfg_data, x='RA', hue='Weather Classified', fill=True, common_norm=False, ax=axes[1], palette='Set2')
axes[1].set_title('Density Distribution of Runs Allowed (RA) by Weather Condition', fontsize=14)
axes[1].set_xlabel('Runs Allowed (RA)', fontsize=12)
axes[1].set_ylabel('Density', fontsize=12)

# Show the plot with appropriate layout
plt.tight_layout()
plt.show()
