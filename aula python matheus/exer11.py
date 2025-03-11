# Crie um programa que solicite ao usuário uma frase e, em seguida, separe essa frase em palavras, armazenando-as em uma lista. O programa deve exibir:
#     - A quantidade total de palavras;
#     - A primeira palavra;
#     - A última palavra.
#     Dica: Utilize o método split() para separar as palavras da frase.

# Função principal para manipular a string e exibir as informações
def main():
    # Solicita ao usuário que digite uma frase
    frase = input("Digite uma frase: ")
    
    # Separa a frase em palavras utilizando o método split()
    palavras = frase.split()
    
    # Exibe as informações solicitadas
    print(f"Quantidade total de palavras: {len(palavras)}")
    if palavras:
        print(f"A primeira palavra: {palavras[0]}")
        print(f"A última palavra: {palavras[-1]}")
    else:
        print("A frase está vazia.")

# Executa o programa
if __name__ == "__main__":
    main()
