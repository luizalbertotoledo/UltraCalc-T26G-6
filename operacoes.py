#preciso multiplicar as pastas e separar os documentos para backup.
from os import system as lt
lt("cls")

def multiplicar (pasta1, pasta2):
    res = pasta1 * pasta2
    return res

resultado = multiplicar (10, 8)
print ("Pastas Multiplicadas:")
print(resultado)

def separador_doc (doc01, doc02):
    res = doc01 * doc02
    return res 

separacao = separador_doc (45, 7)
print ("Documentos Separados:")
print(separacao)