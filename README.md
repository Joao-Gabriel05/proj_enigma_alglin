# aps-2-lipe_caio

# Integrantes
Luis Barretto (Socrates_Morreu) e Caio Liberal (Caiolib)

# Instruções de como usar o demo
- Para rodar o demo é necessário ter o python instalado na maquina, caso não tenha, baixe o python em https://www.python.org/downloads/
- Installe o arquivo zip no GitHub
- Baixe o requirements.txt com o pip, apos isso só executar o arquivo app.py (pip install -r requirements.txt)
- Acesse a pasta do demo com o comando "cd" no terminal
- Use o comando "python demo.py" ou "python3 demo.py"
- Siga as instruções dos comandos e escolha a opição desejada para testar as funções
- As funçoes de decodificação irão usar a mensagem codificada anteriormente direto, portanto, se caso já foi codificado a mensagem "oi" pela função enigma, retornando "xa", por exemplo, a função de_enigma já vai decodificar o "xa", sem ser necessário que o usuário mande esse input.

# Instruções de como usar os testes rapidos
- Para rodar os testes rápidos é necessário ter o python instalado na maquina, caso não tenha, baixe o python em https://www.python.org/downloads/
- Installe o arquivo zip no GitHub
- Baixe o requirements.txt com o pip, apos isso só executar o arquivo app.py (pip install -r requirements.txt)
- Acesse a pasta dos testes rápidos com o comando "cd" no terminal
- Use o comando "python testes_rapidos.py" ou "python3 testes_rapidos.py"
- Todos os testes serão printados automaticamente, é necessario acessar o arquivo "testes_rapidos.py" e alterar a string "mensagem" para alterar a mensagem que vai ser codificada ou decodificada por todas as funções

# Biblioteca do programa
- Instale a biblioteca do programa usando o comando "pip install enigma-lipe-caio" ou "pip install enigma-lipe-caio==0.2"
- Para usar as funcoes da biblioteca, coloque no seu arquivo "from enigma_lipe_caio import funcoes_criadas" e "from enigma_lipe_caio import funcoes_adicionais"
- Dessa forma, é possivel utilizar as funções principais desenvolvidas ("funcoes_criadas.para_one_hot()","funcoes_criadas.para_string()","funcoes_criadas.cifrar()","funcoes_criadas.de_cifrar()","funcoes_criadas.enigma()","de_enigma()") e as funções adicionais desenolvidas("funcoes_adicionais.matriz_identidade_alfabeto()","funcoes_adicionais.permutacao_identidade()","teste_mensagem()")

# Discuções das funções implementadas 

- Função "para_one_hot": Essa função recebe uma mensagem(string) e retorna uma matriz que representa essa string. Para tanto começamos criando a função "matriz_identidade_alfabeto" que converte todos os caracteres do alfabeto (e o espaço) para uma matriz. Dessa forma, cada caracter é representando por uma linha dentro de uma matriz identidade, fazendo com que cada um caracter possa ser identificado por uma linha dentro dessa matriz. Assim, pegamos o index de cada palavra da mensagem mandada pelo usuário da nossa string inicial com todos os caracteres. Dessa maneira, podemos associar esses indexes com os da matriz identidade criada, adicionando cada linha da matriz (que representa cada caracter da mensagem) em uma nova matriz. Portanto, criamos uma matriz resultante que apresenta cada caracter em ordem convertido em matriz. Devolvemos a transposição dessa matriz.*

- Função "para_string": Essa função recebe a matriz criada dentro da função "para_one_hot" e converte ela de volta para string. Para tanto, comparamos a matriz identidade, de todos os caracteres (criada na função "matriz_identidade_alfabeto"), com a transposição da matriz retorndada na função "para_one_hot". Dessa forma, pegamos os indexes de cada linha dessa matriz recebida e salvamo-as em uma lista. Para tanto, pegamos esses indexes e, em ordem, pegamos cada index da lista com todos os caracteres (também criada na função "matriz_identidade_alfabeto") e criamos uma string que foi representada pela matriz recebida pelo usuário. Por fim, retornamos essa string.

