# Listas
rmAlunos = []
nomes = []
rmSeries = []
menu_l = []
blank = []
# Oficinas manhã
oficina1 = []
oficina2 = []
oficina3 = []
oficina4 = []
oficina5 = []
# Oficinas tarde
oficina6 = []
oficina7 = []
oficina8 = []
oficina9 = []
# Listas
oficinasGeral = [
    blank, oficina1, oficina2, oficina3, oficina4, oficina5, oficina6, oficina7, oficina8, oficina9
]
studentsInfo = []

oficinas2Serie = ("#1 -> Criar e contar histórias (Segunda-feira - Manhã)",
                  "#3 -> A língua de sinais (Quarta-feira - Manhã)",
                  "#8 -> O mundo da imaginação (Quarta-feira - Tarde)",
                  "#9 -> Criando e recriando com emojis (Sexta-feira - Tarde)")

oficinas3Serie = ("#1 -> Criar e contar histórias (Segunda-feira - Manhã)",
                  "#2 -> Teatro: Luz, Câmera e Ação (Terça-feira - Manhã)",
                  "#3 -> A língua de sinais (Quarta-feira - Manhã)",
                  "#7 -> O corpo fala (Terça-feira - Tarde)")

oficinas4Serie = ("#2 -> Teatro: Luz, Câmera e Ação (Terça-feira - Manhã)",
                  "#3 -> A língua de sinais (Quarta-feira - Manhã)",
                  "#4 -> Expressão Artística (Quinta-feira - Manhã)",
                  "#6 -> Leitura dinâmica (Segunda-feira/Quinta-feira - Tarde)")

oficinas5Serie = ("#3 -> A língua de sinais (Quarta-feira - Manhã)",
                  "#4 -> Expressão Artística (Quinta-feira - Manhã)",
                  "#5 -> Soletrando (Sexta-feira - Manhã)",
                  "#6 -> Leitura dinâmica (Segunda-feira/Quinta-feira - Tarde)")


def indexWorkshop(escolha, oficina):
    oficinas = ((), (), (1, 3, 8, 9), (1, 2, 3, 7), (2, 3, 4, 6), (3, 4, 5, 6))
    return oficinas[oficina].index(escolha)


def showMenu():
    print("\n-- MENU --\nEscolha uma opção (1-4):\n1 - Cadastrar Alunos\n"
          "2 - Fazer Inscrições\n3 - Listar Inscrições\n4 - Sair")


def chooseWorkShop(oficina, listaOficinas, idAluno):
    oficinas_banidas = [0] * len(oficina)
    while True:
        print("Escolha uma oficina (de acordo com o código):")
        for x in range(len(oficina)):
            if oficina[x] != oficinas_banidas[x]:
                print(oficina[x], sep="\n")

        escolha = int(input("-> "))

        validar_inscricao = True

        for aluno in listaOficinas[escolha]:
            if aluno == idAluno:
                validar_inscricao = False

        if len(listaOficinas[escolha]) > 10:
            print("Número limite de alunos alcançado. Você não pode se registrar.\n")
            oficinas_banidas[indexWorkshop(escolha, listaOficinas)] = escolha
        elif not validar_inscricao:
            print("Não pode ter um aluno inscrito duas vezes em uma mesma oficina. Tente Novamente\n")
        else:
            listaOficinas[escolha].append(idAluno)
            print("Foram realizadas {} inscrições nessa oficina até o momento\n".format(len(listaOficinas[escolha])))
            break


def fillStudentsInfo(rmAluno, nomeAluno, finalArr, series):
    for infoAluno in finalArr:
        if infoAluno == "":
            break
        else:
            return
    for x in range(len(rmAluno)):
        finalArr.append([rmAluno[x], nomeAluno[x], printGrade(series[x])])


def nameStudent(nomeAluno):
    return str.lower(nomeAluno)


def organizeArrayAlphabetically(finalArr):
    finalArr.sort(key=lambda pair: pair[1])


def printStudentsInfo(array, oficina):
    print()
    for j in array:
        print("\033[1m" + "RM: " + str(j[0]) + " - " + j[1] + " - " + j[2] + "\033[0m")
        print("\033[1m" + "Oficinas:" + "\033[0m")
        print(printStudentWorkshop(j[0], oficina))
        print()
    print()


def searchStudentInWorkshop(rm, oficina, index):
    for x in range(len(oficina)):
        if x == index:
            for y in range(len(oficina[x])):
                if oficina[index][y] == rm:
                    return True
    return False


def printStudentsInfoByWorkshop(array, oficina):
    workshops = []  # Oficinas por extenso
    rms = []    # RMs dos alunos cadastrados
    idxOficina = []     # Indexes das oficinas
    alunos = []     # RMs organizados pelo index das oficinas (nested)

    # Enchendo as listas:
    for k in array:
        rms.append(k[0])
    for rm in rms:
        workshops.append(searchStudentWorkshop(rm, oficina))
    for x in workshops:
        for y in x:
            idxOficina.append(y)

    idxOficina = list(dict.fromkeys(idxOficina))    # Removendo oficinas repetidas
    workshops.clear()

    for o in idxOficina:
        workshops.append(printWorkshop(o))  # Colocando as oficinas por extenso

    for x in idxOficina:    # Relacionando RMs com os index da oficina (alunos[])
        rmPack = [[]]
        for y in range(len(rms)):
            if searchStudentInWorkshop(rms[y], oficina, x):
                rmPack[0].append(rms[y])
            if y == len(rms) - 1:
                alunos.append(rmPack[0])

    for x in range(len(workshops)):
        total = 0
        print(workshops[x])
        for y in array:
            for a in range(len(alunos[x])):     # Buscando info dos RMs (nome, serie)
                if y[0] == alunos[x][a]:
                    total += 1
                    print("\033[1m" + "RM: " + str(y[0]) + " - " + y[1] + " - " + y[2] + "\033[0m")
                    continue
        print("Total: {} aluno".format(total)) if total <= 1 else print("Total: {} alunos".format(total))
        print("-----------------------------------------------------------------------")


