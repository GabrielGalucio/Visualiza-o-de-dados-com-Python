### Visualização de Dados com Python

Este repositório demonstra os diferentes tipos de gráficos que são utilizados para a visualização de dados após o devido tratamento dos mesmos. É importante observar que as demonstrações não foram realizadas em caderno de Jupyter Notebook como na maioria dos casos mas sim em um editor, nesse caso o vsCode versão 1.44.

### Proposta

Pode-se afirmar que a utilização de um caderno Jupyter poderia ser a melhor metodologia nesse caso, porém, queremos ver a fundo e diretamente no código como são realizadas a geração dos gráficos. Isso é melhor exemplificado na problematica que o Dr. Diego Mariano propõe no final das demonstrações.

Analisar um estudo de caso voltado para Bioinformática, que consiste na comparação de dois genomas/ sequencias de DNA de um humano e uma bactéria e poder assim, visualizar o que os dois seres vivos tem em comum em relação ao seus genomas. Para isso é utilizado um gráfico de cores em forma de matriz, moldada diretamente por uma estrutura HTML com Python.

### Requisitos

* Conforme citado, os scripts podem ser rodados facilmente em qualquer editor de texto de sua preferência.
* É necessário ter uma versão do Python 3.1 ou maior instalada na sua máquina, caso não tenha você pode acessar esse tutorial xuxu belexa [Tutorial de Instalação Python](https://python.org.br/instalacao-windows/) para Windows, o Python já vem instalado no Linux e MacOS.
* Como os scripts foram criados fora de um ambiente virtual do Jupyter Notebook, foi necessário realizar a instalação da biblioteca Matplotlib manualmente com o **pip**.
* O **pip** é um sistema de gerenciamento de pacotes usado para instalar e gerenciar pacotes de software escritos na linguagem de programação Python, para instalar o pip na sua máquina, basta digitar o comando:

```
sudo apt-get install pip
```
* Após isso você pode rodar o seguinte comando no seu terminal para verificar se o pip foi instalado corretamente:

```
pip --version
```

* Com o pip instalado, você agora terá um gerenciador de pacotes para instalar suas bibliotecas, olha que legal, rode a seguinte linha para instalar o Matplotlib:

```
python -m pip install -U matplotlib
```

Pronto, você agora pode executar e ver essa bagunça toda.