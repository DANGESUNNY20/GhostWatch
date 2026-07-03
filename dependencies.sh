#!/bin/bash

# ====================================================
# TECHNOVA SOC Command Center - Startup Script
# Author: Sunny Dange
# ====================================================

echo -e "\e[32m====================================================\e[0m"
echo -e "\e[32m      INITIALIZING TECHNOVA COMMAND CENTER\e[0m"
echo -e "\e[32m====================================================\e[0m"
if [ ! -d "soc_env" ]; then
    echo -e "\n\e[33m[!] Virtual environment 'soc_env' not found. Creating it now...\e[0m"
    python3 -m venv soc_env
    echo -e "\e[32m[+] Virtual environment created successfully.\e[0m"
else
    echo -e "\n\e[34m[*] Virtual environment 'soc_env' located.\e[0m"
fi
echo -e "\e[34m[*] Verifying requirements...\e[0m"
source soc_env/bin/activate
pip install -r requirements.txt --disable-pip-version-check -q
echo -e "\e[32m[+] Dependencies verified.\e[0m"
if [ ! -x "collect_logs_2.sh" ]; then
    echo -e "\e[33m[*] Granting execution permissions to log collector...\e[0m"
    chmod +x collect_logs_2.sh
fi
echo -e "\n\e[31m[!] Administrative privileges required to read system logs.\e[0m"
echo -e "\e[32m[+] Launching Python Flask Backend...\e[0m"

sudo ./soc_env/bin/python3 app.py
