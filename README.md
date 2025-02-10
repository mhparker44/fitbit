# fitbit
Scripts to analyze Fitbit Data.

After Google acquired Fitbit, there is no web-based dashboard to view your health data. However, you export your data by [following these steps](https://support.google.com/fitbit/answer/14236615?hl=en#zippy=%2Chow-do-i-export-my-fitbit-data).

The goal of this project is to provide sample code that can be used to process this data.

# Step 0: Understand folder format. 
Data is exported into a folder called "takeout". For example: takeout/Fitbit/Heart Rate Variability

# Step 1: Clean the data 
The data is sent in individual files for each day. In my case, that meant thousands of files from 2020 to 2025.
We first use python to aggregate these daily files into one dataframe for processing.

# Step 2: Visualize the data
Plot scatterplots and bar graphs as needed.

# Step 3: Analyzing for anomolies
I am not a doctor and this is not medical advice. If you see something abnormal, please ask a medical professional.

# Step 4: Predicting future trends
Based on heartrate and step data. Build models based on "normal" trends (within 1 to 2 std deviations).

# Step 5: Take Action
Make an actionable plan to improve your fitness.
Example: You might notice that you get an extra 2 hours of sleep on weekends. Perhaps you want to try getting more sleep on Wednesdays.
Example: You typically walk 5,000 steps per day. However, you notice that each Monday you walk less than 3,000 steps. You can set a goal to go a walk after lunch on Mondays.
