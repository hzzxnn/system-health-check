import psutil
import socket

#grab cpu usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")

#grab memory info
memory_info = psutil.virtual_memory()
print(f"Memory Used: {memory_info.percent}%")

#grab disk info
disk_info = psutil.disk_usage('/')
disk_partitions = psutil.disk_partitions()
print(f"Disk Info: {disk_info.percent}%")
print("Partitions:")
for partition in disk_partitions:
    print(f"= {partition.device} mounted on {partition.mountpoint} [{partition.fstype}]")

#check internet connection
def check_connection():
    try:
        #try to connect to Google's DNS
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False
if check_connection():
    print("Internet Access: Active!")
else:
    print("Internet Access: Inactive!")
