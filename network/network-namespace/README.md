# Network Namespace

This guide demonstrates how to create and configure Linux network namespaces, virtual Ethernet (veth) pairs, and bridges.

```sh
# Start a privileged Ubuntu container and install networking tools
docker run -it --privileged --rm \
  -v ./:/mnt/host \
  ubuntu:22.04 bash

ls -la /mnt/host

# install
apt update && apt install -y iproute2 iputils-ping bridge-utils
```

Dockerfile

```sh
# build your custom image
docker build -t ubuntu-netlab:latest .

# run your custom container
docker run -it --rm \
  --privileged \
  -v "$(pwd)":/app \
  ubuntu-netlab bash
```

```sh
# Create two network namespaces: ns1 and ns2
ip netns add ns1
ip netns add ns2

# Verify namespaces have been created
ip netns list

# Display network interfaces inside each namespace
ip netns exec ns1 ip addr
ip netns exec ns1 ip a

ip netns exec ns2 ip addr
ip netns exec ns2 ip a
```

**Debug**

```sh
ip -n ns1 addr
ip -n ns2 addr
ip -n ns1 link
ip -n ns1 neigh
ip netns exec ns1 ping -I veth-ns1 10.0.0.2
ip netns exec ns2 ping -I veth-ns2 10.0.0.1
```

**Clean up**

```sh
ip netns del ns1
ip netns del ns2
```

**Connect Namespace with Host**

```sh
[veth-ns1] <====> [veth-host]

sudo ip link add veth-ns1 type veth peer name veth-host

sudo ip link set veth-ns1 netns ns1

sudo ip netns exec ns1 ip addr add 192.168.10.1/24 dev veth-ns1
sudo ip netns exec ns1 ip link set veth-ns1 up

sudo ip addr add 192.168.10.254/24 dev veth-host
sudo ip link set veth-host up

ping -c 3 192.168.10.1
```

**Connect Namespaces with veth**

```sh
[ns1] veth-ns1 <---- Virtual Cable ----> veth-ns2 [ns2]
```

These two devices are directly connected on the same Layer 2 segment. Before the ping, ns1 will first send an ARP request to find the MAC address for 10.0.0.2. Once the request is resolved over the veth pair, the ICMP packet is sent.


```sh
# Create a veth pair (two connected virtual interfaces)
ip link add veth-ns1 type veth peer name veth-ns2

# Assign each veth endpoint to its respective namespace
ip link set veth-ns1 netns ns1
ip link set veth-ns2 netns ns2

#
ip netns exec ns1 ip link set lo up
ip netns exec ns2 ip link set lo up

# Test
ip netns exec ns1 ping 127.0.0.1
ip netns exec ns2 ping 127.0.0.1

# Configure IP addresses and bring interfaces up in each namespace
ip netns exec ns1 ip addr add 10.0.0.1/24 dev veth-ns1
ip netns exec ns2 ip addr add 10.0.0.2/24 dev veth-ns2

# You must activate it before it can send/receive packets:
ip netns exec ns1 ip link set veth-ns1 up
ip netns exec ns2 ip link set veth-ns2 up

# Test connectivity between namespaces
ip netns exec ns1 ping -c 4 10.0.0.2
ip netns exec ns2 ping -c 4 10.0.0.1
```

**Simulate a Router**

Create a third namespace to act as a router and enable IP forwarding.

**Clean up**

```sh
ip -br link | grep -E 'veth-(ns1|ns2|r1|r2)' && {
  ip link del veth-ns1 2>/dev/null
  ip link del veth-ns2 2>/dev/null
  ip link del veth-r1a 2>/dev/null
  ip link del veth-r2a 2>/dev/null
}
ip netns del ns1 2>/dev/null
ip netns del ns2 2>/dev/null
ip netns del router 2>/dev/null
```

```sh
ns1 (10.0.0.2) <---> router (10.0.0.1 , 10.0.1.1) <---> ns2 (10.0.1.2)
```


