# 1. tcpdump - Capture network packets
sudo tcpdump -i any icmp

OUTPUT:
IP 192.168.1.5 > 8.8.8.8: ICMP echo request
IP 8.8.8.8 > 192.168.1.5: ICMP echo reply

# 2. netstat - Display network connections and statistics
netstat -an

OUTPUT:
Active Internet connections
Proto  Local Address     Foreign Address   State
tcp    127.0.0.1:631     0.0.0.0:*         LISTEN

# 3. ifconfig - Display network interface configuration
ifconfig

OUTPUT:
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>
      inet 192.168.1.5
      netmask 255.255.255.0

# 4. nslookup - Find DNS information
nslookup google.com

OUTPUT:
Server:  8.8.8.8
Name:    google.com
Address: 142.250.190.14

# 5. traceroute - Trace the route to a destination
traceroute google.com

OUTPUT:
traceroute to google.com
1  192.168.1.1
2  10.0.0.1
3  142.250.190.14

# 6. Capture ping packets using tcpdump
sudo tcpdump -i any icmp

OUTPUT:
PING google.com
64 bytes from 142.250.190.14: icmp_seq=1 ttl=117 time=15 ms
64 bytes from 142.250.190.14: icmp_seq=2 ttl=117 time=14 ms

4 packets transmitted, 4 received, 0% packet loss

# Open another terminal and run:
ping -c 4 google.com

# 7. Capture traceroute packets using tcpdump
sudo tcpdump -i any 'icmp or udp'

# Open another terminal and run:
traceroute google.com
