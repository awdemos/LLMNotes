import requests

url = "http://localhost:42767/api/show"
prompt = "What is the weather like today?"
response = requests.post(url, json={"prompt": prompt})

if response.status_code == 200:
    print(response.json()["text"])
else:
    print(f"Error: {response.text}")

