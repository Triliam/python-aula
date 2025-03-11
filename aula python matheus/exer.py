#  Crie um programa em Python que solicite ao usuário dois números inteiros e exiba o resultado da soma, subtração, multiplicação e divisão (garantindo que não haja divisão por zero).Dica: Utilize a função input() para receber os dados e converta-os para o tipo numérico adequado.

n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o primeiro número:"))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2

if n1 != 0:
    div = n1 / n2
else: "Não é possivel dividir"

print(f"Soma: {soma}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {mult}")
print(f"Divisão: {div}")



