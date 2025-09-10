from netmiko import ConnectHandler

r1 = {
    "device_type": "cisco_ios",
    "host": "192.0.2.11",
    "username": "cisco",
    "password": "cisco",
}

cfg = [
    "router ospf 1",
    " network 10.0.0.0 0.0.0.255 area 0",
    " passive-interface default",
    " no passive-interface GigabitEthernet0/0",
]

with ConnectHandler(**r1) as conn:
    print(conn.send_config_set(cfg))
    print(conn.send_command("show ip ospf neighbor"))
