import requests

URL_REG = "https://wrcenmardnbprfpqhrqe.supabase.co/functions/v1/peanut-mining/register"

data = {
    "agent_id": "NAMA_AGENT",
    "public_key": "GANTI_PUBLIK_KEY",
    "compute_capability": "CPU",
    "max_vcus": 1000
}

response = requests.post(URL_REG, json=data)
print(response.json())
