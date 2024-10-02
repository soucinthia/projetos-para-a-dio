# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?

info1 = input("Digite a primeira informação: ")
info2 = input("Digite a segunda informação: ")

info_concatenada = info1 + " " + info2

print("As informações concatenadas são: ", info_concatenada)


# Copilot: Vamos analisar o algoritmo linha por linha:
"""
 info1 = input("Digite a primeira informação: ")
 Esta linha solicita ao usuário que digite a primeira informação. O valor digitado pelo usuário é armazenado na variável info1.

 info2 = input("Digite a segunda informação: ")
 Esta linha solicita ao usuário que digite a segunda informação. O valor digitado pelo usuário é armazenado na variável info2.

 info_concatenada = info1 + " " + info2
 Esta linha concatena (ou seja, junta) as duas informações digitadas pelo usuário, adicionando um espaço entre elas.
 O resultado é armazenado na variável info_concatenada.

 print("As informações concatenadas são: ", info_concatenada)
 Esta linha imprime a mensagem "As informações concatenadas são: " seguida do valor da variável info_concatenada, 
 que contém as duas informações unidas por um espaço.

 Aqui está um exemplo de como o algoritmo funciona:
 Se o usuário digitar “Olá” como a primeira informação e “Mundo” como a segunda, a saída será:
 As informações concatenadas são: Olá Mundo
"""