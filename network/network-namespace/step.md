# Network Namespace

## Connect Namespace with Host

```sh
[veth-ns1] <====> [veth-host]

ip netns add ns1

ip link add veth-ns1 type veth peer name veth-host

ip link set veth-ns1 netns ns1

ip netns exec ns1 ip addr add 192.168.10.1/24 dev veth-ns1
ip netns exec ns1 ip link set veth-ns1 up

# Assigns IP 192.168.10.254 to the host-side interface.
# The host-side interface (veth-host) needs an IP address
# because it acts as the gateway or endpoint for communication between the host and the network namespace (ns1).
ip addr add 192.168.10.254/24 dev veth-host
ip link set veth-host up

ping -c 3 192.168.10.1
```

## Connect Namespaces with veth

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

# Enable loopback interfaces
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

## Simulate a Router (NS1 <-> Router <-> NS2)

Create a third namespace to act as a router and enable IP forwarding.

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

## Simulate a Bridge (NS1 -> Host)

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

## Simulate a Bridge (NS1 <-> NS2)

Docker and Kubernetes use Linux bridges internally.
This step connects multiple namespaces through a bridge, mimicking a Layer 2 switch.

```sh
ns1(192.168.0.1)     ns2(192.168.0.2)
       │                   │
       └── veth pair ──────┘
               │
             [br0] (Linux Bridge)

ns1 (veth1) <-- virtual cable --> (veth1-br) --┐
                                               │
ns2 (veth2) <-- virtual cable --> (veth2-br) --┤
                                               │
                                           [ br0 ]
                                           (Linux bridge = virtual switch)
```

```sh
# Cleanup
ip netns del ns1 2>/dev/null
ip netns del ns2 2>/dev/null
ip link del br0 2>/dev/null

# Create namespaces
ip netns add ns1
ip netns add ns2

# Create the bridge(L2)
ip link add name br0 type bridge
ip link set br0 up

# Connect ns1
# ns1 (veth1) <--cable--> (veth1-br) -- [br0]
ip link add veth1 type veth peer name veth1-br
ip link set veth1 netns ns1
ip link set veth1-br master br0
ip link set veth1-br up

# Connect ns2
ip link add veth2 type veth peer name veth2-br
ip link set veth2 netns ns2
ip link set veth2-br master br0
ip link set veth2-br up

# Assign IPs
ip netns exec ns1 ip addr add 192.168.0.1/24 dev veth1
ip netns exec ns2 ip addr add 192.168.0.2/24 dev veth2
ip netns exec ns1 ip link set veth1 up
ip netns exec ns2 ip link set veth2 up
ip netns exec ns1 ip link set lo up
ip netns exec ns2 ip link set lo up

# Test
ip netns exec ns1 ping -c 3 192.168.0.2
```

## Experiment with NAT (Simulate Internet Access)

Use iptables to NAT packets so private IPs can access the external network — like a home router or cloud VPC.

```sh
ns1 (192.168.1.2)
   │
   │ private subnet
   │
router namespace
 ┌────────────────────────────┐
 │ veth-ns1: 192.168.1.1/24   │  ← Internal interface
 │ eth0:     172.17.0.2/16    │  ← External interface (Host network)
 └────────────────────────────┘
   │
 Host network (e.g., Docker bridge)
   │
Internet

ns1(192.168.1.2) → router(192.168.1.1) → eth0(172.17.0.2)

192.168.1.2:12345 → 172.17.0.2:54321

ns1(192.168.1.2) <--veth--> (192.168.1.1)router(10.0.0.1) <--veth--> (10.0.0.2)nswan
                        [Internal]                         [External]

```

```sh
# Create network namespaces
# Client (private side)
ip netns add ns1
# Router (NAT device)
ip netns add router
 # External world (Internet side)
ip netns add nswan

# ns1 <-> router (internal subnet)
ip link add veth-ns1 type veth peer name veth-r1a
ip link set veth-ns1 netns ns1
ip link set veth-r1a netns router

# router <-> nswan (external subnet)
ip link add veth-r2a type veth peer name veth-wan
ip link set veth-r2a netns router
ip link set veth-wan netns nswan

# Enable loopback interfaces
ip netns exec ns1    ip link set lo up
ip netns exec router ip link set lo up
ip netns exec nswan  ip link set lo up

# ns1 side (internal side)
ip netns exec ns1 ip addr add 192.168.1.2/24 dev veth-ns1
ip netns exec ns1 ip link set veth-ns1 up

# router side: internal interface and external interface
ip netns exec router ip addr add 192.168.1.1/24 dev veth-r1a
ip netns exec router ip addr add 10.0.0.1/24   dev veth-r2a
ip netns exec router ip link set veth-r1a up
ip netns exec router ip link set veth-r2a up

# nswan side (external world)
ip netns exec nswan ip addr add 10.0.0.2/24   dev veth-wan
ip netns exec nswan ip link set veth-wan up

# ns1: set default gateway to router (192.168.1.1)
ip netns exec ns1 ip route add default via 192.168.1.1

# nswan: set return route to router (10.0.0.1)
# Here, for simplicity, we set the "default" route to the router
ip netns exec nswan ip route add default via 10.0.0.1

# Enable L3 forwarding on the router
ip netns exec router sysctl -w net.ipv4.ip_forward=1

# Configure NAT on the router (MASQUERADE packets going out via veth-r2a)
ip netns exec router iptables -t nat -A POSTROUTING -o veth-r2a -j MASQUERADE

# Ping from ns1 to nswan (should reach via NAT)
ip netns exec ns1 ping -c 3 10.0.0.2

# IP 10.0.0.1 > 10.0.0.2: ICMP echo request

# View NAT statistics
ip netns exec router iptables -t nat -L -n -v

# Check connection tracking
ip netns exec router conntrack -L | head

# Capture packets on router:
# Internal interface
ip netns exec router tcpdump -i veth-r1a -nn -c 5 icmp
# External interface (after NAT)
ip netns exec router tcpdump -i veth-r2a -nn -c 5 icmp

# Verify addresses and routes
ip netns exec ns1    ip addr; ip netns exec ns1 ip route
ip netns exec router ip addr; ip netns exec router iptables -t nat -S
ip netns exec nswan  ip addr; ip netns exec nswan ip route
```

## Add Firewall Rules

Simulate a firewall using iptables or nftables.

```sh
[ns1] -- (LAN:10.0.0.0/24) -- [router] -- (WAN:10.0.1.0/24) -- [nswan]
```

```sh
ip netns exec router iptables -A FORWARD -s 10.0.1.2 -d 10.0.0.2 -j DROP
```

## VLAN and VXLAN Networking

## Dynamic Routing Protocols

Install routing daemons in your router namespace and run protocols like OSPF or BGP.

Example with FRRouting:

## Final Goal: Simulate Cloud or Kubernetes Networks
With these building blocks, you can recreate complex networks on a single Linux host:
VPC + subnets
Load balancers using HAProxy or Envoy
Pod networks like Kubernetes CNI plugins
Zero-trust security with network policies