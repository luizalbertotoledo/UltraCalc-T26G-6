def errolog(tipo_erro, mensagem):
    from datetime import datetime

    agora = datetime.now()
    data = f"{agora.day:02d}/{agora.month:02d}/{agora.year} {agora.hour:02d}:{agora.minute:02d}:{agora.second:02d}"
    linha = f"{data} | {tipo_erro} | {mensagem}\n"

    with open("dados/erros_log.txt", "a", encoding="utf-8") as arq:
        arq.write(linha)