def fillWorkshopsByGrade(oficinas, serie2, serie3, serie4, serie5):
    series = ((1, 3, 8, 10), (1, 2, 3, 7), (2, 3, 4, 6), (3, 4, 5, 9))

    for x in range(len(series)):
        for y in range(len(series[x])):
            nomeOficina = "#" + str(series[x][y]) + " -> " + oficinas[series[x][y]]
            if x == 0:
                serie2.append(nomeOficina)
            elif x == 1:
                serie3.append(nomeOficina)
            elif x == 2:
                serie4.append(nomeOficina)
            else:
                serie5.append(nomeOficina)


def fillFullWorkshops(array):
    for x in range(4):
        array.append([0, 0, 0, 0])


def chooseWorkShop(oficina, listaOficinas, idAluno, indexSerie, oficinaLotada):
    oficinasSeries = ((1, 3, 8, 10), (1, 2, 3, 7), (2, 3, 4, 6), (3, 4, 5, 9))
    while True:
        if len(searchStudentWorkshop(idAluno, listaOficinas)) > 2:
            print("\nNúmero limite de oficinas registradas alcançado. Você não pode mais inscrever esse aluno.")
            break
        print("\nEscolha uma oficina (de acordo com o código):")
        for x in range(len(oficina)):
            if oficinasSeries[indexSerie][x] != oficinaLotada[indexSerie][x]:
                print(oficina[x], sep="\n")

        escolha = int(input("-> "))

        oficinaInvalida = True
        for x in range(len(oficinasSeries)):
            if not oficinaInvalida:
                break
            for y in range(len(oficinasSeries[x])):
                if oficinasSeries[indexSerie][y] == escolha:
                    oficinaInvalida = False
                    break
        if oficinaInvalida:
            print("\nCódigo de oficina inválido para a série do aluno.")
            continue

        inscricaoDuplicada = False

        for aluno in listaOficinas[escolha]:
            if aluno == idAluno:
                inscricaoDuplicada = True

        if len(listaOficinas[escolha]) > 9:
            print("\nNúmero limite de alunos alcançado. Você não pode se registrar.")
            for x in range(len(oficinasSeries)):
                for y in range(len(oficinasSeries[x])):
                    if oficinasSeries[indexSerie][y] == escolha:
                        oficinaLotada[x][y] = escolha
            break
        elif inscricaoDuplicada:
            print("\nNão pode ter um aluno inscrito duas vezes em uma mesma oficina.")
        else:
            listaOficinas[escolha].append(idAluno)
            print("\nForam realizadas {} inscrições nessa oficina até o momento".format(len(listaOficinas[escolha])))
            break


def fillStudentsInfo(rmAluno, nomeAluno, finalArr, series):
    for infoAluno in finalArr:
        if infoAluno == "":
            break
        else:
            return
    for x in range(len(rmAluno)):
        finalArr.append([rmAluno[x], nomeAluno[x], printGrade(series[x])])


def sortArrayAlphabetically(finalArr):
    finalArr.sort(key=lambda index: index[1])


def printStudentsInfo(array, oficina, tituloOficina):
    print()
    for j in array:
        print("\033[1mRM: {0} - {1} - {2} \033[0m".format(str(j[0]), j[1], j[2]))
        print("\033[1mOficinas: \033[0m")
        print(printStudentWorkshop(j[0], oficina, tituloOficina))
        print()


def searchStudentInWorkshop(rm, oficina, index):
    for x in range(len(oficina)):
        if x == index:
            for y in range(len(oficina[x])):
                if oficina[index][y] == rm:
                    return True
    return False


def printStudentsInfoByWorkshop(array, oficina, tituloOficina):
    nomeOficinas = []  # Oficinas por extenso
    rms = []  # RMs dos alunos cadastrados
    idxOficina = []  # Indexes das oficinas
    alunos = []  # RMs organizados pelo index das oficinas (nested)

    # Enchendo as listas:
    for k in array:
        rms.append(k[0])
    for rm in rms:
        nomeOficinas.append(searchStudentWorkshop(rm, oficina))
    for x in nomeOficinas:
        for y in x:
            idxOficina.append(y)

    idxOficina = list(dict.fromkeys(idxOficina))  # Removendo oficinas repetidas
    nomeOficinas.clear()

    for o in idxOficina:
        nomeOficinas.append(printWorkshop(o, tituloOficina))  # Colocando as oficinas por extenso

    # Ordenando oficinas alfabeticamente:
    zipped_lists = zip(nomeOficinas, idxOficina)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    nomeOficinas, idxOficina = [list(tupla) for tupla in tuples]

    for x in idxOficina:  # Relacionando RMs com o index da oficina (alunos[])
        rmPack = [[]]
        for y in range(len(rms)):
            if searchStudentInWorkshop(rms[y], oficina, x):
                rmPack[0].append(rms[y])
            if y == len(rms) - 1:
                alunos.append(rmPack[0])

    for x in range(len(nomeOficinas)):
        total = 0
        print("> " + nomeOficinas[x])
        for y in array:
            for a in range(len(alunos[x])):  # Buscando info dos RMs (nome, serie)
                if y[0] == alunos[x][a]:
                    total += 1
                    print("\033[1m RM: {0} - {1} - {2} \033[0m".format(str(y[0]), y[1], y[2]))
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


