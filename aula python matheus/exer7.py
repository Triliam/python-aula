#Construa um programa que utilize um dicionário para armazenar nomes de alunos e suas respectivas notas. Implemente funções para:
#    - Adicionar um novo aluno com sua nota;
#    - Remover um aluno;
#    - Calcular a média de todas as notas;
#    - Identificar o aluno com a maior nota.
#    Dica: Modularize seu código criando funções para cada operação.

notas_alunos = {}
# soma = 0
# maior = 0

def adicionar_aluno(nome, nota):
    notas_alunos[nome] = nota
    print(f"Aluno {nome} adicionado com sucesso.")

def remover_aluno(nome):
    if nome in notas_alunos:
        del notas_alunos[nome]
        print(f"Aluno {nome} removido com sucesso.")
    else:
        print(f"Aluno {nome} não encontrado.")

def calcular_media():
    # soma = notas_alunos.values() + soma
    # med = soma / len(notas_alunos)
    media = sum(notas_alunos.values()) / len(notas_alunos)
    print(f"A média das notas é: {media:.2f}")

def aluno_com_maior_nota():
    # for n in notas_alunos.values():
    #     if n > maior:
    #         maior = n
    aluno = max(notas_alunos, key=notas_alunos.get)
    maior_nota = notas_alunos[aluno]
    print(f"O aluno com a maior nota é {aluno} com a nota {maior_nota}.")

def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Calcular média das notas")
    print("4. Identificar aluno com a maior nota")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    return opcao

def main():
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            nota = float(input(f"Digite a nota do aluno {nome}: "))
            adicionar_aluno(nome, nota)
        elif opcao == "2":
            nome = input("Digite o nome do aluno a ser removido: ")
            remover_aluno(nome)
        elif opcao == "3":
            calcular_media()
        elif opcao == "4":
            aluno_com_maior_nota()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
