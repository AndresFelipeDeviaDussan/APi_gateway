"""
This type of file should not be shared or uploaded to the public (it should only be shared with the members of the group)
{However for educational reasons it will be uploaded}
"""

import requests

security_backend = "http://localhost:8080"
headers = {"Content-Type": "application/json; charset=utf-8"}

# Create roles
roles = [
    {"name": "admin", "description": "administrador del sitema de votos"},
    {"name": "Jurado", "description": "El que autentica los votos"},
    {"name": "ciudadano", "description": "El que vota"}
]
url = f'{security_backend}/rol/insert'
admin = None
for rol in roles:
    response = requests.post(url, headers=headers, json=rol)
    if rol.get('name') == "admin":
        admin = response.json()
    print(response.json())
print("="*30)

"""
The permissions that we are going to define are those that authorize access to the API Gateway
"""
# Basic permission related to admin
