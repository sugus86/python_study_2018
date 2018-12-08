import socket, time, select

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('127.0.0.1', 6633))
soc.listen(1)

while True:
    try:
        sel_in, sel_out, sel_err = select.select([soc],[],[soc],1)
    except:
        print "select has problem"

    for s in sel_err:
        print "socket error"
        break

    for s in sel_in:
        print "socket is active... , ", soc
        sock, addr = soc.accept()
        sock.send('1')
        
    
    time.sleep(1)
    print " 1 second has wait"
    
