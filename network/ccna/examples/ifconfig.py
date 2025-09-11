import subprocess


# ifconfig
def get_ifconfig():
    result = subprocess.run(['ifconfig'], capture_output=True, text=True)
    print(result.stdout)


def get_ipv4_addresses():
    result = subprocess.run("ifconfig | grep 'inet ' | grep -v 127.0.0.1",
                            shell=True, capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")
    for line in lines:
        parts = line.split()
        print("IPv4 Address:", parts[1])


if __name__ == "__main__":
    get_ifconfig()
    print("=" * 60)
    get_ipv4_addresses()