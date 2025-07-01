**Task 2:**

Wireshark was started on the `eth0` interface. I let Wireshark capture live network traffic while I performed various activities to generate traffic. During this session, I browsed multiple websites and connected to a local server on my Linux machine from my Windows machine using the `python -m http.server` command. After generating sufficient network activity, I stopped the capture to review the collected packets for any unusual patterns or potential security issues.

**Wireshark Findings**


- During the capture session, I observed two local IP addresses actively communicating: `192.168.100.1` and `192.168.100.234`.
- According to the Endpoints summary:
  - `192.168.100.1` received 24 packets (2 KB) but did not send any packets during the capture.
  - `192.168.100.234` sent 24 packets (2 KB) but did not receive any packets back.
- This traffic likely represents the connection between my Windows machine and the local Linux server (`python -m http.server`).
- No unusual or suspicious traffic patterns were detected in this basic test — the traffic direction matches the expected behavior of a client sending requests and a server responding.

The screenshot of the capture is present in the file.

