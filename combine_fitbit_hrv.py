import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Define the folder path
folder_path = "takeout/Fitbit/Heart Rate Variability"

# Find all CSV files in the folder

csv_files = glob.glob(os.path.join(folder_path, "Daily Heart Rate Variability Summary*.csv"))
# Initialize an empty list to store DataFrames
dfs = []

# Read each CSV file and append it to the list
for file in csv_files:
    df = pd.read_csv(file)
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.date  # Convert to date only
    dfs.append(df)

# Combine all DataFrames
if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Sort by date
    combined_df = combined_df.sort_values(by="timestamp")

    # Save to a new CSV
    combined_df.to_csv("combined/combined_hrv_data.csv", index=False)
    print(f"Successfully merged {len(csv_files)} files into 'combined_hrv_data.csv'.")
else:
    print("No matching files found.")
