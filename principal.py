def somar(numero1, numero2):
    res = numero1 + numero2
    return res

def executar_sistema():
    while True:


        opcao = int(input("numero int"))
        if opcao == 1:
            print("Somando...")
            somar()

            
        if opcao == "0":
            print("Encerrando o sistema...")
            break