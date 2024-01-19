"""
Abhinav Khanna
axk1312
Project 5

Script for Visualizing Round Trip Times from ping response data
"""
import re
from collections import defaultdict
import matplotlib.pyplot as plt

def extract_ping_data(text):
    pattern = r"(morning|evening|night),([\w\.]+).*?round-trip min/avg/max/stddev = [\d\.]+/([\d\.]+)/[\d\.]+/[\d\.]+ ms"
    results = defaultdict(lambda: defaultdict(list))
    overall_averages = defaultdict(list)

    for match in re.finditer(pattern, text, re.MULTILINE | re.DOTALL):
        time_of_day, website, avg = match.groups()
        avg_float = float(avg)
        results[time_of_day][website].append(avg_float)
        overall_averages[website].append(avg_float)

    # Calculate averages for each time of day
    for time_of_day in results:
        for website in results[time_of_day]:
            avg_list = results[time_of_day][website]
            results[time_of_day][website] = sum(avg_list) / len(avg_list)

    # Calculate overall averages
    for website in overall_averages:
        avg_list = overall_averages[website]
        overall_averages[website] = sum(avg_list) / len(avg_list)
    
    return results, overall_averages

def convert_to_lists(results, overall_averages):
    results_list = []
    overall_list = []

    for time_of_day, websites in results.items():
        for website, avg in websites.items():
            results_list.append((time_of_day, website, avg))

    for website, avg in overall_averages.items():
        overall_list.append((website, avg))

    return results_list, overall_list

with open('ping_results.txt', 'r') as file:
    text_data = file.read()

results, overall_averages = extract_ping_data(text_data)
results_list, overall_list = convert_to_lists(results, overall_averages)

# Average round trip time plotted based on the websites
sorted_overall_list = sorted(overall_list, key=lambda x: x[1])
websites, averages = zip(*sorted_overall_list)
# Creating the bar chart
plt.figure(figsize=(10, 6))
plt.bar(websites, averages, color='skyblue')
plt.xlabel('Websites')
plt.ylabel('Average Round Trip Time (ms)')
plt.title('Overall Average Round Trip Time per Website')
plt.xticks(rotation=80)
plt.tight_layout()
plt.show()


# Plot for Sorted Average Round Trip Times by Company for 'Morning'
morning_data = [(website, avg) for time_of_day, website, avg in results_list if time_of_day == 'morning']
sorted_morning_data = sorted(morning_data, key=lambda x: x[1])
morning_websites, morning_averages = zip(*sorted_morning_data) if sorted_morning_data else ([], [])

plt.figure(figsize=(10, 6))
plt.bar(morning_websites, morning_averages, color='skyblue')
plt.xlabel('Websites')
plt.ylabel('Average Round Trip Time (ms)')
plt.title('Sorted Average Round Trip Time by Company - Morning')
plt.xticks(rotation=80)
plt.tight_layout()
plt.show()


# Plot for Sorted Average Round Trip Times by Company for 'Evening'
evening_data = [(website, avg) for time_of_day, website, avg in results_list if time_of_day == 'evening']
sorted_evening_data = sorted(evening_data, key=lambda x: x[1])
evening_websites, evening_averages = zip(*sorted_evening_data) if sorted_evening_data else ([], [])

plt.figure(figsize=(10, 6))
plt.bar(evening_websites, evening_averages, color='green')
plt.xlabel('Websites')
plt.ylabel('Average Round Trip Time (ms)')
plt.title('Sorted Average Round Trip Time by Company - Evening')
plt.xticks(rotation=80)
plt.tight_layout()
plt.show()


# Plot for Sorted Average Round Trip Times by Company for 'Night'
night_data = [(website, avg) for time_of_day, website, avg in results_list if time_of_day == 'night']
sorted_night_data = sorted(night_data, key=lambda x: x[1])
night_websites, night_averages = zip(*sorted_night_data) if sorted_night_data else ([], [])

plt.figure(figsize=(10, 6))
plt.bar(night_websites, night_averages, color='purple')
plt.xlabel('Websites')
plt.ylabel('Average Round Trip Time (ms)')
plt.title('Sorted Average Round Trip Time by Company - Night')
plt.xticks(rotation=80)
plt.tight_layout()
plt.show()
