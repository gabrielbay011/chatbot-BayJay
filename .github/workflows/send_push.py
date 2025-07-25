import requests

API_URL = "127.0.0.1:8000/update/"

payload = {
    "message": "Código atualizado!"
}

try:
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    print(f"Sucesso: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Erro ao enviar push para API: {e}")
    exit(1)
