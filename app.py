import os

restaurante = []

def encerrar_app():
    os.system('cls')
    print('Encerrando o app')

def exibir_nome_do_programa():
    print('Sabor express')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Finalizar o app')

def opcao_invalida():
    print('Opção invalidade\n')
    input('Digite uma tecla para continuar')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = input("Escolha uma opção: ")
        opcao_escolhida = int(opcao_escolhida)
    
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            print(restaurante)
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            encerrar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def listar_restaurante():
    os.system('cls')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    print('Digite enter')
    main()


def cadastrar_restaurante():
    os.system('cls')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurante.append(nome_do_restaurante)
    input('Pressiona qualquer tecla para voltar ao menu')
    main()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()