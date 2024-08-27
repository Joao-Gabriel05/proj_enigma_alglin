import numpy as np

def matriz_identidade_alfabeto():
    '''
    função para criar a matriz identidade de todos os caracteres do alfabeto
    '''
    #associando todo o alfabeto para uma matriz identidade
    todos_carcteres = "abcdefghijklmnopqrstuvwxyz "
    tamanho_matrix_identidade = len(todos_carcteres)
    matriz_identidade_todos_char = np.identity(tamanho_matrix_identidade)

    return matriz_identidade_todos_char, todos_carcteres

def permutacao_identidade():
    '''
    funçao para criar a matriz identidade do alfabeto mas, toda permutada e toda vez que é chamada, gera uma permutação diferente
    '''

    matriz_identidade_todos_char, todos_carcteres = matriz_identidade_alfabeto()

    matriz_identidade_mensagem = np.identity(len(todos_carcteres))
    matriz_identidade_mensagem_permutada = np.random.permutation(matriz_identidade_mensagem)
    
    return matriz_identidade_mensagem_permutada

def teste_mensagem(mensagem):
    '''
    função para ver se a mensagem que o ususario mandou apresenta todos os caracteres dentro do alfabeto ou noa é uma string vazia
    '''

    if mensagem == "" or mensagem == " ":
        return "Não envie uma mensagem vazia"
    
    mensagem = mensagem.lower()
    
    todos_carcteres = "abcdefghijklmnopqrstuvwxyz "

    for caracter in mensagem:
        if caracter not in todos_carcteres:
            return ("Não use caracteres especiais, apenas os presentes na lista ['abcdefghijklmnopqrstuvwxyz '](contando o espaço)")
    
    return True

    

