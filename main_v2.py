# main_v2.py

import re
from collections import defaultdict

print("FAILED LOGIN DETECTION - Version 2\n")

# Dictionary to count failed logins per IP
failed_ips = defaultdict(int)

# Threshold for brute-force detection
threshold = 2  # change if you want

# Read log file
with open("sample.log", "r") as file:
    logs = file.readlines()

# Process each log line
for line in logs:
    if "Failed password" in line:
        # Extract IP address
        match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
        if match:
            ip = match.group(1)
            failed_ips[ip] += 1
            print(f"Failed login from {ip}")

# Print summary
print("\nSUMMARY:")
total_failures = sum(failed_ips.values())
print("Total failed logins:", total_failures)
print("\nFailed logins by IP:")
for ip, count in failed_ips.items():
    print(f"{ip}: {count} failed attempts")

# Detect potential brute-force attacks
print("\nPotential brute-force attacks:")
for ip, count in failed_ips.items():
    if count >= threshold:
        print(f"{ip} - {count} failed attempts (threshold: {threshold})")
