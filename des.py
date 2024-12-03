from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

# Predefined DES key
DES_KEY = '12345678'  # 8 bytes for DES

# DES Encryption/Decryption
def des_encrypt(data):
    cipher = DES.new(DES_KEY.encode('utf-8'), DES.MODE_ECB)
    encrypted = cipher.encrypt(pad(data.encode(), DES.block_size))
    return base64.b64encode(encrypted).decode('utf-8')

def des_decrypt(encrypted_data):
    cipher = DES.new(DES_KEY.encode('utf-8'), DES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(base64.b64decode(encrypted_data)), DES.block_size)
    return decrypted.decode('utf-8')

# Main function for testing DES
def main():
    data = input("Enter the text to encrypt: ")
    
    des_encrypted = des_encrypt(data)
    print(f"DES Encrypted: {des_encrypted}")
    print(f"DES Decrypted: {des_decrypt(des_encrypted)}")

if __name__ == "__main__":
    main()