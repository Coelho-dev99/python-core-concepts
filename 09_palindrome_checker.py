"""
Verificador de palíndromos

Recebe uma palavra ou frase é verificar se é um palindromo ( se lendo de trás para frente é a mesma escrita).
"""

def e_palindromo(palavra):
    palavra_invertida = palavra [::-1]

    if palavra == palavra_invertida:
        return True
    else:
        return False

palavra = input("Digite uma palavra:")

print(e_palindromo(palavra))
