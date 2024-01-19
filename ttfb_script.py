"""
Abhinav Khanna
axk1312
Project 5

Script for collecting Time to First Byte data
"""
import csv
import requests
import datetime

def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if 6 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 18:
        return "evening"
    else:
        return "night"

import subprocess

def get_ttfb(url):
    try:
        response = subprocess.check_output(
            ["curl", "-o", "/dev/null", "-s", "-w", "%{time_starttransfer}\n", url],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        return response.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.output}")
        return None

def read_websites_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row[1] for row in reader]  # Assuming URLs are in the second column

def main():
    file_path = 'Tech_Companies_List_Final.csv'  # Replace with your CSV file path
    output_file = 'ttfb_results.txt'
    num_iterations = 5

    websites = read_websites_from_csv(file_path)

    for _ in range(num_iterations):
        for url in websites:
            
            ttfb = get_ttfb(url)
            if ttfb is not None:
                with open(output_file, 'a') as f:
                    time_of_day = get_time_of_day()
                    f.write(f"{time_of_day},{url},{ttfb}\n")

if __name__ == "__main__":
    main()
