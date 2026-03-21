import math
def show_menu():
    print('\n======= MENU PRINCIPAL ==================')
    print('SELECIONE UMA OPERAÇÃO:\n')
    print('[1]  Adição (+)')
    print('[2]  Subtração (-)')
    print('[3]  Multiplicação (*)')
    print('[4]  Divisão (/)') 
    print('[5]  Potenciação (x^y)')
    print('[6]  Raiz quadrada ')
    print('[7]  Seno (sin)')
    print('[8]  Cosseno (cos)')
    print('[9]  Tangente (tan)')
    print('[10] Porcentagem (%)')
    print('[11] Log base 10 (log)')
    print('[12] Log natural (ln)')
    print('[13] Média (x̄)')
    print('[14] Exponencial (e^x)')
    print('[15] Fatorial (!)')
    print('[16] Valor absoluto (abs)')
    print('[17] Número π ')
    print('[18] Modo radiano (RAD)')
    print('[19] Última resposta (Ans)')
    print('[20] Histórico (Ans)')
    print('[21].Sair do Menu')
    print(40*'=')
    

def exibir_boas_vindas():

    print("==================================================")
    print("           BEM VINDO FAÇA SEU CALCULO             ")
    print(f"        Sistema Desenvolvido para: Senai         ")
    print("==================================================")
 
def alterar_nome_empresa():
    codigo = input("Digite o código: ")

    if codigo == "8U6T":
        novo_nome = input("Digite o novo nome: ")

        with open("dados/empresa.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(novo_nome)

        print("Nome da empresa alterado com sucesso.")
print(alterar_nome_empresa())
