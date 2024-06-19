# Import the required modules and classes
from EncryptionMLE import EncryptionMLE  # Assuming the code is in a file named EncryptionMLE.py

# Create an instance of the EncryptionMLE class
encryption_instance = EncryptionMLE()

# Example payload to be encrypted (replace this with your actual payload)
payload_to_encrypt = {
    "data": "sensitive data",
    "user_id": 12345
}

# Call the encrypt method to encrypt the payload
encrypted_data = encryption_instance.encrypt(payload_to_encrypt)

# Print or use the encrypted data as needed
print("Encrypted Data:", encrypted_data)
