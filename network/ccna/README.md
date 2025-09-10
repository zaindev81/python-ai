# CCNA

## Setup

```sh
uv init
uv venv
source .venv/bin/activate
uv pip install netmiko pyats genie ipaddress requests nornir rich scapy
uv pip install scapy netaddr dnspython pyshark
```

## Install

```sh
uv venv
source .venv/bin/activate
uv sync
```

## Examples

```sh
python examples/osi-tcp-ip.py

python examples/vector.py
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