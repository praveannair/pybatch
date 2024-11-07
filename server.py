import socket as s
server = s.socket()
server.bind(('localhost',9999))
server.listen(10)
print('Waiting for connection')
while True:
    conn,addr = server.accept()
    cname = conn.recv(1024).decode()
    print('Connected with ' + cname,addr)
    conn.send(bytes('Welcome to Server'+cname,'utf-8'))
    conn.close
