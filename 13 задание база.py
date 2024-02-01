from ipaddress import *
net = ip_network('119.68.84.200/255.255.240.0', 0)
adress = f'{net.network_address:b}'
print(adress.count('1'))