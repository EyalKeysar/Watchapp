import psutil
import json
import time

# Initial call to set up the baseline for CPU usage
psutil.cpu_percent(interval=None)

# Get a list of all running processes
all_processes = psutil.process_iter()

def process_info_to_json(process_info):
    return json.dumps(process_info)

file_path = "processes.txt"
with open(file_path, "w") as file:
    # Iterate through the processes and print information
    for process in all_processes:
        try:
            process_info = process.as_dict(attrs=['pid', 'name', 'username', 'cpu_percent', 'memory_info'])
            if process_info['cpu_percent'] > 0.0:
                print(process_info)
            file.write(process_info_to_json(process_info) + "\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Handle exceptions that may occur due to permission issues or terminated processes
            pass

# Give some time for psutil to calculate CPU percentages
time.sleep(1)

# Print CPU usage after the loop
cpu_percent = psutil.cpu_percent(interval=None)
print(f"Overall CPU Usage: {cpu_percent}%")
