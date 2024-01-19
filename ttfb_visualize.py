"""
Abhinav Khanna
axk1312
Project 5

Script for visualizing Time to First Byte data
"""
import matplotlib.pyplot as plt

def parse_data(file_path):
    time_of_day_data = {}
    overall_data = {}
    counts = {}
    overall_counts = {}

    with open(file_path, 'r') as file:
        for line in file:
            time_of_day, website, time_str = line.strip().split(',')
            time_to_first_byte = float(time_str)

            # For time-of-day data
            if website not in time_of_day_data:
                time_of_day_data[website] = {'morning': 0, 'evening': 0, 'night': 0}
                counts[website] = {'morning': 0, 'evening': 0, 'night': 0}

            time_of_day_data[website][time_of_day] += time_to_first_byte
            counts[website][time_of_day] += 1

            # For overall data
            if website in overall_data:
                overall_data[website] += time_to_first_byte
                overall_counts[website] += 1
            else:
                overall_data[website] = time_to_first_byte
                overall_counts[website] = 1

    # Calculating the averages
    for website, times in time_of_day_data.items():
        for time_of_day in times:
            if counts[website][time_of_day] > 0:
                times[time_of_day] /= counts[website][time_of_day]

    for website in overall_data:
        overall_data[website] /= overall_counts[website]

    return overall_data, time_of_day_data

file_path = 'ttfb_results.txt'
overall_avg, avg_by_time_of_day = parse_data(file_path)

print("Overall Average:", overall_avg)
print("Average by Time of Day:", avg_by_time_of_day)


def plot_overall_avg(overall_avg):
    sorted_avg = dict(sorted(overall_avg.items(), key=lambda item: item[1]))
    websites = list(sorted_avg.keys())
    times = list(sorted_avg.values())

    # Creating the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(websites, times, color='skyblue')
    plt.xlabel('Website')
    plt.ylabel('Average Time to First Byte')
    plt.title('Overall Average Time to First Byte by Website')
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()
plot_overall_avg(overall_avg)

def plot_morning_avg(avg_by_time_of_day):
    morning_avg = {website: data['morning'] for website, data in avg_by_time_of_day.items() if 'morning' in data}
    sorted_avg = dict(sorted(morning_avg.items(), key=lambda item: item[1]))
    websites = list(sorted_avg.keys())
    times = list(sorted_avg.values())

    # Creating the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(websites, times, color='lightgreen')
    plt.xlabel('Website')
    plt.ylabel('Average Time to First Byte (Morning)')
    plt.title('Average Time to First Byte in the Morning by Website')
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()
plot_morning_avg(avg_by_time_of_day)

def plot_evening_avg(avg_by_time_of_day):
    morning_avg = {website: data['evening'] for website, data in avg_by_time_of_day.items() if 'evening' in data}
    sorted_avg = dict(sorted(morning_avg.items(), key=lambda item: item[1]))
    websites = list(sorted_avg.keys())
    times = list(sorted_avg.values())

    # Creating the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(websites, times, color='lightgreen')
    plt.xlabel('Website')
    plt.ylabel('Average Time to First Byte (Evening)')
    plt.title('Average Time to First Byte in the Evening by Website')
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()
plot_evening_avg(avg_by_time_of_day)

def plot_night_avg(avg_by_time_of_day):
    morning_avg = {website: data['night'] for website, data in avg_by_time_of_day.items() if 'night' in data}
    sorted_avg = dict(sorted(morning_avg.items(), key=lambda item: item[1]))
    websites = list(sorted_avg.keys())
    times = list(sorted_avg.values())

    # Creating the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(websites, times, color='lightgreen')
    plt.xlabel('Website')
    plt.ylabel('Average Time to First Byte (Night)')
    plt.title('Average Time to First Byte in the Night by Website')
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.show()
plot_night_avg(avg_by_time_of_day)