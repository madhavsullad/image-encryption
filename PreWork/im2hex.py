import binascii
filename = 'image.jpg'
with open(filename, 'rb') as f:
    content = f.read()
f = open("image.txt","w")
f.write(binascii.hexlify(content).decode())
f.close()
#print(binascii.hexlify(content))
