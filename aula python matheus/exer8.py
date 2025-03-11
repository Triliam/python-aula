# Crie um programa que leia um texto inserido pelo usuário e determine qual palavra aparece com maior frequência. Para isso, normalize o texto (convertendo para minúsculas e removendo pontuações) e utilize um dicionário para contabilizar as ocorrências.
#    Dica: As funções da biblioteca string podem ajudar na remoção de pontuações.

import string

# Função para normalizar o texto (convertendo para minúsculas e removendo pontuação)
def normalizar_texto(texto):
    # Converte para minúsculas
    texto = texto.lower()
    # Remove pontuação usando string.punctuation
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    return texto

# Função para contar a frequência de palavras
def contar_frequencia_palavras(texto):
    # Normaliza o texto
    texto_normalizado = normalizar_texto(texto)
    # Divide o texto em palavras
    palavras = texto_normalizado.split()
    
    # Dicionário para contar as ocorrências das palavras
    frequencia = {}
    
    # Conta as ocorrências de cada palavra
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
    
    return frequencia

# Função para encontrar a palavra com maior frequência
def palavra_mais_frequente(frequencia):
    # Identifica a palavra com a maior frequência
    palavra = max(frequencia, key=frequencia.get)
    return palavra, frequencia[palavra]

# Função principal
def main():
    # Solicita ao usuário para digitar um texto
    texto = input("Digite um texto: ")
    
    # Conta a frequência das palavras
    frequencia = contar_frequencia_palavras(texto)
    
    # Encontra a palavra mais frequente
    palavra, qtd = palavra_mais_frequente(frequencia)
    
    # Exibe o resultado
    print(f"A palavra mais frequente é '{palavra}' com {qtd} ocorrências.")

# Executa o programa
if __name__ == "__main__":
    main()
