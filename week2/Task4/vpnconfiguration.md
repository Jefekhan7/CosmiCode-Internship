
I used VPN services provided by Proton VPN. They provided me with a **WireGuard** configuration file for connecting through the **WireGuard protocol**.

I ran WireGuard using the following command:


`sudo wg-quick up protonvpn-wg` 

After this, I tested the connection by pinging Google:=

`ping -c 4 google.com` 

The connection was working fine and the ping was successful.

I checked my IP address using [ipinfo.io](https://ipinfo.io) and confirmed that my IP changed from Pakistan to California.  
The IP information was as follows:

**Old IP:** `182.189.120.109`  
**New IP:**

json

CopyEdit

`{  "ip":  "146.70.230.149",  "city":  "Los Angeles",  "region":  "California",  "country":  "US",  "loc":  "34.0443,-118.2509",  "org":  "AS9009 M247 Europe SRL",  "postal":  "90014",  "timezone":  "America/Los_Angeles"  }` 

**Ping result:**


`PING google.com (142.250.189.14) 56(84) bytes of data.
64 bytes from 142.250.189.14: icmp_seq=1 ttl=118 time=502 ms

--- google.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 501.539/501.539/501.539/0.000 ms` 

**Result:** The VPN connection was successful, the IP address changed, and network connectivity was verified.
