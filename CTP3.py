# Listas
rmAlunos = []
rmSeries = []
menu_l = []

# Oficinas manhã
oficina1 = oficina2 = oficina3 = oficina4 = oficina5 = []
# Oficinas tarde
oficina6 = oficina7 = oficina8 = oficina9 = []
# Listas
oficinasGeral = [0, oficina1, oficina2, oficina3, oficina4, oficina5, oficina6, oficina7, oficina8, oficina9]

oficinas2Serie = ("1 -> Criar e contar histórias (Segunda-feira - Manhã)",
                  "3 -> A língua de sinais (Quarta-feira - Manhã)",
                  "8 -> O mundo da imaginação (Quarta-feira - Tarde)",
                  "9 -> Criando e recriando com emojis (Sexta-feira - Tarde)")

oficinas3Serie = ("1 -> Criar e contar histórias (Segunda-feira - Manhã)",
                  "2 -> Teatro: Luz, Câmera e Ação (Terça-feira - Manhã)",
                  "3 -> A língua de sinais (Quarta-feira - Manhã)",
                  "7 -> O corpo fala (Terça-feira - Tarde)")

oficinas4Serie = ("2 -> Teatro: Luz, Câmera e Ação (Terça-feira - Manhã)",
                  "3 -> A língua de sinais (Quarta-feira - Manhã)",
                  "4 -> Expressão Artística (Quinta-feira - Manhã)",
                  "6 -> Leitura dinâmica (Segunda-feira/Quinta-feira - Tarde)")

oficinas5Serie = ("3 -> A língua de sinais (Quarta-feira - Manhã)",
                  "4 -> Expressão Artística (Quinta-feira - Manhã)",
                  "5 - > Soletrando (Sexta-feira - Manhã)",
                  "6 -> Leitura dinâmica (Segunda-feira/Quinta-feira - Tarde)")


def showMenu():
    print("-- MENU --\nEscolha uma opção (1-4):\n1 - Cadastrar Alunos\n"
          "2 - Fazer Inscrições\n3 - Listar Inscrições\n4 - Sair")


def escolherOficina(oficina, listaOficinas, idAluno):
    print("Escolha uma oficina (de acordo com o código):")
    print(*oficina, sep="\n")
    escolha = int(input("-> "))
    if len(listaOficinas[escolha]) > 10:
        raise Exception("Número limite de alunos alcançado. Você não pode se registrar.")
    else:
        listaOficinas[escolha].append(idAluno)
        print("Foram realizadas {} inscrições até o momento".format(len(listaOficinas[escolha])))


showMenu()
option = int(input("--> "))
while True:
    if option == 1 and 1 not in menu_l:
        menu_l.append(1)
        rmCadastro = int(input("Insira o RM: "))
        while rmCadastro != 0:
            for i in range(len(rmAlunos)):
                if rmCadastro == rmAlunos[i]:
                    print("RM já existe no sistema!")
            rmAlunos.append(rmCadastro)

            nomeCadastro = input("Insira o nome do aluno: ")

            serieCadastro = int(input("Digite (2) para 2º Série\n(3) para 3º Série\n(4) para 4º Série\n(5) para 5º "
                                      "Série\n--> "))
            while serieCadastro < 2 or serieCadastro > 5:
                print("Série inválida! Apenas séries inicias (1º a 5º)")
                serieCadastro = int(input("Digite (2) para 2º Série\n(3) para 3º Série\n(4) para 4º Série\n(5) para 5º "
                                          "Série\n--> "))
            rmSeries.append(serieCadastro)
            rmCadastro = int(input("Insira o RM: "))

        showMenu()
        option = int(input("--> "))

    if option == 2:
        rmInscricao = int(input("Insira o RM do aluno: "))
        for i in range(len(rmAlunos)):
            if rmAlunos[i] == rmInscricao:
                if rmSeries[i] == 2:
                    escolherOficina(oficinas2Serie, oficinasGeral, rmInscricao)
                    for esc in range(3):
                        print("Deseja escolher mais uma oficina? (S ou N)")
                        continuar = input("--> ")
                        if continuar == "S":
                            escolherOficina(oficinas2Serie, oficinasGeral, rmInscricao)
                        elif continuar == "N":
                            break

                elif rmSeries[i] == 3:
                    escolherOficina(oficinas3Serie, oficinasGeral, rmInscricao)
                    for esc in range(3):
                        print("Deseja escolher mais uma oficina? (S ou N)")
                        continuar = input("--> ")
                        if continuar == "S":
                            escolherOficina(oficinas3Serie, oficinasGeral, rmInscricao)
                        elif continuar == "N":
                            break

                elif rmSeries[i] == 4:
                    escolherOficina(oficinas4Serie, oficinasGeral, rmInscricao)
                    for esc in range(3):
                        print("Deseja escolher mais uma oficina? (S ou N)")
                        continuar = input("--> ")
                        if continuar == "S":
                            escolherOficina(oficinas4Serie, oficinasGeral, rmInscricao)
                        elif continuar == "N":
                            break

                elif rmSeries[i] == 5:
                    escolherOficina(oficinas5Serie, oficinasGeral, rmInscricao)
                    for esc in range(3):
                        print("Deseja escolher mais uma oficina? (S ou N)")
                        continuar = input("--> ")
                        if continuar == "S":
                            escolherOficina(oficinas5Serie, oficinasGeral, rmInscricao)
                        elif continuar == "N":
                            break

            elif rmInscricao == 0:
                break

            elif rmInscricao not in rmAlunos:
                print("Aluno não cadastrado. Favor procurar a coordenação do Fundamental I")

    if option == 4:
        break

    showMenu()
    option = int(input("--> "))
