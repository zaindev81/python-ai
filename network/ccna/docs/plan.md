# **CCNA + Python 12-Week Plan**

## **Phase 1: Networking Foundations (Weeks 1–4)**

> Goal: Master CCNA core concepts with Packet Tracer.

### **Week 1 – Networking Basics**

* **CCNA Topics**

  * OSI & TCP/IP models
  * Ethernet, cabling, basic hardware
  * Network devices: routers, switches, firewalls
  * CLI basics (Cisco IOS commands)
* **Hands-on**

  * Install **Cisco Packet Tracer**
  * Practice basic commands: `show ip interface brief`, `ping`, `traceroute`
* **Python**

  * Install Python 3.12+
  * Learn basics: variables, data types, `if` statements, loops.
* **Project**

  * Simple Python script: print device info from variables.

---

### **Week 2 – IP Addressing & Subnetting**

* **CCNA Topics**

  * IPv4 and IPv6 basics
  * Subnetting, CIDR notation
  * Static IP configuration
* **Hands-on**

  * Create a small network in Packet Tracer with 3 routers + 2 PCs.
  * Configure IPv4 addresses manually.
* **Python**

  * Learn functions and modules.
  * Use the `ipaddress` module to calculate subnets.
* **Mini Project**

  * Build a **Subnet Calculator** in Python.

---

### **Week 3 – Switching & VLANs**

* **CCNA Topics**

  * Switching concepts
  * VLANs, trunk ports, STP basics
* **Hands-on**

  * Configure VLANs on a switch in Packet Tracer.
  * Practice `show vlan brief`, `show spanning-tree`.
* **Python**

  * Learn file handling and CSV.
  * Intro to `Netmiko` library.
* **Mini Project**

  * Python script to generate VLAN configuration commands from a CSV file.

---

### **Week 4 – Routing Basics**

* **CCNA Topics**

  * Static routing
  * Dynamic routing: OSPF, EIGRP basics
* **Hands-on**

  * Configure static routes and OSPF on Packet Tracer routers.
* **Python**

  * Use `Netmiko` to SSH into routers.
* **Mini Project**

  * Automate **routing table verification**:

    * Python logs into routers and runs `show ip route`.

---

## **Phase 2: Network Automation Basics (Weeks 5–8)**

> Goal: Combine Python automation with CCNA labs.

### **Week 5 – ACLs & Security**

* **CCNA Topics**

  * Access Control Lists (ACLs)
  * Firewall basics
* **Hands-on**

  * Configure basic ACLs on Packet Tracer.
* **Python**

  * Generate ACL commands automatically using Python.
* **Mini Project**

  * Script reads CSV of IP addresses → outputs ACL config lines.

---

### **Week 6 – Network Services**

* **CCNA Topics**

  * DHCP, DNS, NAT
  * Wireless networking basics
* **Hands-on**

  * Configure DHCP on a router in Packet Tracer.
* **Python**

  * Use Python to ping multiple hosts and check connectivity.
* **Mini Project**

  * **Network Scanner**: script pings a list of IPs and logs results to a file.

---

### **Week 7 – REST APIs & Cisco DevNet**

* **CCNA Topics**

  * Review all topics from weeks 1–6.
  * Focus on network automation fundamentals.
* **Python**

  * Learn `requests` library for APIs.
  * Intro to **Cisco DevNet Sandbox** for free labs.
* **Mini Project**

  * Use Cisco DNA Center API to pull device inventory.

---

### **Week 8 – Troubleshooting**

* **CCNA Topics**

  * Troubleshooting methodology
  * Common `show` commands
* **Hands-on**

  * Simulate broken networks in Packet Tracer and fix them.
* **Python**

  * Build Python script to check device status automatically.
* **Mini Project**

  * **Automated Troubleshooting Bot**:

    * Python logs into devices and collects health data.

---

## **Phase 3: Advanced Automation + Exam Prep (Weeks 9–12)**

> Goal: Build full automation project and prepare for CCNA exam.

### **Week 9 – Network Automation Project**

* Combine everything you’ve learned into **one big project**:

  * Automate VLAN creation.
  * Verify routing.
  * Generate reports.
  * Save logs in JSON/CSV format.

---

### **Week 10 – Advanced Topics**

* SNMP, syslog basics.
* WAN technologies (VPN, MPLS overview).
* Python logging and exception handling.

---

### **Week 11 – CCNA Exam Prep**

* Take **practice exams**.
* Focus on weak areas:

  * Subnetting speed.
  * OSPF configuration.
  * ACLs.

---

### **Week 12 – Final Review & Deployment**

* Build a **final GitHub portfolio**:

  * Subnet calculator.
  * VLAN automation.
  * Troubleshooting bot.
* Take a full-length **CCNA practice test**.
* Schedule your real exam date.

---

## **Daily Study Routine (2–3 hours/day)**

| Time   | Activity                             |
| ------ | ------------------------------------ |
| 30 min | Review previous notes                |
| 1 hr   | CCNA theory + Packet Tracer practice |
| 30 min | Python coding                        |
| 30 min | Automation project or review         |

---

## **Resources**

* **CCNA**

  * *Cisco Press CCNA 200-301 Official Cert Guide*
  * Packet Tracer (free from Cisco Networking Academy)
* **Python**

  * *Automate the Boring Stuff with Python*
  * Netmiko Docs: [https://github.com/ktbyers/netmiko](https://github.com/ktbyers/netmiko)
* **Practice Exams**

  * Boson ExSim
  * Pearson CCNA practice tests
