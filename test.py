import pandas as pd
import pybaseball as pyball
import warnings # removing extra warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
    
# data = pd.DataFrame(pyball.team_batting(2023).columns)
# data = pd.DataFrame(pyball.team_batting(2023).columns)
data = pd.DataFrame(pyball.schedule_and_record(2023, "NYY"))



# data = pyball.team_batting(2023)
print(data.head)