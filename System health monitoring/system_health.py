#!/usr/bin/env python3

import psutil
import logging
import os
import time
import keyboard

# Set up logging
logging.basicConfig(filename='system_health_monitor.log', 
                    level=logging.INFO, 
                    format='%(asctime)s %(message)s')

# Define thresholds
CPU_THRESHOLD = 80  # percentage
MEMORY_THRESHOLD = 80  # percentage
DISK_THRESHOLD = 80  # percentage
PROCESS_THRESHOLD = 300  # number of processes

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {usage}%')
        print(f'High CPU usage detected: {usage}%')
    return usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    usage = memory.percent
    if usage > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {usage}%')
        print(f'High memory usage detected: {usage}%')
    return usage

def check_disk_usage():
    usage = psutil.disk_usage('/').percent
    if usage > DISK_THRESHOLD:
        logging.warning(f'Low disk space detected: {usage}% used')
        print(f'Low disk space detected: {usage}% used')
    return usage

def check_running_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        logging.warning(f'High number of running processes detected: {process_count}')
        print(f'High number of running processes detected: {process_count}')
    return process_count

def main():
    print("The program will start soon.Press esc to stop:")
    time.sleep(5)
    while True:
        if keyboard.is_pressed('esc'):
            print("Exiting monitoring script.")
            break
        cpu = check_cpu_usage()
        memory = check_memory_usage()
        disk = check_disk_usage()
        processes = check_running_processes()

        logging.info(f'System health: CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%, Processes: {processes}')
        print(f'System health: CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%, Processes: {processes}')
        
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()
