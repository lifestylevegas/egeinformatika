from ipaddress import *
net = ip_network('123.87.81.24/255.255.252.0', 0)
num = net.num_addresses
print(num-2)