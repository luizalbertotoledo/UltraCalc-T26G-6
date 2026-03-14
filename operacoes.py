
# def somar (valor1, valor2):
#     resultado = valor1 + valor2
#     return resultado

try:
    numero=input("digite um numero ")
    num=int (numero)
    print(num)
    return num
except ValueError:
    print("Erro! Digite um número inteiro")
    