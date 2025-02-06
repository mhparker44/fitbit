import pandas as pd
import matplotlib.pyplot as plt
import time

# Measure start time
start_time = time.time()

# Load the combined exercises CSV
csv_file = "combined/combined_exercises.csv"
df = pd.read_csv(csv_file)

# Check if activity_name column exists
if "activity_name" not in df.columns:
    print("Error: 'activity_name' column not found in the dataset.")
    exit()

# Count occurrences of each workout type
activity_counts = df["activity_name"].value_counts()

# Display unique activities and their counts
print("Workout Types and Counts:")
print(activity_counts)

# Plot bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(activity_counts.index, activity_counts.values, color="royalblue", alpha=0.75)

# Add data labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # X position (center of the bar)
        height,  # Y position (on top of the bar)
        str(int(height)),  # Convert count to integer and string
        ha="center",  # Center horizontally
        va="bottom",  # Place text just above the bar
        fontsize=10,
        fontweight="bold"
    )

# Customize plot appearance
plt.xlabel("Workout Type")
plt.ylabel("Count")
plt.title("Workout Frequency")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.tight_layout()  # Prevent labels from being cut off
plt.show()

# Measure end time
end_time = time.time()
print(f"Processing completed in {end_time - start_time:.2f} seconds.")
