# CCNA

## Setup

```sh
source .venv/bin/activate
uv add netmiko pyats genie ipaddress requests nornir rich scapy netaddr dnspython pyshark
uv sync
```

## Examples

```sh
python examples/osi-tcp-ip.py
```

- https://github.com/secdev/scapy

## MacOS

```sh
docker pull opennetworking/mininet
docker run -it --privileged --name mininet-lab opennetworking/mininet /bin/bash
mn --version
ovs-vsctl show
apt-get update
apt-get install -y openvswitch-switch
mn --topo single,3 --controller=none
```