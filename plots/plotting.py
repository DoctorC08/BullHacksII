from plots import plot_histogram
import pandas as pd

basic_path = 'datasets/concated_full_dataset.csv'

columns = [
    "Temperature (°C)", 
    "Humidity (%)", 
    "Relative Wind Direction (°)", 
    # "Precipitation (mm)", 
    # "Snow (mm)", 
    "Wind Speed (m/s)", 
    # "COCO"
]


# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# Read the CSV file into a DataFrame
df = pd.read_csv(basic_path)
# print(df.columns)

# Call the plot_histogram function, passing the DataFrame (df) and columns
plot_histogram(df, columns)
