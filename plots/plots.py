import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_columns(df, column1, column2):
    """
    Plots two columns from a pandas DataFrame with seaborn styling.

    Parameters:
    - df: The pandas DataFrame containing the data.
    - column1: The name of the first column to plot.
    - column2: The name of the second column to plot.
    """
    # Check if the columns exist in the DataFrame
    if column1 not in df.columns or column2 not in df.columns:
        raise ValueError(f"Columns {column1} or {column2} do not exist in the DataFrame.")
    
    # Set the seaborn style for better aesthetics
    sns.set(style="whitegrid")

    # Create the plot using seaborn
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x=column1, y=column2, marker='o', color='b')

    # Add titles and labels
    plt.title(f"Plot of {column2} vs {column1}", fontsize=16)
    plt.xlabel(column1, fontsize=14)
    plt.ylabel(column2, fontsize=14)
    
    # Display the plot
    plt.show()


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_histogram(df, columns):
    """
    Plots the frequency distributions of weather-related variables provided in the columns list.
    
    Parameters:
    - df: pandas DataFrame containing the weather data.
    - columns: List of column names to plot the frequency distributions.
    """
    # Set the seaborn style for better aesthetics
    sns.set_theme(style="whitegrid")

    if "COCO" in df.columns:
        df["COCO"] = df["COCO"] * 27
    
    # Determine the number of rows and columns for subplots based on the number of variables
    n_cols = 2  # Keep two columns for the layout
    n_rows = (len(columns) + 1) // n_cols  # Calculate the number of rows needed to fit the subplots
    if len(columns) % n_cols != 0:
        n_rows += 1  # Ensure there's an extra row if the number of columns is odd

    # Create a figure with subplots based on the number of variables
    fig, axs = plt.subplots(n_rows, n_cols, figsize=(8, 4 * n_rows))
    
    # Flatten the axs array in case there are more than 2 columns for easier indexing
    axs = axs.flatten()

    # Plot each column in the list
    for i, col in enumerate(columns):
        ax = axs[i]
        
        # Check for missing values in the column
        if df[col].isnull().any():
            print(f"Warning: {col} contains missing values. These will be ignored in the plot.")
        
        # Plot based on data type (categorical or continuous)
        if df[col].dtype == 'object' or df[col].dtype.name == 'category':
            # Use countplot for categorical data
            sns.countplot(data=df, x=col, ax=ax, color='tab:blue')
            ax.set_title(f'{col} Frequency')
            ax.set_xlabel(col)
            ax.set_ylabel('Count')
        else:
            # Use histogram for continuous data
            sns.histplot(df[col], kde=True, ax=ax, color='tab:blue', bins=10)
            ax.set_title(f'{col} Distribution')
            ax.set_xlabel(col)
            ax.set_ylabel('Frequency')
    
    # Turn off unused subplots (if any)
    for i in range(len(columns), len(axs)):
        axs[i].axis('off')

    # Adjust layout to prevent overlap
    plt.tight_layout()

    plt.subplots_adjust(hspace=0.5, wspace=0.3)

    # Display the plot
    plt.show()


# Example usage:
# Assuming 'df' is your DataFrame with the weather data
# columns = ['Temperature', 'Humidity', 'Precipitation', 'WindSpeed', 'WindDirection']
# plot_weather_frequencies(df, columns)
