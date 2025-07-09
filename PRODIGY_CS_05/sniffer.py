from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

def packet_callback(packet):
    print("="*60)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Packet Captured")

    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source IP      : {ip_layer.src}")
        print(f"Destination IP : {ip_layer.dst}")
        print(f"Protocol       : {ip_layer.proto}")

        # TCP or UDP layer check
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            print("Protocol Type  : TCP")
            print(f"Source Port    : {tcp_layer.sport}")
            print(f"Dest Port      : {tcp_layer.dport}")
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            print("Protocol Type  : UDP")
            print(f"Source Port    : {udp_layer.sport}")
            print(f"Dest Port      : {udp_layer.dport}")

        # Raw payload data
        if packet.haslayer(Raw):
            print(f"Payload (raw)  : {bytes(packet[Raw].load)[:100]}")  # First 100 bytes

    else:
        print("Non-IP Packet")

# Start sniffing
print("[*] Starting Packet Sniffer (Press Ctrl+C to stop)...")
sniff(prn=packet_callback, store=False)
