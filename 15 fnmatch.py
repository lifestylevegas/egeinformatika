from ipaddress import *
from fnmatch import *
ip = ip_address('99.8.254.232')
for mask in range(33):
    network = ip_network(f'{ip}/{mask}', 0)
    if fnmatch(str(network.netmask),'255.255.*.0'):
        if ip not in [network.network_address, network.broadcast_address]:
            if all(f'{ip:b}'[:16].count('1')<=f'{ip:b}'[16:].count('1') for ip in network):
                print(network.netmask)