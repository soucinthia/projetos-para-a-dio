#Vamos testar se uma palavra é um palíndromo? Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

palavra = input("Digite uma palavra: ")

palavra = palavra.lower()

palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")


#Copilot: Vamos analisar o algoritmo linha por linha:

"""
 Explicação do Algoritmo:

 Entrada de Dados:
 palavra = input("Digite uma palavra: ")
 Esta linha solicita ao usuário que digite uma palavra. O valor digitado é armazenado na variável palavra.

 Conversão para Minúsculas:
 palavra = palavra.lower()
 Esta linha converte a palavra para minúsculas para garantir que a comparação não seja afetada por diferenças de maiúsculas e minúsculas.

 Inversão da Palavra:
 palavra_invertida = palavra[::-1]
 Esta linha inverte a palavra usando fatiamento de strings. O fatiamento [::-1] cria uma nova string que é a versão invertida da original.

 Verificação de Palíndromo:
 if palavra == palavra_invertida:
 Esta linha compara a palavra original com a palavra invertida.

 print("A palavra é um palíndromo.")
 Se as duas palavras forem iguais, esta linha imprime que a palavra é um palíndromo.

 else:
 Esta linha captura o caso em que a palavra original e a palavra invertida não são iguais.

 print("A palavra não é um palíndromo.")
 Se as duas palavras não forem iguais, esta linha imprime que a palavra não é um palíndromo.
"""