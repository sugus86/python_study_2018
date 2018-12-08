import socket, time, select

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


soc.connect(('127.0.0.1', 6633))

while True:
    a=soc.recv(1024)
    if a:
        print repr(a)
        soc.close()
        break
    
