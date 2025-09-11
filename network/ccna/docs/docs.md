# Docs

```
Ethernet (Layer 2: Data Link)
└─ IP (Layer 3: Network)
   └─ ICMP (Part of IP Layer)
      └─ Data (Payload)
```

### **Why this is correct**

* **Ethernet** is at **Layer 2 (Data Link Layer)** — responsible for MAC addressing and local delivery.
* **IP** is at **Layer 3 (Network Layer)** — responsible for logical addressing and routing.
* **ICMP** is **inside the IP layer** (also Layer 3).
  It is **not a separate layer** like TCP/UDP, but a protocol for control and error messages (e.g., `ping`).
* **Data** is the actual message or payload carried by ICMP.

This shows the encapsulation clearly:

* The **Ethernet frame** wraps the **IP packet**,
* The **IP packet** wraps the **ICMP message**,
* The **ICMP message** contains the **data**.
