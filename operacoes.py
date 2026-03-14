import math 

def valor_porcentagem (valor, percentual):
    res = (valor * percentual) / 100
    return res

def exponencial(valor):
    res = math.exp(valor)
    return res

def potencia(base, expoente):
    res = base ** expoente
    return res

def media (primeiro, segundo):
    resul = (primeiro + segundo) /2
    return resul

# def somar (valor1, valor2):
#     resultado = valor1 + valor2
#     return resultado

try:
    numero=input("digite um numero ")
    num=int (numero)
    print(num)
except ValueError:
    print("Erro! Digite um número inteiro")
    