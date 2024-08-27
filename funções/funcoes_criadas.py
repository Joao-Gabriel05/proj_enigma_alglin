import numpy as np
from funções.funcoes_adicionais import *

def para_one_hot(mensagem=str):

    #verificando se todos os carcteres da mensagem estao no alfabeto que esta sendo utilizado
    if teste_mensagem(mensagem):

        #transformando a mensagem para poder traduzi-la
        mensagem = mensagem.lower()

        #pegando a matriz identidade do alfabeto
        matriz_identidade_todos_char, todos_carcteres = matriz_identidade_alfabeto()

        #lista com os indexes de cada caracter dentro do alfabeto
        lista_index_caracteres_mensagem = []
        for caracter_mensagem in mensagem:
            for caracter in todos_carcteres:
                if caracter_mensagem == caracter: #se o caracter da mensagem for o mesmo do alfabeto, pega o index da matriz identidade do alfabeto
                    index_caracter = todos_carcteres.index(caracter)
                    lista_index_caracteres_mensagem.append(index_caracter)

        #cria a matriz da mensagem a pegando cada index de cada caracter na matriz identidade do alfabeto
        mensagem_traduzida = matriz_identidade_todos_char[:,lista_index_caracteres_mensagem]

        return mensagem_traduzida

def para_string(M=np.array):

    #mensagem final
    mensagem_traduzida = ""

    #transformando o array para poder transforma-lo
    M = np.transpose(M)

    #pegando a matriz identidade do alfabeto
    matriz_identidade_todos_char, todos_carcteres = matriz_identidade_alfabeto()

    #lista com os indexes de cada caracter dentro da lista alfabeto
    lista_index_letras_matriz = []
    index_matriz_id = 0 
    for coluna_matriz_mensagem in M:
        index_matriz_id = 0
        for coluna_matriz_id in matriz_identidade_todos_char:
            index_matriz_id += 1
            if np.all(coluna_matriz_mensagem == coluna_matriz_id): # se a coluna da matriz recebida for igual a matriz do alfabeto, pega o index da matriz do alfabeto
                lista_index_letras_matriz.append(index_matriz_id-1)
                index_matriz_id = 0

    #pega os indexes da lista e cria a mensagem traduzida da matriz, dado que o index da matriz identidade do alfabeto tem o mesmo index e representa cada letra do alfabeto
    for index_letra in lista_index_letras_matriz:
        mensagem_traduzida += todos_carcteres[index_letra]

    return mensagem_traduzida

def cifrar(msg=str,P=np.array):

    #verificando se todos os carcteres da mensagem estao no alfabeto que esta sendo utilizado
    if teste_mensagem(msg):

        #transformando a mensagem para matriz
        matriz_mensagem = para_one_hot(msg)

        #multiplicando a matriz por uma matriz permutacao P, criando a matriz da mensagem codificada
        matriz_codificada = P@matriz_mensagem

        #transformando a matriz codificada para mensagem, formando a mensagem codificada
        mensagem_codificada = para_string(matriz_codificada)

        return mensagem_codificada

def de_cifrar(msg=str,P=np.array):

    #verificando se todos os carcteres da mensagem estao no alfabeto que esta sendo utilizado
    if teste_mensagem(msg):

        #transformando a mensagem codificada para matriz
        matriz_mensagem_codificada = para_one_hot(msg)

        #invertendo a matriz permutacao P
        inverso_P = np.linalg.inv(P)

        #multiplicando o inverso de P pela matriz da mensagem codificada para conseguir a matriz da mensagem original, nao codificada
        matriz_de_codificada =  inverso_P @ matriz_mensagem_codificada 

        #transformando a matriz decodificada para mensagem, formando a mensagem decodificada
        mensagem_de_codificada = para_string(matriz_de_codificada)

        return mensagem_de_codificada

def enigma(msg=str,P=np.array, E=np.array):

    #verificando se todos os carcteres da mensagem estao no alfabeto que esta sendo utilizado
    if teste_mensagem(msg):

        #lista para salvar cada caracter da mensagem codificada
        matriz_codificada = []

        #transformando a mensagem codificada para matriz
        matriz_mensagem = para_one_hot(msg)

        #transposicao da matriz da mensagem
        matriz_mensagem = matriz_mensagem.T

        for i in range(len(msg)):
            #primeira letra apenas multiplicar por P
            if i == 0:
                letra_codificada = P @ matriz_mensagem[i] #primeiro caracter codificado em matriz
            else:
                letra_codificada = matriz_mensagem[i]
                #multiplicar por E o caracter, a quantidade de vezes que for o tamanho de i, ou seja, apos a primeira execucao, multiplicamos o proximo caracter sempre por mais um E, criando matrizes de cada caracter que foram codificadas todas por multiplicacoes diferentes
                for j in range(i):
                    letra_codificada = E @ letra_codificada
                letra_codificada = P @ letra_codificada
            matriz_codificada.append(letra_codificada) # adicionando cada matriz dos caracteres codificados em uma lista

        #transformando a lista de caracteres codificados em uma matriz np
        matriz_codificada = np.array(matriz_codificada)

        #transformando a matriz codificada(apos sua transposicao) para mensagem, formando a mensagem codificada
        mensagem_codificada = para_string(np.array(matriz_codificada.T))

        return mensagem_codificada 

def de_enigma(msg=str,P=np.array, E=np.array):

    #verificando se todos os carcteres da mensagem estao no alfabeto que esta sendo utilizado
    if teste_mensagem(msg):
        #lista para salvar cada caracter da mensagem codificada
        matriz_decodificada = []

        #transformando a mensagem codificada para matriz
        matriz_mensagem_codificada = para_one_hot(msg)

        #transposicao da matriz da mensagem
        matriz_mensagem_codificada = matriz_mensagem_codificada.T

        #criando o inverso das matrizes de permutacao P e E 
        inverso_P = np.linalg.inv(P)
        inverso_E = np.linalg.inv(E)

        for i in range(len(msg)):
            letra_decodificada = matriz_mensagem_codificada[i]
            if i == 0:
                letra_decodificada = inverso_P @ letra_decodificada #a matriz decodificada do primeiro caracter é a multiplicacao do inverso de P pela matriz codificada do caracter
            else:
                letra_decodificada = inverso_P @ letra_decodificada
                for _ in range(i): #a matriz decodificada dos caracteres apos o primeiro sao o (inverso de P vezes a matriz do caracter codificado) vezes o inverso de E (varia quantas vezes o inverso de E é multiplicado, de acordo com quantas vezes E foi multiplicado para formar a matriz do caracter codificado)
                    letra_decodificada = inverso_E @ letra_decodificada
            matriz_decodificada.append(letra_decodificada)# adicionando cada matriz dos caracteres decodificados em uma lista

        #transformando a lista de caracteres codificados em uma matriz np + transposicao dessa matriz
        matriz_decodificada = np.array(matriz_decodificada).T

        #transformando a matriz decodificada para mensagem, formando a mensagem decodificada
        mensagem_decodificada = para_string(matriz_decodificada)

        return mensagem_decodificada

