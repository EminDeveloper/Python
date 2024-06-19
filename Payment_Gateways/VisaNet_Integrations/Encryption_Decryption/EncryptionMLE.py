import json
import time
from jwcrypto import jwk, jwe
import os

class EncryptionMLE:  

    def __init__(self):
        self.config = self.load_configuration()

    def load_configuration(self):
        # Assuming Configuration() is a class or function that returns the configuration
        # Adjust accordingly based on your actual implementation
        return Configuration()

    def encrypt(self, payload):
        payload = json.dumps(payload)
        protected_header = {
            "alg": "RSA-OAEP-256",
            "enc": "A128GCM",
            "kid": self.config.api_key['keyId'],
            "iat": int(round(time.time() * 1000))
        }
        modified_path = self.config.encryption_public_key_path.replace("\x0b", "\\")
        print("Modified File Path:", modified_path)

        jwetoken = jwe.JWE(payload.encode('utf-8'),
                           recipient = self.load_pem(modified_path),
                           protected=protected_header)
        encrypted_payload = jwetoken.serialize(compact=True)
        # return json.dumps({"encData": encrypted_payload})
        return encrypted_payload
    

    def load_pem(self, file_path):
        with open(file_path, "rb") as pemfile:
            return jwk.JWK.from_pem(pemfile.read())

class Configuration:
    def __init__(self):
        self.api_key = {
            'keyId': '28352508-7a25-4116-b7c8-aeaeb79572de'
        }
        self.encryption_public_key_path = 'D:\\Rabbit\\YIGIM\\Work\\Magnet\\Original_Area\\Java_8\\Adapters\\Visa\\certificate\\v2\\original\\MLE\\pemiko\\mle-client.pem'



