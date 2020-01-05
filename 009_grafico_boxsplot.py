# Criando um gráfico estilo boxplot 

# Importando a biblioteca de grafica e de geração de valores aleatorios
import matplotlib.pyplot as plt
import random as ran

# vetor = [1, 2, 4, 6, 8, 10, 12, 14, 10, 20]
# vetor vazio
vetor = []

for i in range(10):
    numero_aleatorio = ran.randint(0,10000)
    vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title("Gráfico Boxplot")
plt.show()


