"""
Classificador de números pares e ímpares

Classifica um númeiro inteiro como par ou ímpar usando a lógica de resto da divisão
"""
numero = int (input ("Digite um número: ") )

if numero % 2 == 0:
    print ("O numero é par")
else:
    print ("O número é ímpar ")
