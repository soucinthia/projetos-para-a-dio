#vamos calcular a média de três notas fornecidas na entrada do usuário

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("A média das três notas é:", media)


# Copilot: Vamos analisar o algoritmo linha por linha:
"""
 Explicação do Algoritmo:

 Entrada de Dados:
 nota1 = float(input("Digite a primeira nota: "))
 nota2 = float(input("Digite a segunda nota: "))
 nota3 = float(input("Digite a terceira nota: "))
 Essas linhas solicitam ao usuário que digite três notas. A função input() recebe a entrada do usuário como uma string, 
 e a função float() converte essa string em um número de ponto flutuante (decimal).

 Cálculo da Média:
 media = (nota1 + nota2 + nota3) / 3
 Esta linha soma as três notas e divide o resultado por 3 para calcular a média.

 Saída de Dados:
 print("A média das três notas é:", media)
 Esta linha imprime a média calculada.
"""