import pyaes

# A 256 bit (32 byte) key
key = "This_key_for_demo_purposes_only!"

# For some modes of operation we need a random initialization vector
# of 16 bytes
iv = "InitializationVe"

print "AES algorithm"
ciphertext = raw_input("Enter the cypher text:")

# The counter mode of operation maintains state, so decryption requires
# a new instance be created
aes = pyaes.AESModeOfOperationCTR(key)
decrypted = aes.decrypt(ciphertext)

# True
print decrypted
