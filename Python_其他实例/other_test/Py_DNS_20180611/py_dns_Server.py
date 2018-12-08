''''' 
Created on 2012-10-15 
 
@author: RobinTang 
'''  
06.  
07.import socketserver  
08.import struct  
09.  
10.# DNS Query  
11.class SinDNSQuery:  
12.    def __init__(self, data):  
13.        i = 1  
14.        self.name = ''  
15.        while True:  
16.            d = data[i]  
17.            if d == 0:  
18.                break;  
19.            if d < 32:  
20.                self.name = self.name + '.'  
21.            else:  
22.                self.name = self.name + chr(d)  
23.            i = i + 1  
24.        self.querybytes = data[0:i + 1]  
25.        (self.type, self.classify) = struct.unpack('>HH', data[i + 1:i + 5])  
26.        self.len = i + 5  
27.    def getbytes(self):  
28.        return self.querybytes + struct.pack('>HH', self.type, self.classify)  
29.  
30.# DNS Answer RRS  
31.# this class is also can be use as Authority RRS or Additional RRS   
32.class SinDNSAnswer:  
33.    def __init__(self, ip):  
34.        self.name = 49164  
35.        self.type = 1  
36.        self.classify = 1  
37.        self.timetolive = 190  
38.        self.datalength = 4  
39.        self.ip = ip  
40.    def getbytes(self):  
41.        res = struct.pack('>HHHLH', self.name, self.type, self.classify, self.timetolive, self.datalength)  
42.        s = self.ip.split('.')  
43.        res = res + struct.pack('BBBB', int(s[0]), int(s[1]), int(s[2]), int(s[3]))  
44.        return res  
45.  
46.# DNS frame  
47.# must initialized by a DNS query frame  
48.class SinDNSFrame:  
49.    def __init__(self, data):  
50.        (self.id, self.flags, self.quests, self.answers, self.author, self.addition) = struct.unpack('>HHHHHH', data[0:12])  
51.        self.query = SinDNSQuery(data[12:])  
52.    def getname(self):  
53.        return self.query.name  
54.    def setip(self, ip):  
55.        self.answer = SinDNSAnswer(ip)  
56.        self.answers = 1  
57.        self.flags = 33152  
58.    def getbytes(self):  
59.        res = struct.pack('>HHHHHH', self.id, self.flags, self.quests, self.answers, self.author, self.addition)  
60.        res = res + self.query.getbytes()  
61.        if self.answers != 0:  
62.            res = res + self.answer.getbytes()  
63.        return res  
64.# A UDPHandler to handle DNS query  
65.class SinDNSUDPHandler(socketserver.BaseRequestHandler):  
66.    def handle(self):  
67.        data = self.request[0].strip()  
68.        dns = SinDNSFrame(data)  
69.        socket = self.request[1]  
70.        namemap = SinDNSServer.namemap  
71.        if(dns.query.type==1):  
72.            # If this is query a A record, then response it  
73.              
74.            name = dns.getname();  
75.            if namemap.__contains__(name):  
76.                # If have record, response it  
77.                dns.setip(namemap[name])  
78.                socket.sendto(dns.getbytes(), self.client_address)  
79.            elif namemap.__contains__('*'):  
80.                # Response default address  
81.                dns.setip(namemap['*'])  
82.                socket.sendto(dns.getbytes(), self.client_address)  
83.            else:  
84.                # ignore it  
85.                socket.sendto(data, self.client_address)  
86.        else:  
87.            # If this is not query a A record, ignore it  
88.            socket.sendto(data, self.client_address)  
89.  
90.# DNS Server  
91.# It only support A record query  
92.# user it, U can create a simple DNS server  
93.class SinDNSServer:  
94.    def __init__(self, port=53):  
95.        SinDNSServer.namemap = {}  
96.        self.port = port  
97.    def addname(self, name, ip):  
98.        SinDNSServer.namemap[name] = ip  
99.    def start(self):  
100.        HOST, PORT = "0.0.0.0", self.port  
101.        server = socketserver.UDPServer((HOST, PORT), SinDNSUDPHandler)  
102.        server.serve_forever()  
103.  
104.# Now, test it  
105.if __name__ == "__main__":  
106.    sev = SinDNSServer()  
107.    sev.addname('www.aa.com', '192.168.0.1')    # add a A record  
108.    sev.addname('www.bb.com', '192.168.0.2')    # add a A record  
109.    sev.addname('*', '0.0.0.0') # default address  
110.    sev.start() # start DNS server  
111.  
112.# Now, U can use "nslookup" command to test it  
113.# Such as "nslookup www.aa.com"  
