import subprocess, sys
from ipaddress import ip_network


def ping_sweep(ip: str, timeout_ms=800) -> bool:
    try:
        """
        -c 1: Send 1 packet.
        -W 0.8: Timeout of 0.8 seconds.

        Return code 0 → Host responded → Up.
        Any other code → Host didn't respond → Down.
        """
        cmd = ['ping', '-c', '1', '-W', str(int(timeout_ms/1000)), ip]
        return subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    except Exception:
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ping_sweep.py 192.168.1.0/24")
        sys.exit(1)

    net = ip_network(sys.argv[1], strict=False)
    print(f"Scanning {net} ...")
    up = []

    print("net.hosts():", net.hosts)
    print("len(net.hosts()):", len(list(net.hosts())))

    for host in net.hosts():
        ip = str(host)
        if ping(ip):
            up.append(ip)
            print(f"[UP]   {ip}")
        else:
            print(f"[DOWN] {ip}")
    print("\nActive hosts:")
    for ip in up: print(ip)
