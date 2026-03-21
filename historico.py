with open("dados/historico.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            
            print("--- Histórico de Operações ---")
            print(conteudo)
            print("-------------------------------")