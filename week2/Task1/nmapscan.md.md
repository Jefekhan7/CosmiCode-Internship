**Task 1:**
**Command:**
 sudo nmap -A -T4 192.168.1.0/24 -oN network_scan.txt

This command performs an aggressive scan on the network.

- The `-A` option enables aggressive scanning to identify the operating system, detect service versions, run Nmap scripts, and perform a traceroute to map the network path.
- The `-T4` option sets a faster execution speed, making the scan quicker (but less stealthy).
- The `-oN network_scan.txt` option saves the output summary to a file called `network_scan.txt` for later analysis.

This helps gather detailed information about devices and services on the local network.



