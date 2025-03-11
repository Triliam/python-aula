# Desenvolva um programa que receba uma lista de números inteiros fornecidos pelo usuário e ordene essa lista em ordem crescente utilizando o algoritmo Bubble Sort (ou outro de sua preferência, implementado manualmente). Em seguida, exiba a lista ordenada.
#     Dica: Implemente o algoritmo sem usar funções prontas de ordenação.

# Função para implementar o algoritmo Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    # Percorre todos os elementos da lista
    for i in range(n):
        # Últimos elementos já estão na posição correta, então diminuímos a comparação
        for j in range(0, n - i - 1):
            # Se o elemento atual é maior que o próximo, troque-os
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Função principal para receber a entrada do usuário e ordenar a lista
def main():
    # Recebe uma lista de números inteiros do usuário
    entrada = input("Digite uma lista de números inteiros separados por espaço: ")
    lista_numeros = [int(num) for num in entrada.split()]
    
    # Ordena a lista usando o Bubble Sort
    bubble_sort(lista_numeros)
    
    # Exibe a lista ordenada
    print("Lista ordenada em ordem crescente:", lista_numeros)

# Executa o programa
if __name__ == "__main__":
    main()
