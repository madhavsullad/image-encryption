#Image to hex

import binascii
filename = 'eminem1.jpg'
with open(filename, 'rb') as f:
    content = f.read()
f = open("image.txt","w")
f.write(binascii.hexlify(content).decode())
f.close()

#Hex to image

my_file=open("image.txt","r")

my_hex_string =  my_file.read()
data = binascii.a2b_hex(my_hex_string)
with open('image.jpg', 'wb') as image_file:
    image_file.write(data)
