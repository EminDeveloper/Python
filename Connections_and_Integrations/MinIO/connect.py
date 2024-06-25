from dotenv import find_dotenv, load_dotenv
import boto3
from botocore.client import Config
import os


load_dotenv()
access_key_id = os.environ.get("MINIO_ACCESS_KEY_ID")
secret_access_key = os.environ.get("MINIO_SECRET_ACCESS_KEY")
endpoint = os.environ.get("MINIO_ENDPOINT_URL")
print(access_key_id)
print(secret_access_key)
print(endpoint)


session = boto3.session.Session()
client = session.client('s3',
                        region_name='ams3',
                        endpoint_url=endpoint,
                        aws_access_key_id=access_key_id,
                        aws_secret_access_key=secret_access_key,
                        config=Config(s3={'addressing_style': 'virtual'}))


client.upload_file('2024_06_21_18_40_56_350837.mp3', 'hr-bot-storage',
               'voices/2024_06_21_18_40_56_350837.mp3')



