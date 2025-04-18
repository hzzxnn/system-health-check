import os
import socket
import psutil
import datetime

#Grab CPU
def cpu_usage():
    return psutil.cpu_percent(interval=1)

#Grab Memory
def mem_usage():
    return psutil.virtual_memory().percent

#Grab disk usage
def get_disk_usage():
    return psutil.disk_usage('/').percent

#Grab Partitions
def list_partitions():
    parts_info = []
    for p in psutil.disk_partitions():
        parts_info.append(f"- {p.device} mounted on {p.mountpoint} [{p.fstype}]")
    return parts_info
    
#Grab internet
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False
    
def gen_rep():
    #collect data
    cpu = cpu_usage()
    mem = mem_usage()
    disk = get_disk_usage()
    partitions = list_partitions()
    internet = check_internet()

    #build rep as string
    report_lines = []
    report_lines.append("="*35)
    report_lines.append("SYSTEM HEALTH REPORT 🖥️")
    report_lines.append("="*35)
    report_lines.append(f"CPU Usage:    {cpu}%")
    report_lines.append(f"Memory Usage:    {mem}%")
    report_lines.append(f"Disk Usage (/):    {disk}%")
    report_lines.append("\nPartitions:")
    report_lines.extend(partitions)
    report_lines.append(f"\nInternet Connection: {'✅ Active!' if internet else '❌ Inactive!'}")

    return "\n".join(report_lines)

def save_rep_to_file(report):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"logs/health_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    return filename

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    report = gen_rep()
    print(report)
    log_file = save_rep_to_file(report)
    print(f"\nLog file saved to: {log_file}")


