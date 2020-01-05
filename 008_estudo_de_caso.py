# Estudo de caso sobre o crescimento da população brasileira (1980 - 2016).
# Fonte: DataSUS - http://datasus.saude.gov.br/

# Importanto a biblioteca matplotlib
import matplotlib.pyplot as plt

# Importanto e lendo o aquivo até então, sem biblioteca
dados = open("populacao-brasileira.csv").readlines()

x = [] # Criando um eixo X para os anos
y = [] # Criando um eixo Y para a população

# Criando um for para percorrer os dados usando a função
# range() que cria de 0 ao tamanho final dos dados para i
# gnorar a primeira linha e len() que conta a quantidade 
# bem como usar a função split() para fazer a separação po
# linhas, em dois valores. É importante armazenar em banco
# de dados em INT, para facilitar a manipulação -> int().
for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

# print(x) Testando exibição de X
# print(y) Testando exibição de Y

# Plotando o gráfico e legendas
plt.plot(x, y)
plt.title("Crescimento da população brasileira de 1980 a 2016")
plt.xlabel("Ano")
plt.ylabel("População x 100.000.000")
plt.show()
