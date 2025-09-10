from scapy.all import IP, ICMP, sr1, ARP, Ether, srp, TCP, sniff, DHCP, BOOTP, DNS, DNSQR
from ipaddress import ip_network
import dns.resolver
from ipaddress import ip_network, ip_address
import random

"""
Note: You may need to run this script with elevated privileges (e.g., using sudo on Unix-based systems)
"""


def print_break():
    print("=" * 60)


def ping_host(dst="8.8.8.8", timeout=2):
    """
    Send an ICMP ping to a target host and display the response details.
    This Python code is using Scapy to send an ICMP packet (like a ping)
    to Google's public DNS server (8.8.8.8) and then display the details of the reply.

    Ethernet → IP → ICMP → Data

    IP Layer
    └─ ICMP Layer

    ifconfig | grep "inet " | grep -v 127.0.0.1
    """
    p = IP(dst=dst)/ICMP()
    r = sr1(p, timeout=timeout, verbose=False)
    if r:
        print("L3 Src/Dst:", r[IP].src, "->", r[IP].dst)     # L3 Src/Dst: 8.8.8.8 -> 192.168.1.xxx
        print("ICMP type/code:", r[ICMP].type, r[ICMP].code) # ICMP type/code: 0 0
        return r
    else:
        print(f"No response from {dst}")
        return None


def subnet_info(cidr: str):
    net = ip_network(cidr, strict=False) # Network Object
    hosts = list(net.hosts())
    print("CIDR:", cidr)
    # print("net:", net)
    # print("hosts:", hosts)

    print("Network:", net.network_address)
    print("Broadcast:", net.broadcast_address)
    print("Mask:", net.netmask, "(Prefix:", net.prefixlen, ")")
    print("Host count:", len(hosts))
    print("First/Last host:", hosts[0], hosts[-1])


def arp_resolve(target_ip, iface=None):
    """
    Your PC
    ↓
    Broadcast message:
    "Who has the IP address 192.168.1.1? Please tell me your MAC address!"

    The device with IP address 192.168.1.1 (e.g., a router)
    ↑
    Reply:
    "My MAC address is xx:xx:xx:xx:xx."
    """
    print("Resolving ARP for:", target_ip)
    # Create ARP request packet
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target_ip)

    # Send the packet and receive the response at Layer 2
    ans, unans = srp(pkt, timeout=2, iface=iface, verbose=False)

    # Print the resolved MAC address
    for s, r in ans:
        print(r.psrc, "=>", r.hwsrc)  # IP -> MAC


"""
| **Hop Count** | **Status**        | **Description**                                                 |
| ------------- | ----------------- | --------------------------------------------------------------- |
| **1–5**       | **Very Close**    | Communication within the same LAN or the same metropolitan area |
| **6–10**      | **Normal**        | Communication within the same country or domestic networks      |
| **11–15**     | **Somewhat High** | Communication across international lines or large-scale ISPs    |
| **16–30**     | **High**          | Long-distance communication (overseas access) or complex routes |
"""
def traceroute_host(dst="8.8.8.8", max_hops=30):
    """
    Traceroute works by sending packets with gradually increasing TTL values.
    Each router that handles the packet decrements the TTL by 1.
    When the TTL reaches 0, the router discards the packet and sends back an ICMP "Time Exceeded" message to the sender.
    """
    for ttl in range(1, max_hops+1):

        # Create an IP packet with the specified TTL
        p = IP(dst=dst, ttl=ttl)/ICMP() # TTL (Time To Live)

        # Send the packet and wait for a response
        r = sr1(p, timeout=1, verbose=False)

        # Check if we received a response
        if r:
            print(ttl, r.src)

            if r.src == dst:
                break
        else:
            print(ttl, "*")


def dns_lookup(name="www.example.com"):
    """
    Perform DNS lookups for various record types (A, AAAA, NS, MX,
    TXT) using the dnspython library.
    """
    for qtype in ["A", "AAAA", "NS", "MX", "TXT"]:
        try:
            ans = dns.resolver.resolve(name, qtype)
            print(qtype, [r.to_text() for r in ans])
        except Exception as e:
            print(qtype, "->", e)



def acl_match(pkt):
    """
    The basics of ACLs are "permit or deny when the conditions match."
    """
    # ACL Rule Example: (src, dst, dport, action)
    ACL = [
        ("10.0.0.0/8", "192.168.1.100/32", 22, "permit"),
        ("0.0.0.0/0", "0.0.0.0/0", 22, "deny"),
    ]

    if IP not in pkt or TCP not in pkt:
        return "permit"
    src = ip_address(pkt[IP].src)
    dst = ip_address(pkt[IP].dst)
    dport = pkt[TCP].dport
    for src_cidr, dst_cidr, port, action in ACL:
        if src in ip_network(src_cidr) and dst in ip_network(dst_cidr) and dport == port:
            return action
    return "permit"


class SimpleNAT:
    def __init__(self, public_ip):
        self.public_ip = public_ip
        self.table = {}  # (priv_ip, priv_port) -> (pub_ip, pub_port)
        self.rev = {}    # reverse lookup

    def translate_outbound(self, priv_ip, priv_port):
        key = (priv_ip, priv_port)
        if key not in self.table:
            pub_port = random.randint(20000, 60000)
            self.table[key] = (self.public_ip, pub_port)
            self.rev[(self.public_ip, pub_port)] = key
        return self.table[key]

    def translate_inbound(self, pub_ip, pub_port):
        return self.rev.get((pub_ip, pub_port), None)


def handle(pkt):
    if DHCP in pkt and BOOTP in pkt:
        print("[DHCP]", pkt[BOOTP].yiaddr, pkt[DHCP].options)
    if pkt.haslayer(DNS) and pkt.haslayer(DNSQR) and pkt[DNS].qr == 0:
        print("[DNS-Query]", pkt[DNSQR].qname.decode(errors="ignore"))
    if TCP in pkt and pkt[TCP].dport == 80:
        print("[HTTP-Req?]", pkt[IP].src, "->", pkt[IP].dst)


if __name__ == "__main__":
    print("Ping Test: 8.8.8.8")
    ping_host("8.8.8.8")
    print_break()
    print("Subnet Info for /24:")
    subnet_info("192.168.1.0/24")
    print_break()
    print("Subnet Info for /27:")
    subnet_info("192.168.1.0/27")
    print_break()

    arp_resolve("192.168.1.1")
    print_break()
    arp_resolve("192.168.1.2")
    print_break()

    traceroute_host("8.8.8.8");
    print_break()

    dns_lookup("google.com")
    print_break()

    p = IP(src="10.1.2.3", dst="192.168.1.100")/TCP(dport=22)
    print("ACL match:", acl_match(p))
    print_break()

    nat = SimpleNAT("203.0.113.5")
    print(nat.translate_outbound("192.168.1.10", 54321))  # → (203.0.113.5, X)
    print_break()

    sniff(filter="udp or tcp", prn=handle, iface="en0", store=False)
    print_break()



