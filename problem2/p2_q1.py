
import psutil

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Function to check CPU usage
def check_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        print(f"CPU usage is high: {cpu_percent}%")

# Function to check memory usage
def check_memory():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > MEMORY_THRESHOLD:
        print(f"Memory usage is high: {memory_percent}%")

# Function to check disk space
def check_disk():
    disk_percent = psutil.disk_usage('/').percent
    if disk_percent > DISK_THRESHOLD:
        print(f"Disk space is running low: {disk_percent}%")

# Function to check running processes
def check_processes():
    process_count = len(psutil.pids())
    if process_count > 100:
        print(f"Too many processes running: {process_count}")

# Main function
def main():
    print("System Health Report -", datetime.datetime.now())
    check_cpu()
    check_memory()
    check_disk()
    check_processes()

if __name__ == "__main__":
    import datetime
    main()

