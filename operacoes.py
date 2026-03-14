import math 

def cosseno (graus):
    radianos = math.radians(graus)
    res = math.cos(radianos)
    return res

resultado = cosseno(float(input("Digite um numero: ")))

print(f"O resultado é {resultado}")