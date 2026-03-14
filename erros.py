def potencia(base, expoente):
    res = base ** expoente
    return res

def dividir(a, b):
    return a/b

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    resultado = dividir(numero1, numero2)
    print(f"O resultado é: {resultado}")

except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
