import subprocess

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

run("ip netns add ns1")
run("ip netns add ns2")
run("ip netns list")
run("ip link add veth1 type veth peer name veth2")
run("ip link set veth1 netns ns1")
run("ip link set veth2 netns ns2")