#!/usr/bin/env python3

import re
import argparse
from collections import Counter

def extract_failed_logins(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()

    failed_logins = []
    for line in lines:
        if "Failed password" in line:
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                failed_logins.append(ip_match.group(1))

    return failed_logins

def print_report(ip_list):
    counter = Counter(ip_list)
    print("\n📊 Failed Login Attempt Report")
    print("="*40)
    for ip, count in counter.items():
        print(f"IP: {ip} | Attempts: {count}")
    print("="*40)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze failed SSH login attempts from log files.")
    parser.add_argument("logfile", help="Path to the log file (e.g., /var/log/auth.log)")
    args = parser.parse_args()

    ips = extract_failed_logins(args.logfile)
    if ips:
        print_report(ips)
    else:
        print("No failed login attempts found.")
