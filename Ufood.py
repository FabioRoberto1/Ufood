import os

restaurantes = [{'nome':'Leno Bar', 'categoria':'Bar', 'ativo': True},
                {'nome':'Don Cello', 'categoria':'Pizzaria', 'ativo': False},
                {'nome':'Doce da Mamãe', 'categoria':'Lanchonete', 'ativo': True}]

def exibir_nome_do_programa():
    '''
    Exibe nome do app estilizado no menu principal
    '''
    print('''

██╗░░░██╗███████╗░█████╗░░█████╗░██████╗░
██║░░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
██║░░░██║█████╗░░██║░░██║██║░░██║██║░░██║
██║░░░██║██╔══╝░░██║░░██║██║░░██║██║░░██║
╚██████╔╝██║░░░░░╚█████╔╝╚█████╔╝██████╔╝
░╚═════╝░╚═╝░░░░░░╚════╝░░╚════╝░╚═════╝░
          ''')

def exibir_opcoes():
    '''
    Opçoes do disponiveis no menu 
    1 - Cadastro de Rest.
    2 - Lista de Rest. cadastrados
    3 - Altera o status do Rest.
    4 - Finaliza o App
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' 
    Função numero 4 das opçoes do menu
    Finalizar app
    '''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    ''' 
       Outputs: Volta ao menu principal 
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    ''' 
    Função que limita escolha do usuario

    Outputs: volta para o menu principal
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''
    Função p/ exibir subtitulos em todas a funções do menu principal

    Inputs: - Texto - str
    '''
    os.system('cls')
    linha = '★ ' * (len(texto) + 4)
    print(linha)
    print('\n')
    print(texto)
    print('\n')
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''
    Função responsavel por cadastrar novo restaurante

    Inputs: Nome do rest. & categoria

    Outputs: Add novo rest. na lista
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}. ')
    dados_do_rest = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_rest)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''
    Lista de rest. cadastrados (ativos/desativados)

    Outputs: Exibe a lista na tela
    '''
    exibir_subtitulo('Listando restaurantes')

    print(f'{'◆ Nome do Restaurante'.ljust(20)} {'◆ Categoria'.ljust(20)} | {'◆ Status'}')
    for restaurante in restaurantes:
        nome_rest = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante ['ativo'] else 'desativado'
        print(f'{ nome_rest.ljust(21)} |{ categoria.ljust(19)} |{ ativo}')

    voltar_ao_menu_principal()

def alterar_status_rest():
    '''
    Altera status do rest. (ativo/desativado)

    Outputs:
    Exibe mensagem indicano ativo ou desativado
    '''
   
    exibir_subtitulo('Alterar estado do restaurante')
    nome_rest = input('Digite restaurante que deseja alterar. ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_rest == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_rest} foi ativado com sucesso!' if restaurante['ativo'] else f'0 Restaurante {nome_rest} desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')


    voltar_ao_menu_principal()

def escolher_opcao():
    '''
    Menu p/ o usuario operar o App

    Outputs: Executa opção escolhida pelo usuario
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alterar_status_rest()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''
    Função que inicia o app
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()