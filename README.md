<div align="center">

<pre style="color: #00ff41;">
 _______  _______  _______  __   __  __    _  _______  __   __  _______ 
|       ||       ||       ||  | |  ||  |  | ||       ||  | |  ||       |
|_     _||    ___||       ||  |_|  ||   |_| ||   _   ||  |_|  ||   _   |
  |   |  |   |___ |       ||       ||       ||  | |  ||       ||  | |  |
  |   |  |    ___||      _||       ||  _    ||  |_|  ||       ||  |_|  |
  |   |  |   |___ |     |_ |   _   || | |   ||       | |     | |       |
  |___|  |_______||_______||__| |__||_|  |__||_______|  |___|  |_______|
</pre>

**SOC Command Center // Live Enterprise Log Analysis**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://www.kernel.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Red_Team_Aware-ff003c?style=for-the-badge&logo=hackthebox&logoColor=white)](#)

</div>

<br>

## 🔍 Overview

**TECHNOVA** is a lightweight, real-time Security Operations Center (SOC) dashboard engineered for Linux environments. Built with a deep understanding of offensive security methodologies and vulnerability assessment, this tool shifts to the defensive side to actively monitor enterprise infrastructure. 

It tracks critical authentication events, identifies potential brute-force attacks in real-time, and isolates privilege escalation attempts, wrapping complex system data into a highly responsive, cinematic retro-CRT web interface.

## 🎯 Project Impact
*   **Proactive Threat Detection:** Automatically flags repetitive failed authentication attempts to catch brute-force network attacks early.
*   **Infrastructure Hardening:** Monitors Role-Based Access Control (RBAC) integrity by actively tracking `sudo` escalations and user account modifications.
*   **Zero-Overhead Logging:** Avoids bloated third-party logging agents by natively parsing Linux system services (`journalctl`, `pam`, `lastb`).

---

## 🛠️ Technology Stack

### Core Infrastructure & Security
*   **Enterprise Linux Administration:** System hardening, native service querying.
*   **Log Management:** `systemd` (Journalctl), Pluggable Authentication Modules (PAM).
*   **Network Analysis:** Brute-force threshold tracking, active SSH session monitoring.

### Backend Application
*   **Python 3:** Core execution logic and subprocess management.
*   **Flask:** Lightweight WSGI web application framework bridging local system logs to the web interface via RESTful API endpoints.

### Frontend UI/UX
*   **HTML5 / CSS3 / JavaScript:** Core structural layout and dynamic DOM manipulation.
*   **Tailwind CSS:** Rapid, utility-first UI styling for responsive grid layouts.
*   **Retro-Aesthetic Design:** Custom CSS keyframes and scanline filters for a cinematic "green-on-black" hacker aesthetic.

---

## 📸 Interface Sneak Peek

![TECHNOVA Dashboard Demo](Technova_panel)

---

## 🏗️ Architecture

1.  **The Engine:** A secure background collector querying the Linux kernel, PAM modules, and authentication logs natively.
2.  **The API Bridge:** A Python Flask backend that spins up the collector in an isolated thread, formats the raw text into structured JSON, and buffers the latest events.
3.  **The Interface:** A vanilla JS frontend that polls the API, dynamically rendering alerts and logs while updating visual statistical trackers in real-time.

---

## ⚙️ Installation & Deployment

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/technova-soc-dashboard.git](https://github.com/yourusername/technova-soc-dashboard.git)
cd technova-soc-dashboard
