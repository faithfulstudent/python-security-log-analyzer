# main_v3.py
# Professional Python Security Log Analyzer - Version 3
# Portfolio-ready, with CLI, IP aggregation, brute-force detection, and CSV export

import re
import csv
import sys
from collections import defaultdict

# ----------------------------
# Function: Read logs
# ----------------------------
def read_logs(file_path):
    """Read log file and return lines as a list."""
    try:
        with open(file_path, "r") as file:
            logs = file.readlines()
        return logs
    except FileNotFoundError:
        print(f"Error: Log file '{file_path}' not found.")
        sys.exit(1)

# ----------------------------
# Function: Extract failed login IPs
# ----------------------------
def extract_failures(log_lines):
    """
    Extract IP addresses from failed login lines.
    Returns a dictionary: {IP: failure_count}
    """
    failed_ips = defaultdict(int)
    for line in log_lines:
        if "Failed password" in line:  # Only consider failed logins
            match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)  # Regex to find IPv4
            if match:
                ip = match.group(1)
                failed_ips[ip] += 1
    return failed_ips

# ----------------------------
# Function: Print summary and brute-force alerts
# ----------------------------
def analyze_ips(failed_ips, threshold):
    """Print summary of failed logins and flag IPs exceeding threshold."""
    total_failures = sum(failed_ips.values())
    print("\n==============================")
    print("SECURITY LOG ANALYSIS REPORT")
    print("==============================\n")
    print(f"Total failed logins: {total_failures}\n")

    print("Failed logins by IP:")
    for ip, count in failed_ips.items():
        print(f"- {ip}: {count} failed attempts")

    print(f"\nPotential brute-force attacks (threshold: {threshold}):")
    flagged = False
    for ip, count in failed_ips.items():
        if count >= threshold:
            print(f"- ALERT: {ip} - {count} failed attempts")
            flagged = True
    if not flagged:
        print("None detected")

# ----------------------------
# Function: Export results to CSV
# ----------------------------
def export_csv(failed_ips, filename="failed_logins.csv"):
    """Write failed login counts per IP to a CSV file."""
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP Address", "Failed Attempts"])
        for ip, count in failed_ips.items():
            writer.writerow([ip, count])
    print(f"\nCSV report exported as '{filename}'")

# ----------------------------
# Main program
# ----------------------------
if __name__ == "__main__":
    # Command-line interface: require at least a log file
    if len(sys.argv) < 2:
        print("Usage: python main_v3.py <log_file_path> [threshold]")
        sys.exit(1)

    log_file = sys.argv[1]
    # Optional threshold argument; default = 3
    threshold = int(sys.argv[2]) if len(sys.argv) > 2 else 3

    print(f"Analyzing log file: {log_file}")
    print(f"Brute-force threshold: {threshold}")

    # Step 1: Read logs
    logs = read_logs(log_file)

    # Step 2: Extract failed login IPs
    failed_ips = extract_failures(logs)

    # Step 3: Analyze and print summary
    analyze_ips(failed_ips, threshold)

    # Step 4: Export CSV report
    export_csv(failed_ips)
