**Task 3:**

I opened a terminal on my Linux system and configured a basic firewall rule using `iptables` to allow SSH traffic.  
To do this, I ran the following command to add a rule that permits incoming TCP traffic on port **22** (the default SSH port):

```bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

sudo iptables-save

sudo iptables -L

