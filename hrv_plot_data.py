import pandas as pd
import matplotlib.pyplot as plt
import time

# Measure start time
start_time = time.time()

# Load the pre-combined CSV
csv_file = "combined/combined_hrv_data.csv"
df = pd.read_csv(csv_file)

# Convert timestamp column to datetime (if not already)
df["timestamp"] = pd.to_datetime(df["timestamp"]).dt.date

# Create three plots without blocking execution
fig, axes = plt.subplots(nrows=3, figsize=(12, 12))

# Plot RMSSD
axes[0].scatter(df["timestamp"], df["rmssd"], alpha=0.6, color='blue')
axes[0].set_xlabel("Date")
axes[0].set_ylabel("RMSSD")
axes[0].set_title("RMSSD Over Time")
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid()

# Plot NREM HR
axes[1].scatter(df["timestamp"], df["nremhr"], alpha=0.6, color='green')
axes[1].set_xlabel("Date")
axes[1].set_ylabel("NREM HR")
axes[1].set_title("NREM HR Over Time")
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid()

# Plot Entropy
axes[2].scatter(df["timestamp"], df["entropy"], alpha=0.6, color='red')
axes[2].set_xlabel("Date")
axes[2].set_ylabel("Entropy")
axes[2].set_title("Entropy Over Time")
axes[2].tick_params(axis='x', rotation=45)
axes[2].grid()

# Adjust layout and show all plots at once
plt.tight_layout()
plt.show()

# Measure end time
end_time = time.time()
print(f"Plotting completed in {end_time - start_time:.2f} seconds.")
