"""Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Palmeiras.
OBS: Informações baseadas na classificação do dia 06/09/2023"""


brasileiro = ("Botafogo", "Palmeiras", "Gremio", "Flamengo", "Fluminense",
              "Bragantino", "Athletico-PR", "Fortaleza", "Atletico-MG", "Cuiabá",
              "São Paulo", "Cruzeiro", "Corinthians", "Internacional", "Goiás",
              "Bahia", "Santos", "Vasco da Gama", "América-MG", "Coritiba")

print("Os cinco primeiros colocados são:\n{}".format(brasileiro[0:5]))
print("{:=^140}".format(''))
print("Os ultimos 4 colocados são:\n{}".format(brasileiro[-4:]))
print("{:=^140}".format(''))
print("Em ordem alfabetica:\n{}".format(sorted(brasileiro)))
print("{:=^140}".format(''))
print("O Palmeiras esta na {}ª colocação".format(brasileiro.index('Palmeiras') + 1))
print("{:=^140}".format(''))
