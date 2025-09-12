# Network Namespace

This guide demonstrates how to create and configure Linux network namespaces, virtual Ethernet (veth) pairs, and bridges.

```sh
# Start a privileged Ubuntu container and install networking tools
docker run -it --privileged --rm ubuntu:22.04 bash

# install
apt update && apt install -y iproute2 iputils-ping bridge-utils
```

```sh
# Create two network namespaces: ns1 and ns2
ip netns add ns1
ip netns add ns2

# Verify namespaces have been created
ip netns list

# Display network interfaces inside each namespace
ip netns exec ns1 ip addr
ip netns exec ns2 ip addr
```

Debug

```sh
ip -n ns1 addr
ip -n ns2 addr
ip -n ns1 link
ip -n ns1 neigh
ip netns exec ns1 ping -I veth-ns1 10.0.0.2
ip netns exec ns2 ping -I veth-ns2 10.0.0.1
```

Clean up

```sh
ip netns del ns1
ip netns del ns2
```

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

# Configure IP addresses and bring interfaces up in each namespace
ip netns exec ns1 ip addr add 10.0.0.1/24 dev veth-ns1
ip netns exec ns1 ip link set veth-ns1 up

ip netns exec ns2 ip addr add 10.0.0.2/24 dev veth-ns2
ip netns exec ns2 ip link set veth-ns2 up

# Test connectivity between namespaces
ip netns exec ns1 ping -c 4 10.0.0.2
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