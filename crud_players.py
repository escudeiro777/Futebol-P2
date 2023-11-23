import sqlite3

conn = sqlite3.connect("players.db")

while True:
    print("\nSejam bem vindos ao sistema de gerenciamento de jogadores do Corinthians\n\nDigite 1 para listar todos os jogadores\nDigite 2 para buscar um jogador específico\nDigite 3 para cadastrar um jogador\nDigite 4 para atualizar informações de um jogador\nDigite 5 para excluir um jogador\n")

    options = input("Selecione a opção desejada: ")

    if options == '1':
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players")
        resultados = cursor.fetchall()

        for jogador in resultados:
            print(jogador)

    elif options == '2':
        vcodigo = input("Digite o número da camisa do jogador que deseja buscar: ")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players WHERE idJogador =" + vcodigo)
        resultados = cursor.fetchone()

        if resultados:
            for jogador in resultados:
                print(jogador)
        else:
            print("Jogador não encontrado.")

    elif options == '3':
        while True:
            vcodigo = input("Digite o número da camisa do jogador(a): ")
            vjogador = input("Digite o nome do jogador(a): ")
            vposicao = input("Digite a posição do jogador(a): ")
            vidade = input("Digite a idade do jogador(a): ")
            vtitulo = input("Digite a quantidade de títulos: ")

            if vcodigo.isdigit() and vidade.isdigit() and vtitulo.isdigit():
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM players WHERE idJogador = ?", (vcodigo,))
                resultados = cursor.fetchone()

                if not resultados:
                    conn.execute("INSERT INTO players (idJogador, nomeJogador, posicaoJogador, idadeJogador, titulosJogador) VALUES (?,?,?,?,?)", (vcodigo, vjogador, vposicao, vidade, vtitulo))
                    conn.commit()
                    print("Jogador cadastrado com sucesso!")
                else:
                    print("Já existe um jogador com esse número de camisa.")
            else:
                print("Por favor, preencha corretamente todas as informações do jogador.")

            continuar = input("Deseja continuar cadastrando jogadores? Digite Sim ou Não: ")
            if continuar.lower() != "sim":
                break

    elif options == '4':
        while True:
            print("Atualização de jogador")
            options_update = input("Digite 1 para alterar o número da camisa.\nDigite 2 para alterar o nome do jogador.\nDigite 3 para alterar a posição do jogador\nDigite 4 para alterar a idade do jogador\nDigite 5 para alterar a quantidade de títulos do jogador\n")
            
            vcodigo = input("Digite o número da camisa do jogador que deseja atualizar: ")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM players WHERE idJogador = ?", (vcodigo,))
            resultados = cursor.fetchone()

            if resultados:
                if options_update == '1':
                    novo_numero = input("Qual o novo número da camisa?")
                    if novo_numero.isdigit():
                        cursor.execute("UPDATE players SET idJogador = ? WHERE idJogador = ?", (novo_numero, vcodigo))
                        conn.commit()
                        print("Número da camisa atualizado com sucesso!")
                    else:
                        print("Por favor, insira um valor numérico para o número da camisa.")

                elif options_update == '2':
                    novo_nome = input("Digite o novo nome do jogador: ")
                    cursor.execute("UPDATE players SET nomeJogador = ? WHERE idJogador = ?", (novo_nome, vcodigo))
                    conn.commit()
                    print("Nome do jogador atualizado com sucesso!")

                elif options_update == '3':
                    nova_posicao = input("Digite a nova posição do jogador: ")
                    cursor.execute("UPDATE players SET posicaoJogador = ? WHERE idJogador = ?", (nova_posicao, vcodigo))
                    conn.commit()
                    print("Posição do jogador atualizada com sucesso!")

                elif options_update == '4':
                    nova_idade = input("Digite a nova idade do jogador: ")
                    if nova_idade.isdigit():
                        cursor.execute("UPDATE players SET idadeJogador = ? WHERE idJogador = ?", (nova_idade, vcodigo))
                        conn.commit()
                        print("Idade do jogador atualizada com sucesso!")
                    else:
                        print("Por favor, insira um valor numérico para a idade.")

                elif options_update == '5':
                    novo_titulo = input("Digite a nova quantidade de títulos: ")
                    if novo_titulo.isdigit():
                        cursor.execute("UPDATE players SET titulosJogador = ? WHERE idJogador = ?", (novo_titulo, vcodigo))
                        conn.commit()
                        print("Quantidade de títulos do jogador atualizada com sucesso!")
                    else:
                        print("Por favor, insira um valor numérico para a quantidade de títulos.")

            else:
                print("Jogador não encontrado.")

            continuar = input("Deseja continuar atualizando dados? Digite Sim ou Não: ")
            if continuar.lower() != "sim":
                break

    elif options == '5':
        print("Deleção de jogador")
        vcodigo = input("Digite o número da camisa do jogador que deseja deletar: ")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players WHERE idJogador = ?", (vcodigo,))
        resultados = cursor.fetchone()

        if resultados:
            confirmacao = input(f"Você tem certeza que deseja deletar o jogador com o número da camisa {vcodigo}? Digite 'Sim' para confirmar: ")
            if confirmacao.lower() == 'sim':
                cursor.execute("DELETE FROM players WHERE idJogador = ?", (vcodigo,))
                conn.commit()
                print("Jogador deletado com sucesso!")
            else:
                print("Deleção cancelada.")
        else:
            print("Jogador não encontrado.")

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

    continuar = input("Deseja continuar mexendo no sistema? Digite 'Sim' se sim, 'Não' se não: ")
    if continuar.lower() != 'sim':
        break

conn.close()
