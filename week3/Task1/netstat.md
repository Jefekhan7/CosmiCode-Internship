**Task 1:**

**Harden a Linux system by disabling unnecessary services and ports:**

**System Services:**
Unnecessary background services can become security risks because they provide extra ways for attackers to break in. By stopping and disabling unused services, we reduce these risks and strengthen the system’s security.

List currently running services:

sudo systemctl list-units --type=service --state=running

Found that bluetooth service is running, but i dont need theis service for now so i will disable it by using the following commonds.

systemctl stop bluetooth.service


systemctl disable bluetooth.service

The stop option stop the service for now and disable option keep it inactive after the system boot.

#GeeksforGeeks is used for knowledge about systemctl
https://www.geeksforgeeks.org/linux-unix/systemctl-in-unix/

**Open Ports**
Even if the services is blocked we can block the open ports by using firewall rules so to avoid any point of attack.

I will netstat to check for ports that are listening for a connection and check if it is useful for me now or not other wise i'll block/close it from the firewall using ufw tool.

netstat -tuln

I get the result from this commond show in the result.png file attached. The result shows that the system is listening on port 80 for http connection from any remote IP.

**by using the commond**

netstate -tulnp | grep 80

it show the process id and services running on it. so i found out that apache2 is running and listenting on this port.

ufw deny 80/tcp 

by using this any one connecting to this port will not allow by the firewall even if the service is running.



