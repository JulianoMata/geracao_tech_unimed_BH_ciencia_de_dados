nome = "Juliano"
idade = 46
profissão = "Analista de Dados"
linguagem = "Python"
saldo = 42.457

dados = {"nome": "Juliano", "idade": 46}


print("Nome : %s Idade: %d" % (nome, idade))

print("Nome : {} Idade:{}".format(nome, idade))

print("Nome : {1} Idade:{0}".format(idade, nome))

print("Nome : {nome} Idade:{idade}".format(nome = nome, idade = idade))

print("Nome: {nome} idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
      