def searchStudentWorkshop(idAluno, oficina):
    indexOficinas = []
    counter = 0
    while counter < len(oficina):
        for g in range(len(oficina[counter])):
            if oficina[counter][g] == idAluno:
                indexOficinas.append(counter)
        counter += 1

    return indexOficinas


def printWorkshop(w):
    if w == 1:
        return "Criar e contar histórias (2ª feira - Manhã)"
    elif w == 2:
        return "Teatro: Luz, Câmera e Ação (3ª feira - Manhã)"
    elif w == 3:
        return "A língua de sinais (4ª feira - Manhã)"
    elif w == 4:
        return "Expressão Artística (5ª feira - Manhã)"
    elif w == 5:
        return "Soletrando (6ª feira - Manhã)"
    elif w == 6:
        return "Leitura dinâmica (2ª feira / 5ª feira - Tarde)"
    elif w == 7:
        return "O corpo fala (3ª feira - Tarde)"
    elif w == 8:
        return "O mundo da imaginação (4ª feira - Tarde)"
    elif w == 9:
        return "Criando e recriando com emojis (6ª feira - Tarde)"
    else:
        return


def printStudentWorkshop(idAluno, oficina):
    workshops = []
    ids = searchStudentWorkshop(idAluno, oficina)
    for x in range(len(ids)):
        workshops.append(printWorkshop(ids[x]))

    return '\n'.join(workshops)


def printGrade(series):
    if series == 2:
        return "2ª. série"
    elif series == 3:
        return "3ª. série"
    elif series == 4:
        return "4ª. série"
    else:
        return "5ª. série"


# Main Class:
showMenu()
option = int(input("--> "))
while True:
    if option == 1 and 1 not in menu_l:
        menu_l.append(1)
        while True:
            rmCadastro = int(input("\nInsira o RM: "))
            if rmCadastro == 0:
                break
            rmDuplicado = False
            for i in range(len(rmAlunos)):
                if rmCadastro == rmAlunos[i]:
                    print("\nRM já existe no sistema!")
                    rmDuplicado = True
                    break
            if rmDuplicado:
                continue

            rmAlunos.append(rmCadastro)

            nomeCadastro = input("\nInsira o nome do aluno: ")
            nomes.append(nomeCadastro)

            serieCadastro = int(input("\nDigite (2) para 2º Série\n(3) para 3º Série\n(4) para 4º Série\n(5) para 5º "
                                      "Série\n--> "))
            while serieCadastro < 2 or serieCadastro > 5:
                print("Série inválida! Apenas séries inicias (1º a 5º)")
                serieCadastro = int(input("\nDigite (2) para 2º Série\n(3) para 3º Série\n(4) para 4º Série\n(5) para "
                                          "5º Série\n--> "))
            rmSeries.append(serieCadastro)

        showMenu()
        option = int(input("--> "))

    if option == 2:
        rmInscricao = int(input("Insira o RM do aluno: "))
        for i in range(len(rmAlunos)):
            if rmAlunos[i] == rmInscricao:
                if rmSeries[i] == 2:
                    chooseWorkShop(oficinas2Serie, oficinasGeral, rmInscricao)

                elif rmSeries[i] == 3:
                    chooseWorkShop(oficinas3Serie, oficinasGeral, rmInscricao)

                elif rmSeries[i] == 4:
                    chooseWorkShop(oficinas4Serie, oficinasGeral, rmInscricao)

                elif rmSeries[i] == 5:
                    chooseWorkShop(oficinas5Serie, oficinasGeral, rmInscricao)

            elif rmInscricao == 0:
                break

            elif rmInscricao not in rmAlunos:
                print("Aluno não cadastrado. Favor procurar a coordenação do Fundamental I")
                break

    if option == 3:
        fillStudentsInfo(rmAlunos, nomes, studentsInfo, rmSeries)
        organizeArrayAlphabetically(studentsInfo)
        menuLista = int(input("Listar Inscrições\n1 - Listar por Aluno\n2 - Listar por Oficina\n--> "))
        if menuLista == 1:
            print("\n***** Alunos inscritos – Ordem: Alfabética (nome) *****")
            printStudentsInfo(studentsInfo, oficinasGeral)
        if menuLista == 2:
            print("\n***** Alunos inscritos – Ordem: Alfabética (Oficinas) *****")
            print("\033[1m" + "Oficinas:" + "\033[0m")
            printStudentsInfoByWorkshop(studentsInfo, oficinasGeral)

    if option == 4:
        break

    showMenu()
    option = int(input("--> "))
