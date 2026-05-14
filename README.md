Python Security Log Analyzer

A professional Python tool designed to analyze failed login attempts, detect potential brute-force attacks, and generate structured reports. This project demonstrates progressive learning from basic scripting to professional, portfolio-ready automation, mapping closely to CIS-30A learning outcomes and cybersecurity workflows.

Project Overview

The goal of this project is to simulate a real-world security log analysis workflow, suitable for:

Portfolio development
CPL (Credit for Prior Learning) submission at RCC
Internship/job readiness in DevOps and cybersecurity

The analyzer reads log files, identifies failed login attempts, aggregates results by IP, flags suspicious activity, and exports structured reports for further analysis.

Version History
Version	Description	Key Features	Design Decisions
v1 – Basic Log Analyzer	Initial proof-of-concept	Reads logs, detects failed logins, counts total failures	Simple procedural code to demonstrate Python fundamentals (loops, conditionals, file I/O). No IP extraction yet to keep initial scope manageable.
v2 – IP-Based Detection	Enhanced security detection	Extracts IP addresses, counts failures per IP, basic brute-force detection	Regex was introduced to identify IP addresses; dictionaries (defaultdict) used for efficient counting. Modular functions were optional at this stage.
v3 – Professional CLI Tool	Portfolio-ready scripting	Command-line interface, modular functions, CSV reporting, terminal summary	Structured into functions for readability and reusability. CSV output introduced to simulate real-world SOC reporting. CLI allows for flexible usage beyond a single hardcoded log file.
v4 – Polished & Portfolio-Ready	Full-featured, professional version	CLI with optional JSON export, enhanced error handling, structured terminal summary, comprehensive commentary	Added JSON export to provide multiple data formats for automation or DevOps integration. Functions are fully modular. Error handling ensures robustness. Extensive commentary explains why each element was implemented in this way.
Design Philosophy & Key Decisions
Modular Functions
Each major task (reading logs, extracting IPs, analyzing, exporting) has its own function.
Reason: Encourages reusable, maintainable code—a practice expected in real-world DevOps or SOC scripts.
Regex for IP Extraction
Used a simple IPv4 regex to parse failed login lines.
Reason: Regex is efficient for pattern matching; avoids manually splitting strings, reducing errors.
Command-Line Interface
Accepts log file, threshold, and optional JSON export.
Reason: CLI scripting is standard in security operations, allowing automation and batch processing.
CSV & JSON Export
CSV provides human-readable reporting; JSON allows integration with other tools.
Reason: Simulates real-world reporting pipelines; shows versatility for DevOps workflows.
Error Handling
Graceful exit if log file is missing.
Reason: Real-world scripts must handle unexpected inputs without crashing, demonstrating robustness.
Terminal Summary & Alerts
Provides clear, formatted output highlighting suspicious IPs.
Reason: Enables immediate interpretation by a SOC analyst, simulating professional utility.
Installation
Clone the repository:
git clone https://github.com/faithfulstudent/python-security-log-analyzer.git
cd python-security-log-analyzer
Ensure Python 3.x is installed.
No additional packages are required (uses Python standard library: re, csv, json, sys, collections).
Usage Instructions
Basic Usage
python main_v4.py sample.log
Reads sample.log
Default brute-force threshold: 3
Outputs terminal summary and failed_logins.csv
Custom Threshold
python main_v4.py sample.log 2
Sets brute-force threshold to 2 failed attempts
Enable JSON Export
python main_v4.py sample.log 2 yes
Exports failed_logins.json in addition to CSV
Sample Input / Output

Input (sample.log):

Failed password for invalid user admin from 192.168.1.10 port 22 ssh2
Failed password for invalid user guest from 192.168.1.20 port 22 ssh2
Failed password for invalid user admin from 192.168.1.10 port 22 ssh2

Terminal Output:

==============================
SECURITY LOG ANALYSIS REPORT
==============================

Total failed logins: 3

Failed logins by IP:
- 192.168.1.10: 2 failed attempts
- 192.168.1.20: 1 failed attempts

Potential brute-force attacks (threshold: 2):
- ALERT: 192.168.1.10 - 2 failed attempts

[INFO] CSV report exported as 'failed_logins.csv'
[INFO] JSON report exported as 'failed_logins.json'  # if JSON flag is enabled
Skills Demonstrated / Learning Outcomes
Python Fundamentals: loops, conditionals, variables, functions
File I/O: reading from and writing to logs, CSV, JSON
Regex: pattern matching for IP extraction
Data Structures: dictionaries for counting occurrences
Modular Programming: reusable functions, CLI arguments
Error Handling: robust script behavior
Cybersecurity Relevance: log analysis, brute-force detection, SOC-style reporting
Portfolio & CPL Ready: professional structure, commentary, multiple output formats
Future Work / Version 5 Ideas
Containerize the tool using Docker for portability
Add unit tests with pytest to demonstrate test-driven development
Integrate a small dashboard (Flask or Streamlit) for visual analysis
Expand log parsing to real /var/log/auth.log files on Linux systems