def printWorkshop(w, nomeOficina):
    if w < 1 or w > 10:
        return
    else:
        return nomeOficina[w]


def printStudentWorkshop(idAluno, oficina, tituloOficina):
    workshops = []
    ids = searchStudentWorkshop(idAluno, oficina)
    for x in range(len(ids)):
        workshops.append(printWorkshop(ids[x], tituloOficina))

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


def registerStudent(listaAlunos, listaPorSerie, blockWks):
    while True:
        rmCadastro = int(input("\nInsira o RM: "))
        if rmCadastro == 0:
            break
        rmDuplicado = False
        for x in range(len(listaAlunos)):
            if rmCadastro == listaAlunos[x]:
                rmDuplicado = True
                break
        if rmDuplicado:
            print("\nRM já existe no sistema!")
            continue

        listaAlunos.append(rmCadastro)

        nomeCadastro = input("\nInsira o nome do aluno: ")
        names.append(nomeCadastro)

        serieCadastro = int(input("\n\033[1mEscolha a série do aluno:\033[0m\nDigite (2) para 2º Série\n(3) para 3º "
                                  "Série\n(4) para 4º Série\n(5) para 5º Série\n--> "))
        while serieCadastro < 2 or serieCadastro > 5:
            print("\nSérie inválida! Apenas séries iniciais (1º a 5º)")
            serieCadastro = int(input("\n\033[1mEscolha a série do aluno:\033[0m\nDigite (2) para 2º Série\n"
                                      "(3) para 3º Série\n(4) para 4º Série\n(5) para 5º Série\n--> "))
        listaPorSerie.append(serieCadastro)

    showMenu(blockWks)


def showMenu(blockWks):
    print("\n-- MENU --\nEscolha uma opção (1-4):")
    if not blockWks:
        print("1 - Cadastrar Alunos")
    print("2 - Fazer Inscrições\n3 - Listar Inscrições\n4 - Sair")


# Listas
idStudent = []
names = []
idSeries = []

# Oficinas
workshopRegistrationArray = [[], [], [], [], [], [], [], [], [], [], []]

workshopsTitle = ("",
                  "Criar e contar histórias (2ª feira - Matutino)",
                  "Teatro: Luz, Câmera e Ação (3ª feira - Matutino)",
                  "A língua de sinais (4ª feira - Matutino)",
                  "Expressão Artística (5ª feira - Matutino)",
                  "Soletrando (6ª feira - Matutino)",
                  "Leitura dramática (2ª feira - Vespertino)",
                  "O corpo fala (3ª feira - Vespertino)",
                  "O mundo da imaginação (4ª feira - Vespertino)",
                  "Leitura dinâmica (5ª feira - Vespertino)",
                  "Criando e recriando com emojis (6ª feira - Vespertino)")

workshopsByGrade = [[], [], [], []]
fullWorkshops = []
studentsInfo = []

# Main Class:
fillWorkshopsByGrade(workshopsTitle, workshopsByGrade[0], workshopsByGrade[1], workshopsByGrade[2], workshopsByGrade[3])
fillFullWorkshops(fullWorkshops)
block_option = False
print("\nBem-vindo(a) ao Colégio Nova Esperança - Evento Literário")
showMenu(block_option)
option = int(input("--> "))
while True:
    if option == 1 and not block_option:
        block_option = True
        registerStudent(idStudent, idSeries, block_option)
        option = int(input("--> "))

    if option == 2:
        rmInscricao = int(input("\nInsira o RM do aluno: "))
        for i in range(len(idStudent)):
            if idStudent[i] == rmInscricao:
                if idSeries[i] == 2:
                    chooseWorkShop(workshopsByGrade[0], workshopRegistrationArray, rmInscricao, 0, fullWorkshops)
                elif idSeries[i] == 3:
                    chooseWorkShop(workshopsByGrade[1], workshopRegistrationArray, rmInscricao, 1, fullWorkshops)
                elif idSeries[i] == 4:
                    chooseWorkShop(workshopsByGrade[2], workshopRegistrationArray, rmInscricao, 2, fullWorkshops)
                elif idSeries[i] == 5:
                    chooseWorkShop(workshopsByGrade[3], workshopRegistrationArray, rmInscricao, 3, fullWorkshops)

            elif rmInscricao == 0:
                break

            elif rmInscricao not in idStudent:
                print("\nAluno não cadastrado. Favor procurar a coordenação do Fundamental I")
                break

    if option == 3:
        fillStudentsInfo(idStudent, names, studentsInfo, idSeries)
        sortArrayAlphabetically(studentsInfo)
        menuList = int(input("\nListar Inscrições (em ordem alfabética)\n1 - Listar por Aluno\n2 - Listar por "
                             "Oficina\n--> "))
        if menuList == 1:
            print("\n***** Alunos inscritos – Ordem: Alfabética (nome) *****")
            printStudentsInfo(studentsInfo, workshopRegistrationArray, workshopsTitle)
        if menuList == 2:
            print("\n***** Alunos inscritos – Ordem: Alfabética (Oficinas) *****")
            print("\033[1mOficinas: \033[0m")
            printStudentsInfoByWorkshop(studentsInfo, workshopRegistrationArray, workshopsTitle)

    if option == 4:
        break

    showMenu(block_option)
    option = int(input("--> "))
