from scapy.all import sniff, TCP

syn_counter = {}

def detect_syn(pkt):
    if pkt.haslayer(TCP) and pkt[TCP].flags == "S":
        key = (pkt[IP].src, pkt[TCP].dport)
        syn_counter[key] = syn_counter.get(key, 0) + 1
        if syn_counter[key] > 20:
            print("[ALERT] SYN flood-ish?", key, syn_counter[key])