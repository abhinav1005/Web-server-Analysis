"""
Abhinav Khanna
axk1312
Project 5

Script for finding correlation coefficient between Time of Day and page download time
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
    
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

df['DownloadTime'] = pd.to_numeric(df['DownloadTime'], errors='coerce')
df = df[df['Website'] != 'Website']
time_of_day_mapping = {'morning': 1, 'evening': 2, 'night': 3}
df['TimeOfDay'] = df['TimeOfDay'].map(time_of_day_mapping)
grouped = df.groupby('Website')
correlation_data = []
# Iterate through groups and print correlation coefficients
for name, group in grouped:
    correlation = group['TimeOfDay'].corr(group['DownloadTime'])
    correlation_data.append({'Company': name, 'Correlation': correlation})

correlation_df = pd.DataFrame(correlation_data)
# Sort the DataFrame by 'Correlation' in descending order
correlation_df = correlation_df.sort_values(by='Correlation', ascending=False)
correlation_df.reset_index(drop=True, inplace=True)
print(correlation_df)