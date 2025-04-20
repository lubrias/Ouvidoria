from operacoesbd import *
from mainOuvidoria import *

'''
1)Listagem de manifestações
2) Listagem de manifestações por tipo
3) Criar uma manifestação
4) Exibir quantidade de manifestações
5) Pesquisar uma manifestação por código
6) Excluir uma manifestação pelo código
7) Sair do sistema
'''

#Menu principal
while True:
    print(
        "Bem-vindo à Ouvidoria Unifacisa! \n"
        "Opções: \n"
        "1) Listar manifestações cadastradas \n"
        "2) Listar manifestações por tipo\n"
        "3) Criar uma nova manifestação \n"
        "4) Exibir quantidade de manifestações\n"
        "5) Pesquisar manifestação por código\n"
        "6) Excluir manifestação por código\n"
        "7) Sair do sistema\n"
        )
    
    #User digita a opção
    opcao = int(input("Digite sua opção: "))

    #Listagem de manifestações cadastradas:
    if opcao == 1:
        manifestacaoTotal(conn)
    
    #Listagem de manifestações por tipo:
    elif opcao == 2:
        manifestacaoPorTipo(conn)

    #Adicionar uma nova manifestação:
    elif opcao == 3:
        criarNovaManifestacao(conn)

    #Exibir a quantidade manifestações existentes:
    elif opcao == 4:
        quantidadeManifestacoes(conn)

    #Pesquisar manifestação por código:
    elif opcao == 5:
        pesquisaPorCodigo(conn)

    #Excluir manifestação por código:
    elif opcao == 6:
        excluirManifestacao(conn)
    
    #Sair do sistema:
    elif opcao == 7:
        print("Obrigado. Volte sempre!\n")
    
    elif opcao !=7:
        print("Número inválido. Digite um número de 1 a 7.")
        break
