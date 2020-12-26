# usar o go live no arquivo json teste.json !!

import requests

response = requests.get("http://127.0.0.1:5500/teste.json")
print("Status code:\n", response.status_code)
print("\nArquivo json:\n", response.json())
# print(requests.post("http://127.0.0.1:5500/teste.json", json= {"nome": "Nick", "idade": 18, "id": 3})) tentativa de realizar aa criaçãom de um novo elemento no arquivo json teste.json