# Criando uma demonstração de gráfico em linha com o mtaplotlib.py
# Importanto a Bilbioteca
import matplotlib.pyplot as plt

# Onde X define a largura (qtd de barras)
# Onde Y define a altura (valor das barras)
x1 = [1, 3, 5, 7, 9, 11, 13] # Impar (para comparar)
y1 = [2, 3, 7, 2, 6, 0, 7]  
 
x2 = [2, 4, 6, 8, 10, 12, 14] # Par (para comparar)
y2 = [5, 1, 3, 7, 6, 9, 10]

# Variaveis
titulo = "Gráfico de barras II"
eixoX = "Eixo X"
eixoY = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# Chamando a função de plotagem bar() dos eixos x e y
plt.bar(x1, y1, label = "Grupo 01")
plt.bar(x2, y2, label = "Grupo 02")
plt.legend()
plt.show()

