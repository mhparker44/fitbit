import pandas as pd
import glob
import os

# Define the folder path

# --- Note that I created the "User Exercises" folder and moved the csv files into this folder ---
# The files were moved from takeout/Fitbit/Health Fitness Data_GoogleData
folder_path = "takeout/Fitbit/User Exercises"

# Find all matching CSV files
csv_files = glob.glob(os.path.join(folder_path, "UserExercises_*.csv"))

# Initialize an empty list to store DataFrames
dfs = []

# Read and append each CSV file
for file in csv_files:
    df = pd.read_csv(file)

    # Ensure expected columns exist
    if "exercise_start" in df.columns:
        df["exercise_start"] = pd.to_datetime(df["exercise_start"])  # Convert to datetime
        dfs.append(df)

# Combine all DataFrames
if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Sort by exercise start time
    combined_df = combined_df.sort_values(by="exercise_start")

    # Save to a new CSV
    combined_df.to_csv("combine/combined_exercises.csv", index=False)
    print(f"Successfully merged {len(csv_files)} files into 'combined_exercises.csv'.")
else:
    print("No matching files found.")
