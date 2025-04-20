from operacoesbd import *
'''
1)Listagem de manifestações
2) Listagem de manifestações por tipo
3) Criar uma manifestação
4) Exibir quantidade de manifestações
5) Pesquisar uma manifestação por código
6) Excluir uma manifestação pelo código
7) Sair do sistema
'''


conn = criarConexao("127.0.0.1","root","lalaeluan1234","ouvidoriacompleta")


#Função para obter a opção do User
def opcaoUser():
    while True:
        try:
            print("Ouvidoria Lubrias")
            print("1)Listagem de manifestações"
                    "2 - Listagem de manifestações por tipo"
                    "3 - Criar uma manifestação"
                    "4 - Exibir quantidade de manifestações"
                    "5 - Pesquisar uma manifestação por código"
                    "6 - Excluir uma manifestação pelo código"
                    "7 - Sair do sistema")
            opcao = int(input("Digite a sua opção: "))
        except ValueError:
            print("Diagramação inválida. Digite um número de 1 a 7.\n")

#Manifestações totais       
def manifestacaoTotal(conn):
    consultaListaManifestacoes = "SELECT * FROM manifestacoes"
    listaManifestacoes = listarBancoDados(conn,consultaListaManifestacoes)

    if len(listaManifestacoes) == 0:
        print("Nenhuma manifestação adicionada até o momento.")
    else:
        for item in listaManifestacoes:
            print(f"Manifestação: {item[0]}:\n"
                f"- Descrição: {item[2]}\n"
                f"- Tipo: {item[3]}\n")

#Manifestação por Tipo
def manifestacaoPorTipo(conn):
    tipoDoUser = int(input("Digite o tipo de manifestação que você deseja: 1) Reclamação. 2) Elogios. 3) Melhorias"))
    consultaManifestacaoPorTipo = "SELECT * FROM manifestacoes where tipo = %s"
    dados = [tipoDoUser]
    listaManifestacoesPorTipo = listarBancoDados(conn,consultaManifestacaoPorTipo,dados)

#User cria nova manifestação:
def criarNovaManifestacao(conn):
    while True:
        try:
            autor = input("Digite o seu nome: ")
            descricao = input("Digite a descrição: ")
            tipo = int(input("Digite o número que corresponde ao tipo da sua manifestação.\n"
                             "(1 - Reclamação.\n 2 - Elogios.\n 3- Melhorias.)\n"
                             "Digite sua escolha: "))

        except ValueError:
            print("Valores inválidos. Verifique o erro que você cometeu e tente novamente.")

#Exibir quantidade de manifestações
def quantidadeManifestacoes(conn):
        consultaQuantidade = "select count(*) from manifestacoes"
        quantidadeManifestacao = listarBancoDados(conn,consultaQuantidade)

        if len(quantidadeManifestacao) == 0:
                print("Nenhuma manifestação adicionada até o momento.")
        else:
            for item in quantidadeManifestacao:
                print("-", item)

#Pesquisa de manifestação por código
def pesquisaPorCodigo(conn):
    while True:
        try:
            codigoDePesquisa = int(input("Digite o código que responde a manifestação que você deseja pesquisar"))
            consultaPesquisaCodigo = "select * from manifestacoes where codigo = %s"
            dados = [codigoDePesquisa]
            codigoPesquisado = listarBancoDados(conn,consultaPesquisaCodigo,dados)

            if len(codigoPesquisado):
                print("Nenhuma manifestação encontrada com o código informado.")
            else:
                for item in codigoPesquisado:
                    print("-",item)
        except ValueError:
            print("Código inválido. Verifique seu erro e tente novamente.")

#Exclusão de manifestação por código
def excluirManifestacao(conn):
    while True:
        try:
            codigoDeExclusao = int(input("Digite o código da manifestação que você deseja excluir: "))
            consultaExcluir = "delete from manifestacoes where codigo = %s"
            dados = [codigoDeExclusao]
            manifestacaoExcluida = excluirBancoDados(conn,consultaExcluir,dados)

            if len(manifestacaoExcluida) == 0:
                print("Nenhuma manifestação encontrada.")
            else:
                print(f"Manifestação {codigoDeExclusao} excluída com sucesso!")

        except ValueError:
            print("Digitação inválida. Verifique o erro que você cometeu e tente novamente.")

                             
encerrarConexao(conn)