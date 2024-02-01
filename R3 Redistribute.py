from netmiko import ConnectHandler

r21 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.10.41',
    'username': 'Ali',
    'password': 'Hojaji',
}
net_connect = ConnectHandler(**r21)
config_commands = ['router ospf 110', 'network 10.10.10.40 0.0.0.3 area 0', 'redistribute eigrp 90']
output = net_connect.send_config_set(config_commands)
config_commands = ['router EIGRP 90', 'no auto-summary', 'network 11.11.11.40 0.0.0.3', 'redistribute ospf 1 metric 1 1 1 1 1']
output = net_connect.send_config_set(config_commands)
print(output)