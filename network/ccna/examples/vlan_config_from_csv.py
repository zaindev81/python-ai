import csv, sys
from netmiko import ConnectHandler


"""
Automate VLAN config from CSV (Switching)

The script:
  Reads VLAN data (ID and name) from a CSV file.
  Connects to a Cisco device over SSH using Netmiko.
  Automatically creates VLANs and sets their names.
  Verifies the configuration by running show vlan brief.


CSV format example (vlan_list.csv):
vlan_id,name
10,USERS
20,SERVERS
30,VOICE
"""


def load_vlans(csv_path: str):
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        return [{'id': r['vlan_id'].strip(), 'name': r['name'].strip()} for r in reader]


def build_commands(vlans):
    cmds = []
    for v in vlans:
        cmds += [f"vlan {v['id']}", f"name {v['name']}"]
    return cmds


if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python vlan_config_from_csv.py <host> <username> <password> <csv_path> <device_type=cisco_ios>")
        sys.exit(1)

    host, user, pwd, csvp, dev = sys.argv[1:6]
    vlans = load_vlans(csvp)
    print(f"Loaded {len(vlans)} VLANs from csv file:{csvp}: {vlans}")

    cmds = build_commands(vlans)
    device = {"device_type": dev, "host": host, "username": user, "password": pwd}

    with ConnectHandler(**device) as conn:
        conn.enable()
        output = conn.send_config_set(cmds)
        print(output)
        print("Done. Verifying VLANs...")
        print(conn.send_command("show vlan brief"))