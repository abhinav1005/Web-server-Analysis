"""
Abhinav Khanna
axk1312
Project 5

Script for visualizing and finding page download percentage change analysis
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
    
file_path = 'wget_outputs.txt'

parsed_data = []

with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(', ')
        if len(parts) == 3:
            time_of_day = parts[0]
            website = parts[1]
            download_time = parts[2]
            parsed_data.append((time_of_day, website, download_time))


df = pd.DataFrame(parsed_data, columns=['TimeOfDay', 'Website', 'DownloadTime'])
df['DownloadTime'] = pd.to_numeric(df['DownloadTime'].str.replace('s', ''), errors='coerce')
grouped_stats = df.groupby('Website')['DownloadTime'].agg(['mean', 'median', 'std', 'min', 'max'])
df['DownloadTime'] = pd.to_numeric(df['DownloadTime'], errors='coerce')
df = df[df['Website'] != 'Website']
# Group by both Website and TimeOfDay and calculate mean
avg_download_by_website_time = df.groupby(['Website', 'TimeOfDay'])['DownloadTime'].mean().reset_index()
pivot_df = avg_download_by_website_time.pivot(index='Website', columns='TimeOfDay', values='DownloadTime')

# Function to calculate percentage change
def percentage_change(old, new):
    if old == 0 or pd.isnull(old) or pd.isnull(new):
        return None
    return round((new - old) / old * 100, 1)

pivot_df['Morning_to_Evening_%'] = pivot_df.apply(lambda row: percentage_change(row['morning'], row['evening']), axis=1)
pivot_df['Evening_to_Night_%'] = pivot_df.apply(lambda row: percentage_change(row['evening'], row['night']), axis=1)

pivot_df = pivot_df.sort_values(by='Evening_to_Night_%', ascending=False)

print(pivot_df[['Morning_to_Evening_%', 'Evening_to_Night_%']])


# Assuming you've loaded your data into a DataFrame named df
# Convert DownloadTime to numeric
df['DownloadTime'] = pd.to_numeric(df['DownloadTime'], errors='coerce')


# Average Download Time by Website
avg_download_by_website = df.groupby('Website')['DownloadTime'].mean()


# Average Download Time by Website and Time of Day
avg_download_by_website_time = df.groupby(['Website', 'TimeOfDay'])['DownloadTime'].mean().unstack()


# Visualization
plt.figure(figsize=(8, 5))
avg_download_by_website.plot(kind='bar')
plt.title('Average Download Time by Website')
plt.ylabel('Average Download Time (s)')
plt.xlabel('Website')
plt.subplots_adjust(bottom=0.2)  # Adjust bottom margin
plt.tight_layout() 
plt.savefig("fig.png")
plt.show()
