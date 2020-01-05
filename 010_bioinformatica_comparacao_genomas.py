# Estudo de caso: Comparaçãode Genomas  Humano x Bactéria
# Importar mapeamento de dados dos genomas em download

entrada = open("download/bacteria.fasta").read()
saida = open("bacteria.html","w")

# Criando um dicionário de contagem
contador = {}

# Cria-se um laço for para percorrer os valores e ver a quantidade
# de comparações entre os genomas A - T - C - G presentes no mapa.

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        contador[i+j] = 0

#Fazendo o tratamento de erro de caracteres "/" com uma função:
entrada = entrada.replace("\n","")

for k in range(len(entrada)-1):
    contador[entrada[k] + entrada[k+1]] += 1


# Printando a estrutura HTML

i = 1
for k in contador:
    transparencia = contador[k]/max(contador.values())
    saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparencia)+"')>"+k+" </div>")

    if i%4 == 0:
        saida.write("<div style='clear:both'> </div>")
    i += 1

saida.close()