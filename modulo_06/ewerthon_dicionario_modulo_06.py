import json

clients = {
    "client1": {"name": "Ana", "age": "25"},
    "client2": {"name": "Ewerthon", "age": "22"}
}

with open ('clients.json', "w", encoding="utf-8") as arquivo:
    json.dump(clients, arquivo, indent=4, ensure_ascii=False)

with open("clients.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
print(dados)