"""
Abhinav Khanna
axk1312
Project 5

Script for collecting page download time data using wget
"""
import subprocess
import datetime
import csv

def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if 6 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 18:
        return "evening"
    else:
        return "morning"

def wget_download_time(url):
    timeout = 20
    try:
        start_time = datetime.datetime.now()
        subprocess.run(["wget", "--delete-after", url], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, timeout=timeout)
        end_time = datetime.datetime.now()
        duration = (end_time - start_time).total_seconds()
        return duration
    except subprocess.TimeoutExpired:
        return "timeout"
    except subprocess.CalledProcessError:
        return None

def read_websites_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row[1] for row in reader]

def main():
    file_path = 'Tech_Companies_List_Final.csv'
    output_file = 'wget_results.txt'
    num_iterations = 1

    websites = read_websites_from_csv(file_path)

    for _ in range(num_iterations):
        for url in websites:
            duration = wget_download_time(url)
            if duration is not None:
                with open(output_file, 'a') as f:
                    time_of_day = get_time_of_day()
                    f.write(f"{datetime.datetime.now()}, {time_of_day}, {url}, {duration}s\n")

if __name__ == "__main__":
    main()
