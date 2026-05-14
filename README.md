# python-security-log-analyzer
Cybersecurity-focused Python tool for analyzing Linux authentication logs and detecting suspicious activity.

# Python Security Log Analyzer

## Overview

The Python Security Log Analyzer is a cybersecurity-focused Python project designed to analyze authentication log files and detect failed login attempts.

This project was created as part of a professional Python/DevOps/Cybersecurity portfolio and demonstrates foundational scripting, automation, and log analysis skills relevant to:

- Cybersecurity operations
- Security monitoring
- DevOps automation
- Linux system administration
- Python programming fundamentals

---

## Features

Current Version (v1) includes:

- Read log files
- Detect failed SSH login attempts
- Count failed login events
- Display summarized results

Planned future features:

- IP address extraction
- Brute-force attack detection
- CSV/JSON export
- Docker containerization
- Command-line arguments
- Real Linux auth.log support
- API integrations
- SIEM-style alerting

---

## Technologies Used

- Python 3
- GitHub
- Git
- Linux/Bash concepts
- Log analysis techniques

---

## Project Structure

```text
python-security-log-analyzer/
│
├── main.py
├── sample.log
└── README.md
```

---

## Sample Log Entries

```text
Jan 10 10:00:01 sshd Failed password for root from 192.168.1.10
Jan 10 10:00:05 sshd Failed password for admin from 192.168.1.10
Jan 10 10:01:00 sshd Accepted password for user from 192.168.1.20
Jan 10 10:02:00 sshd Failed password for root from 192.168.1.30
```

---

## Example Output

```text
FAILED LOGIN DETECTION

Jan 10 10:00:01 sshd Failed password for root from 192.168.1.10
Jan 10 10:00:05 sshd Failed password for admin from 192.168.1.10
Jan 10 10:02:00 sshd Failed password for root from 192.168.1.30

SUMMARY:
Total failed logins: 3
```

---

## Learning Objectives Demonstrated

This project demonstrates several Python programming competencies relevant to CIS-30A:

- Variables
- File input/output
- Loops
- Conditional statements
- String processing
- Counters and accumulation
- Basic automation scripting
- Program structure and logic

---

## Cybersecurity Relevance

Security analysts and DevOps engineers commonly analyze logs to:

- Detect failed login attempts
- Identify brute-force attacks
- Monitor authentication systems
- Investigate suspicious activity
- Automate security monitoring workflows

This project simulates foundational security log analysis techniques used in real-world environments.

---

## Author

GitHub: Umar Love
