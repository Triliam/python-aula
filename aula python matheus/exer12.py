#  Elabore um programa que permita ao usuário inserir as notas de uma turma. As notas devem ser armazenadas em uma lista. O programa deve:
#     - Permitir a inserção das notas até que o usuário digite um valor negativo;
#     - Validar que cada nota esteja entre 0 e 10 (descartando valores inválidos);
#     - Exibir a média das notas válidas e a quantidade de notas consideradas.
#     Dica: Utilize um loop while para controlar a entrada de dados e estruturas condicionais para validar cada nota.

# Função principal para inserir as notas e calcular a média
def main():
    notas = []  # Lista para armazenar as notas válidas
    while True:
        try:
            # Solicita ao usuário para inserir uma nota
            nota = float(input("Digite uma nota entre 0 e 10 (ou um valor negativo para encerrar): "))
            
            # Se o usuário digitar um valor negativo, o loop é encerrado
            if nota < 0:
                break
            
            # Validação da nota
            if 0 <= nota <= 10:
                notas.append(nota)  # Adiciona a nota à lista
            else:
                print("Nota inválida! A nota deve estar entre 0 e 10.")
        
        except ValueError:
            # Trata o caso de o usuário inserir algo que não seja um número
            print("Entrada inválida! Por favor, insira um número válido.")
    
    # Se houver notas válidas, calcula e exibe a média
    if notas:
        media = sum(notas) / len(notas)  # Calcula a média das notas
        print(f"\nQuantidade de notas válidas: {len(notas)}")
        print(f"Média das notas: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi inserida.")

# Executa o programa
if __name__ == "__main__":
    main()
