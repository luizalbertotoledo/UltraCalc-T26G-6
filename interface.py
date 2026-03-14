def alterar_nome_empresa():
    codigo = input("Digite o código: ")

    if codigo == "8U6T":
        novo_nome = input("Digite o novo nome: ")

        with open("dados/empresa.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(novo_nome)

        print("Nome da empresa alterado com sucesso.")
print(alterar_nome_empresa())