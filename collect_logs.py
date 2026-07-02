#!/bin/bash

FOLLOW_TIME=7

echo -e "\e[32m====================================================\e[0m"
echo -e "\e[32m      LINUX SOC LOG COLLECTION SCRIPT\e[0m"
echo -e "\e[32m====================================================\e[0m"

echo -e "\n\e[33m[+] ERROR LOGS\e[0m"
timeout $FOLLOW_TIME journalctl -f -p err -n 20 --no-pager

echo -e "\n\e[33m[+] WARNING LOGS\e[0m"
timeout $FOLLOW_TIME journalctl -f -p warning -n 20 --no-pager

echo -e "\n\e[33m[+] SSH LOGS\e[0m"
timeout $FOLLOW_TIME journalctl -f -u ssh -n 20 --no-pager

echo -e "\n\e[33m[+] AUTHENTICATION EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep -Ei "authentication|session opened|session closed"'

echo -e "\n\e[33m[+] PAM EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep -i pam'

echo -e "\n\e[33m[+] FAILED PASSWORD ATTEMPTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep "Failed password"'

echo -e "\n\e[33m[+] SUDO / PRIVILEGE ESCALATION LOGS\e[0m"
timeout $FOLLOW_TIME journalctl -f -t sudo -n 20 --no-pager

echo -e "\n\e[33m[+] ACCOUNT LOCK EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep -i locked'

echo -e "\n\e[33m[+] USER ACCOUNT EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep -Ei "useradd|userdel|usermod"'

echo -e "\n\e[33m[+] SUCCESSFUL LOGIN HISTORY\e[0m"
last

echo -e "\n\e[33m[+] FAILED LOGIN HISTORY\e[0m"
lastb 2>/dev/null

echo -e "\n\e[33m[+] LAST LOGIN INFORMATION\e[0m"
lastlog

echo -e "\n\e[33m[+] KERNEL LOGS\e[0m"
timeout $FOLLOW_TIME journalctl -f -k -n 20 --no-pager

echo -e "\n\e[33m[+] CURRENT BOOT LOGS\e[0m"
journalctl -b -n 20 --no-pager

echo -e "\n\e[33m[+] PREVIOUS BOOT LOGS\e[0m"
journalctl -b -1 -n 20 --no-pager 2>/dev/null

echo -e "\n\e[33m[+] REBOOT HISTORY\e[0m"
last reboot

echo -e "\n\e[33m[+] FAILED SERVICES\e[0m"
systemctl --failed

echo -e "\n\e[33m[+] SERVICE EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep systemd'

echo -e "\n\e[33m[+] NETWORK EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep -Ei "network|eth0|wlan0"'

echo -e "\n\e[33m[+] DNS EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep -i dns'

echo -e "\n\e[33m[+] DHCP EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep -i dhcp'

echo -e "\n\e[33m[+] FIREWALL EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep -Ei "iptables|ufw|firewall"'

echo -e "\n\e[33m[+] OPENVPN EVENTS\e[0m"
timeout $FOLLOW_TIME journalctl -f -u openvpn --no-pager 2>/dev/null

echo -e "\n\e[33m[+] USB DEVICE EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f -k --no-pager | grep -i usb'

echo -e "\n\e[33m[+] MOUNT EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep mount'

echo -e "\n\e[33m[+] DISK EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f -k --no-pager | grep -Ei "disk|filesystem|ext4|sda"'

echo -e "\n\e[33m[+] KERNEL MODULE EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f -k --no-pager | grep module'

echo -e "\n\e[33m[+] PROCESS CRASHES\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep -i segfault'

echo -e "\n\e[33m[+] OUT OF MEMORY EVENTS\e[0m"
timeout $FOLLOW_TIME bash -c 'journalctl -f --no-pager | grep -i "out of memory"'

echo -e "\n\e[33m[+] PACKAGE INSTALLATION HISTORY\e[0m"
grep "install " /var/log/dpkg.log 2>/dev/null

echo -e "\n\e[33m[+] APACHE EVENTS\e[0m"
timeout $FOLLOW_TIME journalctl -f -u apache2 --no-pager 2>/dev/null

echo -e "\n\e[33m[+] NGINX EVENTS\e[0m"
timeout $FOLLOW_TIME journalctl -f -u nginx --no-pager 2>/dev/null

echo -e "\n\e[33m[+] MYSQL EVENTS\e[0m"
timeout $FOLLOW_TIME journalctl -f -u mysql --no-pager 2>/dev/null

echo -e "\n\e[33m[+] REDIS EVENTS\e[0m"
timeout $FOLLOW_TIME journalctl -f -u redis-server --no-pager 2>/dev/null

echo -e "\n\e[31m[+] BRUTE FORCE DETECTION\e[0m"

THRESHOLD=5

journalctl -u ssh --no-pager |
grep "Failed password" |
awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' |
sort |
uniq -c |
while read count ip
do
    if [ "$count" -gt "$THRESHOLD" ]; then
        echo "[ALERT] Possible Brute Force Attack From: $ip ($count Attempts)"
    fi
done

echo -e "\n\e[32m====================================================\e[0m"
echo -e "\e[32m      LOG COLLECTION COMPLETED\e[0m"
echo -e "\e[32m====================================================\e[0m"
```
