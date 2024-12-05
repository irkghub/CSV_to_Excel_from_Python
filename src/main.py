import os
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir,"files","csv_file","weather_data.csv")

# Read CSV file into a dataframe now
data = pd.read_csv(csv_file_path)
excel_file_path = os.path.join(current_dir,"files","excel_file","data.xlsx")
data.to_excel(excel_file_path,"excel_file",index=False)

print(f"Data has been successfully saved to {excel_file_path}")