# CCNA

## Setup

```sh
source .venv/bin/activate
uv add netmiko pyats genie ipaddress requests nornir rich scapy netaddr dnspython pyshark
uv sync
```

## Examples

```sh
sudo python examples/00_osi_tcp_ip.py


sudo python examples/ping_sweep.py

python examples/vlan_config_from_csv.py 192.168.1.1 admin password vlan_list.csv cisco_ios
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