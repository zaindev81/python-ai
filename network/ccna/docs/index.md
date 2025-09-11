# Docs

If you want to **learn CCNA with Python**, you should focus on topics that connect networking fundamentals with Python automation. CCNA is about understanding networking concepts, while Python can help you **automate tasks and simulate networks**. Here’s a roadmap:

---

## **1. Networking Fundamentals (CCNA Core Topics)**

These are essential CCNA topics. You’ll use Python later to practice and automate them.

* **OSI & TCP/IP Models** – layers, protocols, encapsulation.
* **IP Addressing** – IPv4/IPv6, subnetting, CIDR.
* **Routing Basics** – static routes, dynamic routing (OSPF, EIGRP).
* **Switching Basics** – VLANs, trunking, STP.
* **Network Services** – DHCP, DNS, NAT.
* **Security** – ACLs, basic firewall concepts.
* **Wireless Networking** – basic Wi-Fi concepts.
* **Troubleshooting** – Ping, traceroute, show commands.

💡 *Practice tools*: Cisco Packet Tracer or GNS3.

---

## **2. Python for Network Automation**

After understanding networking, you can use Python to automate:

* **Python Basics**: variables, loops, functions, modules.
* **Networking Libraries**:

  * `socket` – low-level network programming.
  * `ipaddress` – manage IP addresses/subnets.
  * `paramiko` – SSH into network devices.
  * `netmiko` – high-level automation for Cisco devices.
  * `napalm` – multi-vendor network automation.
* **REST APIs**:

  * Use `requests` to interact with devices that support APIs (like Cisco DNA Center).

---

## **3. Python + CCNA Integration Topics**

| CCNA Topic         | Python Project Example                               |
| ------------------ | ---------------------------------------------------- |
| Subnetting         | Script to calculate subnets automatically            |
| VLAN Configuration | Automate VLAN setup on switches via Netmiko          |
| OSPF/EIGRP         | Script to verify routing tables via SSH              |
| ACLs               | Generate ACL configs dynamically from CSV            |
| Troubleshooting    | Python script to ping multiple hosts and log results |

---

## **4. Recommended Learning Flow**

1. **Month 1-2** – Focus on CCNA theory + Packet Tracer labs.
2. **Month 3** – Learn Python basics and small scripts.
3. **Month 4** – Combine Python + CCNA, start with Netmiko projects.
4. **Month 5+** – Work on larger automation projects (multi-device).

---

## **5. Tools You Should Use**

* **Packet Tracer** – for CCNA simulation.
* **VS Code or PyCharm** – for Python coding.
* **GitHub** – to save your automation scripts.
* **Cisco DevNet Sandbox** – free Cisco devices for practice.
