from operacoesbd import *
'''
1)Listagem de manifestações
2) Listagem de manifestações por tipo
3) Criar uma manifestação
4) Exibir quantidade de manifestações
5) Pesquisar uma manifestação por código
6) Exclir uma manifestação pelo código
7) Sair do sistema
'''
opcao = -1
conn = criarConexao('127.0.0.1','root','luan1293@','ouvidoriaparte2')

while opcao !=7:
    print('Ouvidoria Geral')
    print('Opções:\n1) Listagem das manifestações\n2) Listagem de manifestações por tipo\n3) Criar uma nova manifestação\n4) Exibir quantidade de manifestações\n5) Pesquisar uma manifestação por código\n6) Excluir uma manifestação pelo código\n7) Sair do sistema')
    opcao = int(input('Digite a opção que você deseja escolher: '))

    if opcao == 1:
        print('Você entrou na sessão: Listagem de manifestações.')
        codeListSQL = 'select * from manifestacoes'
        manifestacoes = listarBancoDados(conn,codeListSQL)

        if len(manifestacoes) == 0:
            print('Não há nenhuma manifestação adicionada.')
        else:
            for item in manifestacoes:
                print('Cód. {}- {}, de: {} para: {}. Categoria: {}'.format(item[0],item[2],item[1],item[4],item[3]))
    
    elif opcao == 2:
        print('Você entrou na sessão: Listagem POR TIPO de manifestações.')
        print('Escolha a opção que você deseja entre: \n1) Reclamação\n2) Elogio\n3) Sugestão')
        tipoManifestacao = int(input('Digite a opção que você deseja escolher: '))

        if tipoManifestacao == 1:
            codeListTypeSQL = "select * from manifestacoes where tipo = 'Reclamação';"
            manifestacaoRec = listarBancoDados(conn,codeListTypeSQL)
            
            if len(manifestacaoRec) == 0:
                print('Nenhuma manifestação de Reclamação feita.')
                
            else:
                
                print('Lista de Manifestações de Reclamação:')
                for item in manifestacaoRec:
                    print('Cód. {}- {}, de: {} para: {}. Categoria: {}'.format(item[0],item[2],item[1],item[4],item[3]))
                
        
        elif tipoManifestacao == 2:
            codeListTypeSQL = "select * from manifestacoes where tipo = 'Elogio';"
            manifestacaoRec = listarBancoDados(conn,codeListTypeSQL)

            if len(manifestacaoRec) == 0:
                print('Nenhuma manifestação de Elogio feita.')
             
            else:
                
                print('Lista de Manifestações de Reclamação:')
                for item in manifestacaoRec:
                    print('Cód. {}- {}, de: {} para: {}. Categoria: {}'.format(item[0],item[2],item[1],item[4],item[3]))
                

        elif tipoManifestacao == 3:
            codeListTypeSQL = "select * from manifestacoes where tipo = 'Sugestão';"
            manifestacaoRec = listarBancoDados(conn,codeListTypeSQL)

            if len(manifestacaoRec) == 0:
                print('Nenhuma manifestação de Sugestão feita.')
                
            else:
                print('Lista de Manifestações de Reclamação:')
                for item in manifestacaoRec:
                    print('Cód. {}- {}, de: {} para: {}. Categoria: {}'.format(item[0],item[2],item[1],item[4],item[3]))



    elif opcao == 3: 
        print('Você entrou na sessão: Criar uma nova manifestação')
        print('Selecione o tipo de manifestação que você quer colocá-la. \n1) Reclamação\n2) Elogio\n3) Sugestão')
        typeNewManifestation = int(input('Selecione o tipo de manifestação: '))


        if typeNewManifestation == 1:
            print('Você entrou em MANIFESTAÇÃO POR RECLAMAÇÃO.')
            autorRec = input('Digite o seu nome: ')
            reclamacao = input('Digite a sua manifestação(reclamação): ')
            ouvidor = input('Digite o nome do ouvidor: ')
            codRecSQL = "insert into manifestacoes(autor,descricao,tipo,ouvidor) values(%s,%s,'Reclamação',%s);"
            dados = [autorRec,reclamacao,ouvidor]
            manifestacoes = insertNoBancoDados(conn,codRecSQL,dados)
            print('Manifestação Salva. Obrigado. Digite 1 para visualizar todas as manifestações.')
            

        if typeNewManifestation == 2:
            print('Você entrou em MANIFESTAÇÃO POR ELOGIO.')
            autorRec = input('Digite o seu nome: ')
            reclamacao = input('Digite a sua manifestação(elogio): ')
            ouvidor = input('Digite o nome do ouvidor: ')
            codRecSQL = "insert into manifestacoes(autor,descricao,tipo,ouvidor) values(%s,%s,'Elogio',%s);"
            dados = [autorRec,reclamacao,ouvidor]
            manifestacoes = insertNoBancoDados(conn,codRecSQL,dados)
            print('Manifestação Salva. Obrigado. Digite 1 para visualizar todas as manifestações.')
            

        if typeNewManifestation == 3:
            print('Você entrou em MANIFESTACÃO POR SUGESTÃO.')
            autorRec = input('Digite o seu nome: ')
            reclamacao = input('Digite a sua manifestação(sugestão): ')
            ouvidor = input('Digite o nome do ouvidor: ')
            codRecSQL = "insert into manifestacoes(autor,descricao,tipo,ouvidor) values(%s,%s,'Sugestão',%s);"
            dados = [autorRec,reclamacao,ouvidor]
            manifestacoes = insertNoBancoDados(conn,codRecSQL,dados)
            print('Manifestação Salva. Obrigado. Digite 1 para visualizar todas as manifestações.')
            

    elif opcao == 4:
        print('Você entrou na sessão: EXIBIR A QUANTIDADE DE MANIFESTAÇÕES.')
        
        codQuantSQL = 'select count(*) from manifestacoes'
        manifestacoes = listarBancoDados(conn,codQuantSQL)
        print(manifestacoes[0][0],'manifestações até o momento.')
        

    elif opcao == 5:
        print('Você entrou na sessão: PESQUISAR MANIFESTAÇÃO POR CÓDIGO.')
        pesqManifestacao = int(input('Digite o código da manifestação alvo: '))
        codPesqSQL = 'select * from manifestacoes where codigo = %s'
        dados =[pesqManifestacao]
        manifestacoesDePesquisa = listarBancoDados(conn,codPesqSQL,dados)
        print('Cód. {}- {}, de: {} para: {}. Categoria: {}'.format(manifestacoesDePesquisa[0][0],manifestacoesDePesquisa[0][2],manifestacoesDePesquisa[0][1],manifestacoesDePesquisa[0][4],manifestacoesDePesquisa[0][3]))

    elif opcao == 6:
        print('Você entrou na sessão: EXCLUIR MANIFESTAÇÃO POR CÓDIGO.')
        opcaoDelete = input('Digite o código da manifestação que você deseja excluir: ')
        comandDelSQL = 'delete from manifestacoes where codigo = %s'
        dados = [opcaoDelete]
        manifestacoesDel = insertNoBancoDados(conn,comandDelSQL,dados)
        print('Manifestação com código',opcaoDelete,'foi excluída com sucesso.')
        

    elif opcao == 7:
        print('Obrigado. Volte sempre.')
        

    elif opcao !=7:
        print('Número inválido.')