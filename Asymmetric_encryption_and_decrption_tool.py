from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes



#generate RSA keys using standards/default
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()   #saves public key from generated private key

    #saves private key to "private_key.pem" file
    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption() 
        ))
    
    #saves public key to "public_key.pem" file
    with open("public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ))

#loads private key from "private_key.pem" file and deserialize to use
def load_private_key():
    with open("private_key.pem", "rb") as f:
        return serialization.load_pem_private_key(
            f.read(),
            password=None,  #key is not password protected
            backend=default_backend()
        )

#loads public key from "public_key.pem" file and deserialize to use
def load_public_key():
    with open("public_key.pem", "rb") as f:
        return serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )



#encrypts a message using the public key and adds OAEP padding for extra security
def encrypt_message(message):
    public_key = load_public_key()
    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message


#decrypts message by taking in encrypted message as input and using private key and same OAEP padding
def decrypt_message(encrypted_message):
    private_key = load_private_key()
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode()   #returns decrypted message as a string




#run to demonstrate encryption and decryption
if __name__ == "__main__":
    generate_keys()  #generate keys (run this once)
    
    #request user input for a message and print it
    original_message = input("Enter the message to encrypt: ")
    print("Original:", original_message)
    
    #encrypt message and print
    encrypted = encrypt_message(original_message)
    print("Encrypted:", encrypted)
    
    #decrypt message and print
    decrypted = decrypt_message(encrypted)
    print("Decrypted:", decrypted)