from plots import plot_histogram
import pandas as pd

basic_path = 'datasets/ARI_dataset.csv'

columns = [
    "Temperature (°C)", 
    "Humidity (%)", 
    # "Relative Wind Direction (°)", 
    # "Precipitation (mm)", 
    # "Snow (mm)", 
    "Wind Speed (m/s)", 
    "COCO"
]

# Read the CSV file into a DataFrame
df = pd.read_csv(basic_path)

# Call the plot_histogram function, passing the DataFrame (df) and columns
plot_histogram(df, columns)
