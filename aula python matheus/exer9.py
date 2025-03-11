#  Crie um programa que simule o cadastro de produtos em uma loja. Para cada produto, registre o nome, o preço e a quantidade em estoque. Em seguida, permita que o usuário consulte um produto pelo nome e exiba suas informações ou informe que o produto não foi encontrado.
#    Dica: Utilize uma lista para armazenar dicionários, onde cada dicionário representa um produto.

# Lista para armazenar os produtos (cada produto é um dicionário)
produtos = []

# Função para cadastrar um novo produto
def cadastrar_produto(nome, preco, quantidade):
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)
    print(f"Produto {nome} cadastrado com sucesso.")

# Função para consultar um produto pelo nome
def consultar_produto(nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return produto
    return None

# Função principal que executa o programa
def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar produto")
        print("2. Consultar produto")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1-3): ")
        
        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade em estoque: "))
            cadastrar_produto(nome, preco, quantidade)
        
        elif opcao == "2":
            nome = input("Digite o nome do produto a ser consultado: ")
            produto = consultar_produto(nome)
            
            if produto:
                print(f"\nProduto encontrado:")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: R${produto['preco']:.2f}")
                print(f"Quantidade em estoque: {produto['quantidade']}")
            else:
                print(f"Produto '{nome}' não encontrado.")
        
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
