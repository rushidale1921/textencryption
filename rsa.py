from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# RSA Encryption/Decryption
def rsa_encrypt(data, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted = cipher.encrypt(data.encode())
    return base64.b64encode(encrypted).decode('utf-8')

def rsa_decrypt(encrypted_data, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_data))
    return decrypted.decode('utf-8')

# Generate RSA keys
def generate_rsa_keys():
    key_pair = RSA.generate(2048)
    return key_pair.export_key(), key_pair.publickey().export_key()

# Main function for testing RSA
def main():
    data = input("Enter the text to encrypt: ")
    private_key, public_key = generate_rsa_keys()
    
    rsa_encrypted = rsa_encrypt(data, public_key)
    print(f"RSA Encrypted: {rsa_encrypted}")
    print(f"RSA Decrypted: {rsa_decrypt(rsa_encrypted, private_key)}")

if __name__ == "__main__":
    main()