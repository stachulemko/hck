from scapy.all import IP, TCP, send, sr1
i = 22
p = sr1(IP(dst="192.168.1.46")/TCP(sport=666, dport=i, flags="S"))
value = str(p[TCP].flags)
if value == "SA":
    print(f"port open : {i}")
