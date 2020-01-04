# Criando uma demonstração de gráfico em linha com o mtaplotlib.py
# Importanto a Bilbioteca
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7] # Definindo a largura (qtd de barras)
y = [2, 3, 7, 2, 6, 0, 7] # Definindo a altura  (valores da barras)

# Variaveis
titulo = "Gráfico de barras"
eixoX = "Eixo X"
eixoY = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# Chamando a função de plotagem bar() dos eixos x e y
plt.bar(x, y)
plt.show()