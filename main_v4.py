# main_v4.py
# Professional Python Security Log Analyzer - Version 4
# CLI-based, modular, CSV/JSON reporting, portfolio-ready
# Author: Your Name
# Purpose: Detect failed logins, identify brute-force attempts, export reports

import re
import csv
import json
import sys
from collections import defaultdict

# ----------------------------
# Function: Read logs
# ----------------------------
def read_logs(file_path):
    """Reads a log file and returns all lines as a list. Exits if file not found."""
    try:
        with open(file_path, "r") as file:
            logs = file.readlines()
        return logs
    except FileNotFoundError:
        print(f"[ERROR] Log file '{file_path}' not found.")
        sys.exit(1)

# ----------------------------
# Function: Extract failed login IPs
# ----------------------------
def extract_failures(log_lines):
    """
    Extracts IP addresses from lines containing 'Failed password'.
    Returns a dictionary {IP: failure_count}.
    """
    failed_ips = defaultdict(int)
    for line in log_lines:
        if "Failed password" in line:
            match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)  # IPv4 regex
            if match:
                ip = match.group(1)
                failed_ips[ip] += 1
    return failed_ips

# ----------------------------
# Function: Analyze and print summary
# ----------------------------
def analyze_ips(failed_ips, threshold):
    """
    Prints:
    - Total failed logins
    - Failures per IP
    - Alerts for IPs exceeding threshold (potential brute-force)
    Returns a dictionary of flagged IPs for reporting/export.
    """
    total_failures = sum(failed_ips.values())

    print("\n==============================")
    print("SECURITY LOG ANALYSIS REPORT")
    print("==============================\n")
    print(f"Total failed logins: {total_failures}\n")

    print("Failed logins by IP:")
    for ip, count in failed_ips.items():
        print(f"- {ip}: {count} failed attempts")

    print(f"\nPotential brute-force attacks (threshold: {threshold}):")
    flagged_ips = {}
    for ip, count in failed_ips.items():
        if count >= threshold:
            print(f"- ALERT: {ip} - {count} failed attempts")
            flagged_ips[ip] = count
    if not flagged_ips:
        print("None detected")
    return flagged_ips

# ----------------------------
# Function: Export CSV report
# ----------------------------
def export_csv(failed_ips, filename="failed_logins.csv"):
    """Exports failed IP counts to a CSV file."""
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP Address", "Failed Attempts"])
        for ip, count in failed_ips.items():
            writer.writerow([ip, count])
    print(f"\n[INFO] CSV report exported as '{filename}'")

# ----------------------------
# Function: Export JSON report
# ----------------------------
def export_json(failed_ips, filename="failed_logins.json"):
    """Exports failed IP counts to a JSON file."""
    with open(filename, "w") as jsonfile:
        json.dump(failed_ips, jsonfile, indent=4)
    print(f"[INFO] JSON report exported as '{filename}'")

# ----------------------------
# Main Program
# ----------------------------
if __name__ == "__main__":
    # CLI arguments:
    #   1: log file path (required)
    #   2: brute-force threshold (optional, default=3)
    #   3: export JSON? (optional, default=False)
    if len(sys.argv) < 2:
        print("Usage: python main_v4.py <log_file> [threshold] [json: yes/no]")
        sys.exit(1)

    log_file = sys.argv[1]
    threshold = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    export_json_flag = (sys.argv[3].lower() == "yes") if len(sys.argv) > 3 else False

    print(f"[INFO] Analyzing log file: {log_file}")
    print(f"[INFO] Brute-force threshold: {threshold}")
    if export_json_flag:
        print("[INFO] JSON export enabled")

    # Step 1: Read logs
    logs = read_logs(log_file)

    # Step 2: Extract failed login IPs
    failed_ips = extract_failures(logs)

    # Step 3: Analyze IPs and print summary
    flagged_ips = analyze_ips(failed_ips, threshold)

    # Step 4: Export CSV
    export_csv(failed_ips)

    # Step 5: Export JSON (optional)
    if export_json_flag:
        export_json(failed_ips)
