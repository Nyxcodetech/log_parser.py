# 📄 Log Parser – SSH Failed Login Analyzer (Python)

This Python tool analyzes system log files (e.g., `/var/log/auth.log`) to detect failed SSH login attempts and identify suspicious IP addresses. Built by [Mariana García (@nyxhunter)](https://www.linkedin.com/in/), it's part of her offensive cybersecurity toolkit.

---

## 🔍 What it does
- Scans logs for `Failed password` entries
- Extracts IP addresses of failed SSH login attempts
- Counts and displays the number of attempts per IP
- Prints a clean, easy-to-read report

---

## 🛠 Usage

python3 log_parser.py <log_file_path>

python3 log_parser.py /var/log/auth.log

Requirements
Python 3
Log file with failed SSH login attempts (e.g., /var/log/auth.log
No external libraries needed (uses built-in re and collections)


📊 Failed Login Attempt Report
========================================
IP: 192.168.1.10 | Attempts: 3
IP: 203.0.113.50 | Attempts: 7
========================================

Mariana García (@nyxhunter) is a cybersecurity student, offensive tools builder, and certified by Google, AWS, and IBM. This script is part of her personal journey toward becoming a professional red teamer.
