import requests
import os

# funçao para enviafr mensagem dinamica via Z-API 
def sendMensage(
    telefone: str,
    mensagem: str
):  
    url_zapi = os.getenv("ZAPI_URL") 
    if not url_zapi:
        raise ValueError("A variável de ambiente ZAPI_URL não está definida.")
    
    requests.post(
        url_zapi,
        json={
            "phone": telefone,
            "message": mensagem
        }
    )