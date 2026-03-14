#Função Tangente

import math

def tangente(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    return math.tan(angulo_radianos)

angulo = float(input("Digite o ângulo em graus: "))
resultado = tangente(angulo)

print("A tangente do ângulo é:", resultado)