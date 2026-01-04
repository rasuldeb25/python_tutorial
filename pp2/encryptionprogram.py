#Pyhton encryption program

import  random
import  string

#Encrypt
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"The encrypted message is: {cipher_text}")
print(f"The original message is: {plain_text}")
#Dycrypt
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"The encrypted message is: {cipher_text}")
print(f"The original message is: {plain_text}")