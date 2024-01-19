"""
Abhinav Khanna
axk1312
Project 5

Script for collecting Ping response data
"""
import csv
import subprocess
import datetime

def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if 6 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 18:
        return "evening"
    else:
        return "night"

def ping_website(url):
    try:
        response = subprocess.check_output(
            ["ping", "-c", "5", url],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        return response
    except subprocess.CalledProcessError:
        return None

def read_websites_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row[1] for row in reader]

def main():
    file_path = 'Tech_Companies_List_Final.csv'
    output_file = 'ping_results.txt'
    num_iterations = 5

    websites = read_websites_from_csv(file_path)

    for _ in range(num_iterations):
        for url in websites:
            response = ping_website(url)
            if response:
                with open(output_file, 'a') as f:
                    time_of_day = get_time_of_day()
                    f.write(f"{time_of_day},{url},{response}\n")

if __name__ == "__main__":
    main()
