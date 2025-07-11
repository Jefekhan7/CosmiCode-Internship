**Setup Apache Server on Linux**

Commonds:

sudo apt update
sudo apt install apache2

sudo systemctl start apache2

Apache2 server is start on the system i can access the server file a simple form in html on my browser through http://localhost



**Configuration Setup**

The main configuration file for apache is stored in the file :

/etc/apache/apache2.conf 

By Reviewing the configuration files and the server files There are some default configuration that need to be changes some module to be disabled for security practices.

**By using:** 
Apache2ctl -M 
show the module apache2 is using in which the autoindex that list direcotory and the status_module need to be disabled.

**To disabled these module:**
sudo a2dismod autoindex
sudo a2dismod status


**More Configuration:**

-   **Directory Listing Disabled:**  
    Updated Apache config to disable directory listing (`Options -Indexes`). Now, folders without an index file return **403 Forbidden** instead of listing files.
    
-   **Server Banner Hidden:**  
   et `ServerTokens Prod` and `ServerSignature Off` in the Apache config. This hides version and OS info from HTTP headers and error pages.

**Scan for Common Vulnerabilities**

We’ll use  tools:  
1️⃣ **Nikto** — for web server & config vulnerabilities  
2️⃣ **Nmap** — to see open ports & service versions


**Nmap:**
nmap -sV -p 1-65535 localhost

will scan all the port and the service running on it and detect the version they are using.

**nikto:**
nikto -h http://localhost


The result of both test is attached:

**Possible fixed and patches:**

apt upgrade 
apt upgrade apache2

we already have apply configuration setting so thats not showing.

nmap was showing unused services like golang 
so:
sudo lsof -i :37771
sudo kill <PID>






