import socket

CHUNK_SIZE = 4 * 1024

server_socket = socket.socket()
server_socket.bind(('192.168.1.102', 12345))
server_socket.listen(5)
print 'server init. and listening'
while True:
    client_socket, addr = server_socket.accept()
    with open('enc.txt', 'rb') as f:
        data = f.read(CHUNK_SIZE)
        while data:
            client_socket.send(data)
            data = f.read(CHUNK_SIZE)
            print 'sending...'
        print 'sent!!!!!!!!!'
    client_socket.close()
    break
f.close()
print 'done!'
