# Criando uma demonstração de gráfico em linha com o mtaplotlib.py
# Importanto a Bilbioteca
import matplotlib.pyplot as plt

# Onde X define a largura 
# Onde Y define a altura 
x = [1, 3, 5, 7, 9, 11, 13] 
y = [2, 3, 7, 2, 6, 0, 7]   
z = [300, 200, 300, 500, 400, 450, 600]
# Criando uma variavel para alterar o tamanho do circulo aplicada na função s()


# Variaveis
titulo = "Scatterplot: Gráfico de Dispersão"
eixoX = "Eixo X"
eixoY = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# Plotando o gráfico
plt.scatter(x, y, label = "Meus pontos", color = 'k', marker = ".", s = z)
plt.plot(x, y, color = "#A9A9A9", linestyle = "-") # Plotando ao mesmo tempo, um gráfico de linha para ligar os pontos.
plt.legend()   # Exibindo uma legenda label() também neste tipo de grafico disperso.
plt.show()