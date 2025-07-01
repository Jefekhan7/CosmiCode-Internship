
 -   Edited the **`snort.lua`** configuration file to set up network variables and rule paths.
        


        `sudo nano /usr/local/etc/snort/snort.lua` 
        

        `ips =
        {
          ...
          rules = [[./rules/local.rules]] }` 
        
2.  **Created Custom IDS Rules:**
    
    -   Edited the `local.rules` file to add a basic rule. For example:
        
        bash
        
        CopyEdit
        
        `sudo nano /usr/local/etc/snort/rules/local.rules`
        
        `alert icmp any  any -> any  any (msg:"ICMP Packet Detected"; sid:1000001; rev:1;)` 
        
 **Ran Snort in IDS Mode:**
    
    -   Started Snort using the `.lua` configuration file:
   
        
        `sudo snort -c /usr/local/etc/snort/snort.lua -R /usr/local/etc/snort/rules/local.rules -i eth0` 
        
        _(Replace `eth0` with your network interface name.)_
        
  **Tested Detection:**
    
  -   Generated ICMP traffic (ping) to trigger the custom rule:
 
        
        `ping google.com` 
        
    -   Verified that Snort detected the packet and displayed an alert in the console.
        
5.  **Captured Screenshots:**
    
    -   The terminal showing Snort running.
            
  -   The alert output when traffic was detected.
            

 **Result:**

Snort 3.x was installed and configured successfully. Custom IDS rules were implemented using a `.lua` configuration and `local.rules` file. Snort detected test ICMP traffic and generated alerts as expected. Screenshots were captured for documentation.
