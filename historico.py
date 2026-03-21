import json
from datetime import datetime

ARQUIVO_HISTORICO = "historico.json"

def carregar_historico():
    try:
        with open (ARQUIVO_HISTORICO, "r") as f:
            return json.load(f)
    except (FileNotFoundError , json.JSONDecodeError):
        return[]
    
def salvar_historico(historico):
    with open(ARQUIVO_HISTORICO, "w") as f:
        json.dump(historico, f, indent=2, ensure_ascii=False)

def registrar_calculo(expressao, resultado):
    historico = carregar_historico()
    entrada = {
        "id": len(historico) + 1,
        "expressao": expressao,
        "resultado": resultado,
        "data": datetime.now().strftime("%d/%m%y %H:%M:%S")   
    }            
    historico.append(entrada)
    salvar_historico(historico)

# Exemplo de uso
registrar_calculo("2 + 3", 5)
registrar_calculo("10 / 2", 5.0)
registrar_calculo("7 * 8", 56)
