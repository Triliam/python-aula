# Crie uma função que receba uma string como parâmetro e retorne essa string invertida. Em seguida, peça ao usuário para digitar uma frase, chame a função e exiba o resultado. Dica: Utilize slicing de strings (ex.: texto[::-1]).


def inverter_string(texto):
    return texto[::-1]

frase = input("Digite uma frase: ")

resultado = inverter_string(frase)
print(frase)
print(f"A frase invertida é: {resultado}")