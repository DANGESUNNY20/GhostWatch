#!/bin/bash

# ====================================================
# TECHNOVA SOC Command Center - Startup Script
# Author: Sunny Dange
# ====================================================

echo -e "\e[32m====================================================\e[0m"
echo -e "\e[32m      INITIALIZING TECHNOVA COMMAND CENTER\e[0m"
echo -e "\e[32m====================================================\e[0m"
#!/bin/bash

apt-get update
apt-get install python3-venv python3-pip -y

python3 -m venv soc_env
soc_env/bin/pip install -r requirements.txt

chmod +x collect_logs_2.sh
chmod +x start_technova.sh

echo "[Unit]" > /etc/systemd/system/technova.service
echo "Description=TECHNOVA SOC Command Center" >> /etc/systemd/system/technova.service
echo "After=network.target" >> /etc/systemd/system/technova.service
echo "" >> /etc/systemd/system/technova.service
echo "[Service]" >> /etc/systemd/system/technova.service
echo "User=root" >> /etc/systemd/system/technova.service
echo "WorkingDirectory=/home/socproject" >> /etc/systemd/system/technova.service
echo "ExecStart=/home/socproject/soc_env/bin/python3 /home/socproject/app.py" >> /etc/systemd/system/technova.service
echo "Restart=always" >> /etc/systemd/system/technova.service
echo "RestartSec=5" >> /etc/systemd/system/technova.service
echo "" >> /etc/systemd/system/technova.service
echo "[Install]" >> /etc/systemd/system/technova.service
echo "WantedBy=multi-user.target" >> /etc/systemd/system/technova.service

systemctl daemon-reload
systemctl enable technova.service
systemctl start technova.service

echo "installation finished!"
