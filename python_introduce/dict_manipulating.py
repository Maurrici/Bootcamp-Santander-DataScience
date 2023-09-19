dicionario = {"nome": "Maurício", "idade": 22}
dicionario2 = dict(nome="Maurício", idade=22)
dicionario["endereco"] = dict(rua="Rua Pedestre D", num="191")

print(dicionario)
print(dicionario2)
print("\n")

# Acesso
print(dicionario["nome"])
print(dicionario["endereco"]["num"])
print(dicionario.get("teste"))
print("\n")

# Alterando dados
dicionario["nome"] = "Maurício de Moura dos Santos"
print(dicionario["nome"])
print("\n")

# Percorrendo dados
print(dicionario.items())
print(dicionario.keys())
print(dicionario.values())
print("\n")

for key in dicionario:
    print(f"{key}: {dicionario[key]}")
print("\n")

for key, value in dicionario.items():
    print(f"{key}: {value}")
print("\n")

# Removendo
removido = dicionario.pop("idade", None)
print(removido)
print("\n")

# Criação baseada em list
keys = ["nome", "idade", "endereco"]
dicionario = dict.fromkeys(keys)
print(dicionario)
