#Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.

numero = int(input("Digite um número inteiro: "))


if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")



#Copilot: Vamos analisar o algoritmo linha por linha:

"""
 Explicação do Algoritmo:
 numero = int(input("Digite um número inteiro: "))
 Esta linha solicita ao usuário que digite um número inteiro. 
 O valor digitado é convertido para um inteiro usando a função int() e armazenado na variável numero.

 if numero % 2 == 0:
 Esta linha verifica se o número é par. 
 O operador % (módulo) é usado para obter o resto da divisão do número por 2. Se o resto for 0, o número é par.
 print("O número", numero, "é par.")
 Se a condição do if for verdadeira (ou seja, o número é par), esta linha imprime que o número é par.

 else:
 Esta linha captura o caso em que a condição do if não é verdadeira (ou seja, o número não é par).
 print("O número", numero, "é ímpar.")
 Se a condição do if não for verdadeira, esta linha imprime que o número é ímpar.
"""