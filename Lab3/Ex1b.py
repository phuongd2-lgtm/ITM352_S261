from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = input("Enter a message: ")

# encode before encrypt
encrypted = cipher.encrypt(message.encode('utf-8'))
print("Encrypted:", encrypted)

# decrypt and decode
decrypted = cipher.decrypt(encrypted).decode('utf-8')
print("Decrypted:", decrypted)