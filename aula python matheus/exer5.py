#Desenvolva um programa que receba uma lista de números (ou palavras) e retorne um dicionário onde as chaves são os elementos da lista e os valores representam a quantidade de vezes que cada elemento aparece. Dica: Utilize o método get() dos dicionários para facilitar a contagem.


def contar_frequencia(lista):
    frequencia = {}  
    for elemento in lista:
        if elemento in frequencia:
            frequencia[elemento] += 1
        else:
            frequencia[elemento] = 1
    return frequencia

# Solicita ao usuário para digitar uma lista de números ou palavras
entrada = input("Digite uma lista de elementos separados por espaço: ")
# Converte a entrada para uma lista
lista = entrada.split()

# Chama a função e exibe o resultado
resultado = contar_frequencia(lista)
print(f"Frequência dos elementos: {resultado}")
