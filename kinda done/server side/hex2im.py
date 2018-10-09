import binascii

my_file=open("dec.txt","r")

my_hex_string =  my_file.read()
data = binascii.a2b_hex(my_hex_string)
with open('image1.jpg', 'wb') as image_file:
    image_file.write(data)
