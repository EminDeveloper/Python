import json
import time
from jwcrypto import jwk, jwe

class DecryptionMLE:  

    def __init__(self):
        self.config = self.load_configuration()

    def load_configuration(self):
        # Assuming Configuration() is a class or function that returns the configuration
        # Adjust accordingly based on your actual implementation
        return Configuration()

    def decrypt(self, encPayload):
        modified_path = self.config.decryption_private_key_path.replace("\x0b", "\\")
        print("Modified File Path:", modified_path)
        if type(encPayload) is str:
            payload = json.loads(encPayload)
        if payload.get('encData', False):
            config = Configuration()
            jwetoken = jwe.JWE()
            jwetoken.deserialize(payload["encData"], key=self.loadPem(modified_path))
            return json.dumps(json.loads(jwetoken.payload))
        return encPayload

    def loadPem(self, filePath):
        with open(filePath, "rb") as pemfile:
            return jwk.JWK.from_pem(pemfile.read())


class Configuration:
    def __init__(self):
        self.api_key = {
            'keyId': '28352508-7a25-4116-b7c8-aeaeb79572de'
        }

        self.decryption_private_key_path = 'D:\\Rabbit\\YIGIM\\Work\\Magnet\\Original_Area\\Java_8\\Adapters\\Visa\\certificate\\v2\\original\\MLE\\pemiko\\mle-server.pem'
        # Add other configuration parameters as needed

