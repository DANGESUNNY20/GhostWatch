# 👻 GhostWatch

### 🛡️ Security Operations Center (SOC) Automation & Threat Detection Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Linux-Kali%20%7C%20Ubuntu-FCC624?logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/Bash-Scripting-4EAA25?logo=gnubash&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/Cybersecurity-Blue%20Team-red" />
</p>

---

## 🎯 Project Overview

GhostWatch is a Linux-based Security Operations Center (SOC) automation platform designed to simulate real-world security monitoring workflows.

The platform automates:

* 📥 Log Collection
* 🔍 Threat Detection
* 🚨 Security Alerting
* 📊 Incident Reporting
* 🌐 Dashboard Visualization

Built using Python, Bash, and Linux administration concepts commonly used by SOC Analysts, Blue Teams, and Security Operations Engineers.

---

## ✨ Core Features

### 📥 Log Collection

* Monitor authentication logs
* Collect system events using `journalctl`
* Automated log archival

### 🔍 Threat Detection

* SSH Brute Force Detection
* Failed Login Monitoring
* Invalid User Detection
* Sudo Privilege Abuse Detection
* User Creation Monitoring

### 🚨 Alert Engine

* Threshold-based Detection
* Severity Classification
* Email Notifications
* Slack Integration
* Desktop Notifications

### 📊 Reporting

* CSV Reports
* JSON Reports
* Event Summaries
* Security Statistics

### 🌐 Dashboard

* Failed Login Trends
* Top Attacking IP Addresses
* Alert Timeline
* Incident Overview

---

## 🏗️ Architecture

```text
Linux Authentication Logs
            │
            ▼
     collect_logs.sh
            │
            ▼
      analyze_logs.py
            │
    ┌───────┼────────┐
    ▼       ▼        ▼
 Reports   Alerts  Dashboard
    │       │        │
    └───────┴────────┘
            ▼
       SOC Analyst
```

---

## 🛠️ Technology Stack

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| 🐍 Python         | Log Analysis & Automation       |
| 🐧 Linux          | Security Monitoring Environment |
| ⚙️ Bash           | Log Collection & Automation     |
| 🌐 Flask          | Dashboard Development           |
| 🕒 Cron           | Scheduled Task Execution        |
| 📄 JSON           | Structured Security Reports     |
| 📊 CSV            | Data Export & Reporting         |
| 🔀 Git            | Version Control                 |
| 🛡️ Cybersecurity | Threat Detection & Monitoring   |

---

## 📂 Repository Structure

```text
GhostWatch/
│
├── scripts/
│   ├── collect_logs.sh
│   ├── backup.sh
│   └── cron.conf
│
├── analyzer/
│   ├── analyze_logs.py
│   ├── alerts.py
│   └── ip_reputation.py
│
├── dashboard/
│
├── logs/
│
├── output/
│
├── sample_data/
│
├── tests/
│
└── screenshots/
```

---

## 🎓 Skills Demonstrated

* Security Operations (SOC)
* Linux Administration
* Bash Scripting
* Python Programming
* Incident Detection
* Log Analysis
* Threat Hunting
* Alert Engineering
* Security Automation
* Dashboard Development
* Git & GitHub

---

## 🚀 Future Enhancements

* GeoIP Tracking
* AbuseIPDB Integration
* Docker Deployment
* SIEM Integration
* Elastic Stack Support
* Splunk-Compatible Output

---

## 👨‍💻 Author

**Sunny Dange**

Cybersecurity | SOC | VAPT | Blue Teaming

---

## ⚠️ Disclaimer

This project is intended strictly for educational, research, and defensive cybersecurity purposes. Unauthorized use against systems you do not own or have permission to test is prohibited.
