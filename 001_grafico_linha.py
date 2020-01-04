# Criando uma demonstração de gráfico em linha com o mtaplotlib.py

# Importanto a Bilbioteca
import matplotlib.pyplot as plt

x = [1, 2, 5] # Definindo a largura
y = [2, 3, 7] # Definindo a altura

# Inserindo um título no gráfico
plt.title("Gráfico com Matplotlib")

# Inserindo um título no eixo X e Y
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Chamando a função de plotagem plot() dos eixos x e y
plt.plot(x, y)
plt.show()
