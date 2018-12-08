def pretty_ipv4(v):
    return "%d.%d.%d.%d" % ((v >> 24) & 0xFF, (v >> 16) & 0xFF, (v >> 8) & 0xFF, v & 0xFF)

def ip2int(ip):
    ip_list = [int(i) for i in ip.split(".")]
    print(ip_list)
    return ip_list[0]*256*256*256+ip_list[1]*256*256+ip_list[2]*256+ip_list[3]

print (pretty_ipv4(16843009))
print(ip2int("1.2.3.4"))
print(pretty_ipv4(16909060))
