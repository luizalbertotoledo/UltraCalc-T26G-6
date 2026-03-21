def executar_sistema():
    while True:
        exibir_boas_vindas()
        exibir_menu()
        opcao = ler_opcao_menu()
        if opcao == 1:
            print("Somando...")
        elif opcao == 2:
            print("Subtraindo...")
        elif opcao == 3:
            print("Multiplicando...")
        elif opcao == 4:
            print("Dividindo...")
        elif opcao == 5:
            print("Potenciando...")
        elif opcao == "0":
            print("Encerrando o sistema...")
            break