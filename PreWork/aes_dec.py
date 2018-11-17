from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter


print "To decrypt:"

# Decryption steps
# Pad for short keys
pad = '# constant pad for short keys ##'
IV = 95914734


# Ask user for key: it must be same to that used for encryption
prompt = 'Input your key. It will padded or truncated at 32 bytes (256 bits).\n-: '
user_keyd = raw_input(prompt)
keyd = (user_keyd + pad)[:32]

# Create counter for decryptor: it is same to the encryptor, but restarts from the beginning

ctr_d = Counter.new(64, prefix=IV)

# Create decryptor, then decrypt and print decoded text
decryptor = AES.new(keyd, AES.MODE_CTR, counter=ctr_d)
decoded_text = decryptor.decrypt(ciphertext)
#print decoded_text

print 'Message decoded and stored in dec.txt'

filed = open("dec.txt","w")
filed.write(decoded_text)

filed.close()
