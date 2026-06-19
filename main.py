import os
import requests
from dotenv import load_dotenv

load_dotenv()

INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN = os.getenv("ZAPI_SECURITY_TOKEN")

url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"

payload = {
    "phone": "5531999999999",
    "message": "Olá João, teste da Z-API!"
}

headers = {
    "Client-Token": CLIENT_TOKEN
}

response = requests.post(url, json=payload ,headers=headers)

print(response)