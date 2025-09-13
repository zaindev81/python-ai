# Network Namespace

This guide demonstrates how to create and configure Linux network namespaces, virtual Ethernet (veth) pairs, and bridges.

## Setup Environment

```sh
# Start a privileged Ubuntu container and install networking tools
docker run -it --privileged --rm \
  -v ./:/mnt/host \
  ubuntu:22.04 bash

ls -la /mnt/host

# install
apt update && apt install -y iproute2 iputils-ping bridge-utils
```

## Build a Custom Lab Image

```sh
# build your custom image
docker build -t ubuntu-netlab:latest .

# run your custom container
docker run -it --rm \
  --privileged \
  -v "$(pwd)":/app \
  ubuntu-netlab bash
```

## Inspect Network Interfaces

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

## Create a veth pair (like a cable with two plugs):

```sh
ip link add <interface-name-1> type veth peer name <interface-name-2>
ip link add veth-ns1 type veth peer name veth-ns2

ip link show

[ns1] veth-ns1 <---- Virtual Cable ----> veth-ns2 [ns2]
```

## Debugging Commands

```sh
# Show IP addresses in each namespace
ip -n ns1 addr
ip -n ns2 addr

# List all network interfaces in a namespace
ip -n ns1 link

# Check ARP table (neighbor cache)
ip -n ns1 neigh

ip netns exec ns1 ping -I veth-ns1 10.0.0.2
ip netns exec ns2 ping -I veth-ns2 10.0.0.1
```

## Cleanup

```sh
ip netns del ns1
ip netns del ns2
```