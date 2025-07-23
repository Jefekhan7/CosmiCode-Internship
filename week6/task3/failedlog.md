# README - Failed SSH Login Log Analyzer

## Overview

This Python script analyzes a Linux `auth.log` file to detect failed SSH login attempts.
It extracts the IP addresses of hosts that attempted and failed to log in, then counts how many times each IP appears.
This helps identify possible brute-force attacks or unauthorized access attempts.

## How It Works

- The script uses Python's `re` (regular expressions) module to find lines with "Failed password".
- It captures the IP address from each matching line.
- It counts how many times each IP occurs using a subprocess module for system commonds like uniq and sort.
- Finally, it prints a simple report showing which IPs had the most failed attempts.

## Example Log Format

The log should contain lines similar to:

    Jul 23 13:02:10 ubuntu sshd[12346]: Failed password for root from 203.0.113.12 port 48412 ssh2

## How To Use

1. Place your sample `auth.log` in the same folder as the script.
2. Run the script with Python 3 | python:

    python3 failedlog.py

3. The script will print a summary of failed login attempts grouped by IP address.

## Dependencies

- Python 3.x
- Standard Python libraries (`re` and `subprocess`)

## Purpose

This script demonstrates how log analysis helps detect suspicious login activity.
It can be extended to send alerts or block suspicious IPs automatically.

---

