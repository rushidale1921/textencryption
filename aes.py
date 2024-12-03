from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Predefined AES key
AES_KEY = '1234567890123456'  # 16 bytes for AES

# AES Encryption/Decryption
def aes_encrypt(data):
    cipher = AES.new(AES_KEY.encode('utf-8'), AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(encrypted).decode('utf-8')

def aes_decrypt(encrypted_data):
    cipher = AES.new(AES_KEY.encode('utf-8'), AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(base64.b64decode(encrypted_data)), AES.block_size)
    return decrypted.decode('utf-8')

# Main function for testing AES
def main():
    data = input("Enter the text to encrypt: ")
    
    aes_encrypted = aes_encrypt(data)
    print(f"AES Encrypted: {aes_encrypted}")
    print(f"AES Decrypted: {aes_decrypt(aes_encrypted)}")

if __name__ == "__main__":
    main()