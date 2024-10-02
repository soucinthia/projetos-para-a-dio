# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.


num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o primeiro numero: "))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    print(num1 / num2)

else:
    print("Operação inválida. Por favor, digite uma das seguintes operações: +, -, *, /")



#Copilot:Claro! Vamos analisar o algoritmo linha por linha:

"""
 num1 = int(input("Digite o primeiro numero: "))
 Esta linha solicita ao usuário que digite o primeiro número. 
 O valor digitado é convertido para um inteiro usando a função int() e armazenado na variável num1.

 num2 = int(input("Digite o primeiro numero: "))
 Esta linha solicita ao usuário que digite o segundo número. 
 Novamente, o valor digitado é convertido para um inteiro e armazenado na variável num2. 
 Note que há um pequeno erro de digitação na mensagem de entrada, que deveria ser "Digite o segundo número: ".

 operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")
 Esta linha solicita ao usuário que digite a operação que deseja realizar. 
 O valor digitado é armazenado na variável operacao.

 if operacao == '+':
 Esta linha verifica se a operação digitada é a adição (+). Se for, executa o bloco de código seguinte.
 print(num1 + num2)
 Se a operação for adição, esta linha imprime a soma dos dois números.
   
 elif operacao == '-':
 Esta linha verifica se a operação digitada é a subtração (-). Se for, executa o bloco de código seguinte.
 print(num1 - num2)
 Se a operação for subtração, esta linha imprime a diferença entre os dois números.
    
 elif operacao == '*':
 Esta linha verifica se a operação digitada é a multiplicação (*). Se for, executa o bloco de código seguinte.
 print(num1 * num2)
 Se a operação for multiplicação, esta linha imprime o produto dos dois números.
    
 elif operacao == '/':
 Esta linha verifica se a operação digitada é a divisão (/). Se for, executa o bloco de código seguinte.
 print(num1 / num2)
 Se a operação for divisão, esta linha imprime o quociente dos dois números.
    
 else:
 Esta linha captura qualquer operação que não seja uma das especificadas (+, -, *, /).
 print("Operação inválida. Por favor, digite uma das seguintes operações: +, -, *, /")
 Se a operação digitada não for válida, esta linha imprime uma mensagem de erro informando que a operação é inválida.
    
 Aqui está um exemplo de como o algoritmo funciona:

 Se o usuário digitar 10 como o primeiro número, 5 como o segundo número e + como a operação, a saída será:
 15
"""