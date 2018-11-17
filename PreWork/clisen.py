import socket

CHUNK_SIZE = 4 * 1024

sock = socket.socket()
sock.connect(('localhost', 12345))
print 'client connected'
chunk = sock.recv(CHUNK_SIZE)
data = chunk
print 'first chunk received'
while chunk:
    chunk = sock.recv(CHUNK_SIZE)
    data +=chunk
    print 'receiving...'
print 'received!!!!!!!!!!!!!!!!'
f = open('new.jpg','wb')
f.write(data)
f.close()
sock.close()
