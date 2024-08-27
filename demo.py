from funções.funcoes_criadas import *
import numpy as np

#função que roda o demo
def main():
    #loop que mostra as opições para o usuario escolher sua funções
    while True:
        print("\nEscolha uma opção:")
        print("1. Executar a função para_one_hot")
        print("2. Executar a função para_string")
        print("3. Executar a função cifrar")
        print("4. Executar a função de_cifrar")
        print("5. Executar a função enigma")
        print("6. Executar a função de_enigma")
        print("7. Sair")

        escolha = input("Digite o número da sua escolha: ")

        if escolha == '1':
            mensagem_para_one_hot = input("Digite a string para ser convertida para matriz:")
            matriz_para_one_hot = para_one_hot(mensagem_para_one_hot)
            print(matriz_para_one_hot)

        elif escolha == '2':
            matriz_para_string_one_hot = para_string(matriz_para_one_hot)
            print(f"Matriz convertida para string: {matriz_para_string_one_hot}")

        elif escolha == '3':
            P = permutacao_identidade()
            mensagem_cifrar = input("Digite a string para ser codificada:")
            mensagem_cifrar_codificada = cifrar(mensagem_cifrar,P)
            print(mensagem_cifrar_codificada)

        elif escolha == '4':
            mensagem_cifrar_decodificada = de_cifrar(mensagem_cifrar_codificada,P)
            print(f"Mensagem cifrar decodificada: {mensagem_cifrar_decodificada}")

        elif escolha == '5':
            P = permutacao_identidade()
            E = permutacao_identidade()
            mensagem_enigma = input("Digite a string para ser codificada:")
            mensagem_enigma_codificada = enigma(mensagem_enigma,P, E)
            print(mensagem_enigma_codificada)
        elif escolha == '6':
            mensagem_enigma_decodificada = de_enigma(mensagem_enigma_codificada,P,E)
            print(f"Mensagem cifrar decodificada: {mensagem_enigma_decodificada}")
        elif escolha == '7':
            print("Saindo do programa...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