- Função "cifrar": Essa funçao recebe uma mensagem(string) e uma matriz P(matriz permutação) e codifica essa mensagem retornando uma string de mesmo tamanho do que a mandada mas, com diferentes caracteres. Essa matriz P é criada a partir da função adicional "permutacao_identidade", que cria uma matriz de mesmas dimenções da matriz identidade que contem todos os caracteres que podem ser usados (criada na função "matriz_identidade_alfabeto") mas, com as linhas embaralhadas. Cada vez que essa função é chamada, uma matriz permutada diferente é criada. Assim, pegamos a mensagem que o usuário quer codificar e transformamos tal em uma matriz usando a função "para_one_hot". Dessa forma, multiplicamos a matriz da mensagem mandada pelo usuario pela matriz P. Assim, criamos uma nova matriz codificada e usando a função "para_string" retornamos uma string codificada, criada a partir da matriz codificada da mensagem mandada pelo usuário.

- Função "de_cifrar": Essa funçao recebe uma mensagem(string) codificada e uma matriz P(matriz permutação) e decodifica essa mensagem, retornando a mensagem original mandada para a função "cifrar". Para tanto, multiplicamos o inverso da matriz P com a matriz da mensagem codificada (geradada a partir da função "cifrar") para resultar novamente na matriz da mensagem nao codificada. Podemos fazer essa conta uma vez que podemos assumir de C = A @ B, que B = inverso(A) @ C, da mesma forma, como matriz_da_mensagem_codificada = matriz_permutacao_P @ matriz_mensagem, podemos concluir que a matriz_mensagem = inverso(matriz_permutacao_P) @ matriz_da_mensagem_codificada. Portanto, usamos a função "para_string" para converter a matriz da mensagem original para a mensagem original, retornando essa string.

- Função "enigma": Essa função recebe uma mensagem(string), uma matriz P(matriz permutação) e uma matriz E(matriz permutação) e retornamos a string original codificada. A matriz E, embora diferente da matriz P, também é gerada da mesma forma pela função "permutacao_identidade". Pegamos a mensagem que o usuário quer codificar e transformamos tal em uma matriz usando a função "para_one_hot" e multiplicamos cada matriz do caracter por permutações diferentes. Começamos multiplicando o primeiro carcter apenas pela matriz permutação P, os seguintes caracteres pela mesma matriz P e pela matriz E, sendo que a cada proximo caracter, começando do segundo, adicionamos mais uma matriz E na multiplicação do caracter. Assim, temos que a matriz do primeiro caracter codificada é criada como:
 a[0] = P @ matriz_caracter, a do segundo a[1] = E @ P @ matriz_caracter, a[n] =(E ** (n-1)) @ P @ matriz_caracter (...). 
 Dessa forma criamos uma matriz nova que em ordem junta as matrizes de todos os caracters após suas devidas multiplicações. Por fim usamos a função "para_string" para converter a matriz da mensagem codificada para a mensagem codificada, retorando essa string.

- Função "de_enigma": Essa função recebe uma mensagem(string) codificada, uma matriz P(matriz permutação) e uma matriz E(matriz permutação) e retornamos a string original decodificada. Primeiramenta, convertemos a mensagem codificada para sua matriz codificada usando a função "para_one_hot". Usando a mesma logica anteriormente desenvolvida na função "de_cifrar" e a logica de multiplicação de cada caracter por uma matriz de permutação, desenvolvida na função "engima", podemos concluir que cada matriz de caracter codificado pode ser decodificado a partir da logica, sendo m a matriz da mensagem decodificada e a matriz da mensagem codificada:
m[0] = inverso[P] @ a[0]; m[1] = inverso[E] @ inverso[P] @ a[1]; 
m[n] = inverso([E] ** (n-1)) @ (inverso[E] @ a[n]);(...)
Dessa forma, podemos montar em uma outra matriz todos as matrizes dos caractres decodificados. Por fim, apenas usamos a trasnposição dessa matriz na função "para_string" para retornar a mensagem original decodificada.