def dividir(numero1, numero2):
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = dividir(numero1, numero2)
        print(resultado)

    except ValueError:
        print("Entrada inválida. Digite apenas números.")

    except ZeroDivisionError:
        print("Não é possível dividir por zero.")



def errolog(tipo_erro, mensagem):
    from datetime import datetime

    agora = datetime.now()
    data = f"{agora.day:02d}/{agora.month:02d}/{agora.year} {agora.hour:02d}:{agora.minute:02d}:{agora.second:02d}"
    linha = f"{data} | {tipo_erro} | {mensagem}\n"

    with open("dados/erros_log.txt", "a", encoding="utf-8") as arq:
        arq.write(linha)