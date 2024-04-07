import random
import string


chars = " " + string.punctuation + string.ascii_letters + string.digits

#turn the string into a list
chars = list(chars)
key = chars.copy()
random.shuffle(key)


#encrypt the message
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter) #find the index of the letter in the chars list
    cipher_text += key[index] #get the corresponding character from the key

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")


#decrypt the message
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""


for letter in cipher_text:
    index = key.index(letter) #find the index of the letter in the chars list
    plain_text += chars[index] #get the corresponding character from the key


print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")