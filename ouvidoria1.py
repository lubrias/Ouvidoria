'''
Projeto Ouvidoria
Sistema de ouvidoria da unifacisa com menu de 5 opções
1)Listagem das manifestações. 2)Criar uma nova manifestação. 3)Exibir a quantidade de manifestações. 4) Pesquisar uma manifestação por código. 5) Sair
'''
opcao = -1
listamanifest = [   ]
pos = 0
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
        
        else:
            for i,item in enumerate(listamanifest):
                print('Manifestação {}) {}'.format(i+1,item))

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

    elif opcao == 3:
        codmanifest = len(listamanifest)
        print(int(codmanifest),'manifestação(ões) até agora.')
