\# Prodigy CS-05

\### 🛡️ Python Packet Sniffer

A simple packet sniffer tool built using Python and Scapy. This tool captures and displays essential network packet details like IP addresses, ports, protocol types, and raw payloads in real-time.



---



\### 📂 Project Structure

packet\_sniffer.py     # Main Python script

README.md             # This file



\### ⚙️ Requirements

Python 3.x



Scapy library



You can install Scapy using pip:



bash



pip install scapy

⚠️ On Windows, Scapy may require Npcap or WinPcap to work properly. Download and install from:



https://nmap.org/npcap/



\### 🚀 How to Run

python packet\_sniffer.py

You may need to run the script with administrator/root privileges depending on your OS:



Windows (Admin Command Prompt):



python packet\_sniffer.py

Linux/macOS:



sudo python3 packet\_sniffer.py



\### 📡 Features

Captures all IP-based packets.



Supports both TCP and UDP protocols.



Displays:



Timestamp



Source \& Destination IP



Source \& Destination Ports



Protocol Type



First 100 bytes of raw payload



\### 🧪 Sample Output

============================================================

\[2025-07-09 21:45:12] Packet Captured

Source IP      : 20.189.173.12

Destination IP : 8.8.8.8

Protocol       : 6

Protocol Type  : TCP

Source Port    : 54321

Dest Port      : 80

Payload (raw)  : b'GET / HTTP/1.1\\r\\nHost: example.com\\r\\n\\r\\n'





\### ⚠️ Legal Disclaimer

This tool is intended only for educational or authorized testing purposes on networks you own or have permission to analyze. Unauthorized sniffing is illegal and unethical.



\### 👨‍💻 Author

Mohamed Shadhil H

B.Tech Cyber Security | Crescent Institute of Science and Technology



