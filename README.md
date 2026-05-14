# Python Security Log Analyzer

## Overview
The Python Security Log Analyzer is a cybersecurity-focused Python project designed to **analyze authentication log files** and detect failed login attempts.

This project is part of a professional **Python/DevOps/Cybersecurity portfolio** and demonstrates scripting, automation, log analysis, and modular programming skills relevant to:
- Cybersecurity operations
- Security monitoring
- DevOps automation
- Linux system administration
- Python programming fundamentals

The project is designed to be **portfolio-ready and CPL-friendly**, showing clear progression from basic scripting to professional, production-like tooling.

---

## Version History

| Version | Description | Key Features | Design Decisions |
|---------|------------|--------------|-----------------|
| **v1 – Basic Log Analyzer** | Initial proof-of-concept | Reads logs, detects failed logins, counts total failures | Simple procedural code to demonstrate Python fundamentals. Minimal functionality to establish a working base. |
| **v2 – IP-Based Detection** | Added IP detection | Extracts IPs, counts failures per IP | Regex used for pattern matching. Dictionaries introduced for counting per IP. Demonstrates modular thinking. |
| **v3 – CLI Tool with CSV** | Professional scripting | Command-line interface, modular functions, CSV reporting, terminal summary | CLI added for flexibility. Modular functions improve readability. CSV export simulates real-world reporting. |
| **v4 – Polished, Portfolio-Ready** | Full-featured version | CLI with optional JSON export, robust error handling, enhanced terminal summary, extensive commentary | JSON export added for automation integration. Functions fully modular. Error handling ensures robustness. Commentary explains **why design choices were made**. Portfolio-ready for CPL or internships. |

---

## Key Features & Design Choices
1. **Modular Functions** – Each task (read logs, extract IPs, analyze, export) is in its own function.  
   *Reason:* Encourages reusable, maintainable code, aligned with professional practices.

2. **Regex for IP Extraction** – Efficient and reliable for pattern matching.  
   *Reason:* Avoids manual string parsing, reduces errors, mirrors real-world security scripts.

3. **Command-Line Interface (CLI)** – Users specify log files, thresholds, and export options.  
   *Reason:* CLI is standard in security automation and DevOps workflows.

4. **CSV & JSON Export** – CSV for human-readable reporting; JSON for automated processing.  
   *Reason:* Demonstrates professional reporting capabilities and workflow integration.

5. **Error Handling** – Program exits gracefully on invalid input.  
   *Reason:* Robust scripts are essential for real-world deployment.

6. **Terminal Summary & Alerts** – Highlights suspicious IPs based on threshold.  
   *Reason:* Provides immediate insights, simulating SOC analyst reporting.

---

## Project Structure
python-security-log-analyzer/
│
├── main.py # Main Python script
├── sample.log # Sample log file
└── README.md # Project documentation

---

## Sample Log Entries
Jan 10 10:00:01 sshd Failed password for root from 192.168.1.10
Jan 10 10:00:05 sshd Failed password for admin from 192.168.1.10
Jan 10 10:01:00 sshd Accepted password for user from 192.168.1.20
Jan 10 10:02:00 sshd Failed password for root from 192.168.1.30

## Example Output from Version 4

==================================
SECURITY LOG ANALYSIS REPORT

Total failed logins: 3

Failed logins by IP:

-192.168.1.10: 2 failed attempts
-192.168.1.20: 1 failed attempt

Potential brute-force attacks (threshold: 2):

-ALERT: 192.168.1.10 - 2 failed attempts

[INFO] CSV report exported as 'failed_logins.csv'
[INFO] JSON report exported as 'failed_logins.json'

---

## Learning Objectives / Skills Demonstrated
- **Python fundamentals:** variables, loops, conditionals, functions  
- **File I/O:** reading logs, writing CSV/JSON  
- **Regex:** pattern matching for IPs  
- **Data structures:** dictionaries for counting failed attempts  
- **Modular programming:** reusable, maintainable code  
- **Error handling:** graceful handling of invalid inputs  
- **CLI scripting:** command-line interface for professional workflow  
- **Cybersecurity relevance:** failed login detection, brute-force alerts  
- **Portfolio/CPL readiness:** commentary, structured code, multiple outputs

---

## Future Work / Version 5 Ideas
- Docker containerization for portability  
- Unit tests with `pytest` for professional validation  
- Small dashboard (Flask/Streamlit) for visualization  
- Expanded Linux `auth.log` parsing and SIEM-style integration

---

## Author
GitHub: [Umar Love](https://github.com/faithfulstudent)
