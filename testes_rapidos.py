from funções.funcoes_criadas import *

#Criando as permutações 
P = permutacao_identidade()
E = permutacao_identidade()

# Mensagem de exemplo
mensagem = "LipeTheBarber"

# Demonstrando o funcionamento de para_one_hot e para_string
print("Demonstração de para_one_hot e para_string:")
mensagem_one_hot = para_one_hot(mensagem)
print("Mensagem em one-hot encoding:")
print(mensagem_one_hot)
mensagem_string = para_string(mensagem_one_hot)
print("Mensagem convertida de volta para string:")
print(mensagem_string)

# Demonstrando o funcionamento de cifrar e de_cifrar
print("\nDemonstração de cifrar e de_cifrar:")
mensagem_cifrada = cifrar(mensagem, P)
print("Mensagem cifrada:")
print(mensagem_cifrada)
mensagem_decifrada = de_cifrar(mensagem_cifrada, P)
print("Mensagem decifrada:")
print(mensagem_decifrada)

# Demonstrando o funcionamento de enigma e de_enigma
print("\nDemonstração de enigma e de_enigma:")
mensagem_codificada_enigma = enigma(mensagem, P, E)
print("Mensagem codificada com enigma:")
print(mensagem_codificada_enigma)
mensagem_decodificada_enigma = de_enigma(mensagem_codificada_enigma, P, E)
print("Mensagem decodificada do enigma:")
print(mensagem_decodificada_enigma)