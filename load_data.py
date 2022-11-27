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
modules = ['table', 'candidate', 'political_parties', 'result', 'user', 'rol']
endpoints = [('s', 'GET'), ('/?', 'GET'), ('/insert', 'POST'), ('/update/?', 'PUT'), ('/delete/?', 'DELETE')]
url = f'{security_backend}/permission/insert'
for module in modules:
    for endpoint, method in endpoints:
        permission_url = f'/{module}{endpoint}'
        body = {
            "url": permission_url,
            "method": method
        }
        response = requests.post(url, headers=headers, json=body)
        print(response.json())
        permission = response.json()
        url_relation = f'{security_backend}/rol/update/{admin.get("idRol")}/add_permission/{permission.get("id")}'
        response = requests.put(url_relation, headers=headers)
