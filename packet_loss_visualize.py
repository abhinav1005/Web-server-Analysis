"""
Abhinav Khanna
axk1312
Project 5

Script for visualizing packet loss data
"""
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def extract_data(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    current_website = None
    current_time = None

    for line in lines:
        if 'PING' in line:
            website_match = re.search(r'(\w+\.com),PING', line)
            time_match = re.search(r'(\w+),', line)
            if website_match and time_match:
                current_website = website_match.group(1)
                current_time = time_match.group(1)
        elif 'packet loss' in line:
            packet_loss_match = re.search(r'(\d+\.?\d*)% packet loss', line)
            if packet_loss_match and current_website and current_time:
                packet_loss = float(packet_loss_match.group(1))
                data_list.append({'website': current_website, 'time': current_time, 'packet_loss': packet_loss})
    
    return data_list

file_path = 'ping_results.txt'
extracted_data = extract_data(file_path)

new_data=[]
for data in extracted_data:
    if(data["packet_loss"]!=0.0):
        new_data.append(data)
        print(data)

df = pd.DataFrame(new_data)
# Creating a pivot table with average packet loss
pivot_table = df.pivot_table(index='website', columns='time', values='packet_loss', aggfunc='mean')
pivot_table = pivot_table.fillna(0)
# Creating the heatmap
plt.figure(figsize=(15, 10))
sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt=".1f", linewidths=.5, cbar_kws={'label': 'Packet Loss (%)'})
plt.title('Heatmap of Average Packet Loss Across Websites and Times of Day')
plt.ylabel('Website')
plt.xlabel('Time of Day')
plt.xticks(rotation=45) 
plt.yticks(rotation=0)  
plt.tight_layout()
plt.show()

# Convert the data into a Pandas DataFrame
# df = pd.DataFrame(new_data)

# # Creating a pivot table. Adjust the aggregation function as needed (mean, sum, etc.)
# pivot_table = df.pivot_table(index='website', columns='time', values='packet_loss', aggfunc='mean')

# # Creating the heatmap
# plt.figure(figsize=(12, 8))
# sns.heatmap(pivot_table, annot=True, cmap='viridis', fmt=".1f")
# plt.title('Heatmap of Packet Loss Across Websites and Times of Day')
# plt.ylabel('Website')
# plt.xlabel('Time of Day')
# plt.show()