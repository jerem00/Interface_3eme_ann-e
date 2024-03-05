import requests

# URL de l'endpoint de l'API Flask
url = 'http://localhost:5000/submit'

# Données JSON à envoyer au serveur
data = {'key': 'value'}
# Envoi d'une requête POST
response = requests.post(url, json=data)

# Affichage de la réponse du serveur
print('Status Code:', response.status_code)
print('Response:', response.json())
