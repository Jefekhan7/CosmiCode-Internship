import re
import os
import subprocess

ips = ""
pattern = r'from (\d+\.\d+\.\d+\.\d+)'
with open("/var/log/auth.log","r") as file:
          for line in file.readlines():
              if "Failed " in line:
                  match = re.search(pattern,line)
                  ips += match.group(1) + "\n"
          if ips:
              with open("sus_ips.txt","w+") as f:
                  f.write(ips)
              p1 = subprocess.Popen(['sort','sus_ips.txt'],stdout=subprocess.PIPE)
              p2 = subprocess.Popen(['uniq','-c'],stdin = p1.stdout, stdout = subprocess.PIPE)
              output, _  = p2.communicate()
              content = ""
              with open("sus_ips.txt","w") as f:
                 content = output.decode()
                 f.write(content)
              print("Appeared ","ipAddress")
              print(content)
              
              print("IP's Appeared in /var/log/auth.log due to Failed attempts  ")

          else:
              print("No! suspicious ip found. ")
