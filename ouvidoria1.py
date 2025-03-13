'''
Projeto Ouvidoria
Sistema de ouvidoria da unifacisa com menu de 5 opções
1)Listagem das manifestações. 2)Criar uma nova manifestação. 3)Exibir a quantidade de manifestações. 4) Pesquisar uma manifestação por código. 5) Sair
'''
opcao = -1
listamanifest = [   ]

while opcao !=5:
    print('Bem-vindo a Ouvidoria UniFacisa.')
    print('Digite as opções à seguir para saber mais:')
    print('Opções:\n1) Listagem de manifestações.\n2) Criar uma nova manifestação.\n3) Exibir a quantidade de manifestações.\n4) Pesquisar uma manifestação por código.\n5) Sair')
    opcao = int(input('Digite a opção que você quer: '))

    if opcao == 1:
        print('Aqui você verá a listagem de manifestações.')
        print('Listagem de manifestações:')
        if len(listamanifest) == 0:
            print('Nenhuma manifestação adicionada até agora.')
            print()
        
        else:
           for item in range(len(listamanifest)):
               print(item+1,')',listamanifest[item])
               


    elif opcao == 2:
        print('Crie sua manifestação abaixo')
        while True:
            manifest = input('Digite sua crítica: ').strip()
            if len(manifest) < 8:
                print('Digite uma reclamação válida')
            else:
                break
        listamanifest.append(manifest)
        print('Sua manifestação foi lançada à Ouvidoria. Verifique se está na lista digitando 1.')
        print()

    elif opcao == 3:
        codmanifest = len(listamanifest)
        print(int(codmanifest),'manifestação(ões) até agora.')

    elif opcao == 4:
        codPesquisa = int(input('Digite o código a ser pesquisado: '))
        if codPesquisa >= 1 and codPesquisa <= len(listamanifest):
            codPesquisado = listamanifest[codPesquisa-1]
            print(codPesquisa,')',codPesquisado)
        else:
            print('Não há manifestação com esse código que você digitou.') 
    elif opcao == 5:
        print()
        print('Obrigado. Volte sempre!')

    elif opcao != 5:
        print('Digite um código válido. Por favor.')
