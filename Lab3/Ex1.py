from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)  


encoded_text = cipher_suite.encrypt(b"Hello, this is a secret message!")
print(f"encoded_text: {encoded_text}")


# Use the crytography library to encode and decode a message
decoded_text = cipher_suite.decrypt(encoded_text)
print(f"decoded_text: {decoded_text.decode('utf-8')}")