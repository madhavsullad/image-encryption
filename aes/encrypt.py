from Crypto.Cipher import AES

#encrypting
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is yo"
ciphertext = obj.encrypt(message)
print repr (ciphertext)

#deceypting
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
dec = obj2.decrypt(ciphertext)
print dec
