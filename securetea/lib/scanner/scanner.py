from re import sub
import nmap
import socket   
import json
from netaddr import IPAddress

class Scanner:
    def __init__(self, cred):
        self.scan = cred["scan"].lower()

    def get_interface_data(self):
        addr_dict = {}
        from netifaces import interfaces, ifaddresses, AF_INET
        for ifaceName in interfaces():
            for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] ):
                addr_dict[ifaceName] = i
        
        return addr_dict
    
    def get_ip_from_IFDATA(self, addrs):
        ip_data = []
        for key in addrs:
            # print(addrs[key]["addr"])
            ip_addr = addrs[key]["addr"]
            if ip_addr !=  "No IP addr" and ip_addr.find("127") != 0:
                # print(ip_addr)
                net_mask = addrs[key]["netmask"]
                # print(net_mask)

                ip_data.append([ip_addr, net_mask])
        
        return ip_data
    
    def get_CIDR(self, netmask):
        return IPAddress(netmask).netmask_bits()
    
    def scan(self, ipaddress, subnet):
        nm = nmap.PortScanner()

        # host_range = ipaddress/cidr
        host_range = ipaddress + "/" + subnet
        print(host_range)

        scan_range = nm.scan(
            hosts=host_range
        )
        return json.dumps(scan_range["scan"], indent=4, sort_keys=True)
    
    def runner(self):
        if self.scan == 'y':
            # scanner_obj = Scanner()
            addrs = self.get_interface_data() 
            ip_data = self.get_ip_from_IFDATA(addrs=addrs)
            print(ip_data)

            for element in ip_data:
                cidr_data = self.get_CIDR(element[1])
                # print(cidr_data)
                element.pop()
                element.append(str(cidr_data))
            
            print(ip_data)
            # ip_data.pop()
            # print(ip_data)

            for element in ip_data:
                scan_res = self.scan(element[0], element[1])
            
            print(scan_res)
            return scan_res
        else:
            return "Scanner Inactive"
    

"""
if __name__ == "__main__":
    scanner_obj = Scanner()
    addrs = scanner_obj.get_interface_data() 
    ip_data = scanner_obj.get_ip_from_IFDATA(addrs=addrs)
    print(ip_data)

    for element in ip_data:
        cidr_data = scanner_obj.get_CIDR(element[1])
        print(cidr_data)
        element.pop()
        element.append(cidr_data)
    
    print(ip_data)
    # ip_data.pop()
    # print(ip_data)

    for element in ip_data:
        scan_res = scanner_obj.scan(str(element[0]), str(element[1]))
    
    print(scan_res)

    # print(json.dumps(addrs, indent=4, sort_keys=True))

"""
