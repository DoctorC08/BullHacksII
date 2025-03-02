import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('datasets/concated_full_dataset.csv')

# Filter data for the team 'SFG' (San Francisco Giants)
sfg_data = df[df['Team'] == 'SFG']

# Create a plot showing Runs Scored (R) vs. Runs Allowed (RA) and color by weather condition
plt.figure(figsize=(12, 6))

# Create a scatter plot with color-coded points based on the weather classification
sns.scatterplot(data=sfg_data, x='R', y='RA', hue='Weather Classified')

# Adding titles and labels
plt.title('San Francisco Giants: Runs Scored vs. Runs Allowed by Weather Condition', fontsize=16)
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
