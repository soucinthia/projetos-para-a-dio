# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

print(string * numero)



#Copilot: Vamos analisar o algoritmo linha por linha:

"""
 string = input("Digite uma string: ")
 Esta linha solicita ao usuário que digite uma string (uma sequência de caracteres). O valor digitado pelo usuário é armazenado na variável string.

 numero = int(input("Digite um número inteiro: "))
 Esta linha solicita ao usuário que digite um número inteiro. O valor digitado é convertido para um inteiro usando a função int() e 
 armazenado na variável numero.

 print(string * numero)
 Esta linha imprime a string digitada pelo usuário repetida o número de vezes especificado pelo valor inteiro. Em Python, o operador * 
 pode ser usado para repetir uma string. Por exemplo, se string for “abc” e numero for 3, o resultado será “abcabcabc”.

 Aqui está um exemplo de como o algoritmo funciona:

 Se o usuário digitar “hello” como string e 3 como número inteiro, a saída será:
 hellohellohello

 Imprime a string com espaços repetida o número de vezes especificado pelo usuário, com um espaço adicional entre cada repetição.
 print((string_com_espacos + ' ') * numero)
 """