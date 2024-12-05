import os
import pandas as pd

data = pd.read_csv("files/weather_data.csv")

current_dir = os.path.dirname(os.path.abspath(__file__))

excel_path = os.path.join(current_dir,"files","weather_data.xlsx")

data.to_excel(excel_path,index=False)

print(f"Data has been successfully saved to {excel_path}")