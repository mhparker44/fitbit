import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Define the folder path
folder_path = "takeout/Fitbit/Heart Rate Variability"

# Find specifically named CSV files in the folder

csv_files = glob.glob(os.path.join(folder_path, "Daily Heart Rate Variability Summary*.csv"))
# Initialize an empty list to store DataFrames
dfs = []

# Read each CSV file and append it to the list
for file in csv_files:
    df = pd.read_csv(file)
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.date  # Convert to date only
    dfs.append(df)

# Combine all DataFrames
combined_df = pd.concat(dfs, ignore_index=True)

# Sort by date
combined_df = combined_df.sort_values(by="timestamp")

# Save to a new CSV
combined_df.to_csv("combined_hrv_data.csv", index=False)

# Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(combined_df["timestamp"], combined_df["rmssd"], label="RMSSD", alpha=0.6)
plt.scatter(combined_df["timestamp"], combined_df["nremhr"], label="NREM HR", alpha=0.6)
plt.scatter(combined_df["timestamp"], combined_df["entropy"], label="Entropy", alpha=0.6)
plt.xlabel("Date")
plt.ylabel("Values")
plt.title("Heart Rate Variability Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.show()