```sh
# Clean start (delete old interfaces/namespaces if they exist)
ip -br link | grep -E 'veth-(ns1|ns2|r1|r2)' && {
  ip link del veth-ns1 2>/dev/null
  ip link del veth-ns2 2>/dev/null
  ip link del veth-r1a 2>/dev/null
  ip link del veth-r2a 2>/dev/null
}
ip netns del ns1 2>/dev/null
ip netns del ns2 2>/dev/null
ip netns del router 2>/dev/null

# Create three network namespaces: two hosts (ns1, ns2) and one router
ip netns add ns1
ip netns add ns2
ip netns add router

# Create a veth pair for router <-> ns1
ip link add veth-r1a type veth peer name veth-ns1
ip link set veth-r1a netns router
ip link set veth-ns1 netns ns1

# Create a veth pair for router <-> ns2
ip link add veth-r2a type veth peer name veth-ns2
ip link set veth-r2a netns router
ip link set veth-ns2 netns ns2

# Enable loopback interfaces inside each namespace
ip netns exec router ip link set lo up
ip netns exec ns1 ip link set lo up
ip netns exec ns2 ip link set lo up

# Assign IP addresses to router interfaces (separate subnets)
# Router
# ns1 <-> router network
ip netns exec router ip addr add 10.0.0.1/24 dev veth-r1a
# ns2 <-> router network
ip netns exec router ip addr add 10.0.1.1/24 dev veth-r2a

ip netns exec router ip link set veth-r1a up
ip netns exec router ip link set veth-r2a up

# Check router's IP forwarding setting
# Topology: ns1 (10.0.0.2) <---> router (10.0.0.1 , 10.0.1.1) <---> ns2 (10.0.1.2)
# Should be 0 by default
ip netns exec router sysctl net.ipv4.ip_forward
# This will fail because forwarding is off
ip netns exec ns1 ping 10.0.1.2

# Enable IP forwarding on the router to allow packet routing
ip netns exec router sysctl -w net.ipv4.ip_forward=1 >/dev/null
# Will still fail until routes are set
ip netns exec ns1 ping 10.0.1.2

# Configure ns1 (10.0.0.0/24 side)
# Assign IP to ns1
ip netns exec ns1 ip addr add 10.0.0.2/24 dev veth-ns1
# Bring interface up
ip netns exec ns1 ip link set veth-ns1 up
# Set default route so ns1 sends packets to router
ip netns exec ns1 ip route add default via 10.0.0.1
# Verify routing table
ip netns exec ns1 ip route

# Configure ns2 (10.0.1.0/24 side)
# Assign IP to ns2
ip netns exec ns2 ip addr add 10.0.1.2/24 dev veth-ns2
# Bring interface up
ip netns exec ns2 ip link set veth-ns2 up
# Set default route via router
ip netns exec ns2 ip route add default via 10.0.1.1

# Final connectivity test: ping from ns1 to ns2 through router
ip netns exec ns1 ping -c 4 10.0.1.2
ip netns exec ns2 ping -c 4 10.0.0.2
```


```sh
[ ns1 namespace ]
  veth1 (192.168.0.1/24)
      │
      │ Virtual Cable
      │
  veth1-br
      │
[ br0 ＝ Linux Bridge ] ← Other virtual or physical NICs can also be connected here
      │
   (Host)
```


```sh
# Create a bridge named br0 on the host
ip link add name br0 type bridge
ip link set br0 up

# Create another veth pair to connect namespace ns1 to the bridge
ip link add veth1 type veth peer name veth1-br

# Move one end (veth1) into namespace ns1 and attach the other (veth1-br) to the bridge
ip link set veth1 netns ns1
ip link set veth1-br master br0
ip link set veth1-br up

# Inside ns1: configure IP on veth1 and bring it up
ip netns exec ns1 ip addr add 192.168.0.1/24 dev veth1
ip netns exec ns1 ip link set veth1 up

# (Optional) From host: verify bridge and namespace connectivity
ip addr show br0
ip addr add 192.168.0.254/24 dev br0
ip netns exec ns1 ping -c 4 192.168.0.254
```