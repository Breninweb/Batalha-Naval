import random

jogador = []
computador = []
tab_oculto = []

for casaJogador in range(5):
    jogador.append(["0"] * 10)

for casaComputador in range(5):
    computador.append((["0"] * 10))

for tabuleiroComputador in range(5):
    tab_oculto.append((["0"] * 10))

print("-------------------------------BATALHA NAVAL!-------------------------------")
print("---------------------------------Instruções---------------------------------")
print("1 - O jogador deve primeiramente escolher a posição que deseja colocar os seus navios. ")
print("2 - Respeitando o intervalo de 0 a 4 na linha e de 0 a 9 em coluna. ")
print("3 - Ao atacar, você precisa escolher a linha de 0 a 4 e a coluna de 0 a 9. ")
print("4 - Para vencer, você precisa destruir todos os navios do inimigo! ")
print("N - Navio | X - Acerto | O - Casa possível para escolha | - Casa vazia.")
print("---------------------------------BOA SORTE!!!--------------------------------")

def tabuleiro(jogador):

    print("  0 1 2 3 4 5 6 7 8 9")
    l = 0

    for linha in jogador:
        print("%d|%s|" % (l, " ".join(linha)))
        l += 1

def NavioJogador():
    print("Escolha a posição de seus Navios:  ")
    for i in range(5):
        linhaJogador = int(input("Por favor, escolha o número da linha: "))

        while linhaJogador not in (0, 1, 2, 3, 4):
            print("Linha inválida!")
            linhaJogador = int(input("Por favor, escolha o número da linha entre 0 e 4: "))

        colunaJogador = int(input("Agora escolha qual o número da coluna: "))

        while colunaJogador not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
            print("Coluna inválida!")
            colunaJogador = int(input("Escolha o número da coluna entre 0 e 9: "))

        jogador[linhaJogador][colunaJogador] = 'N'

        return int(linhaJogador), int(colunaJogador)

def NavioComputador(tab_oculto):
    for semRepetir in range(5):
        linha = int(random.randint(0, 4))
        coluna = int(random.randint(0, 9))

        while tab_oculto[linha][coluna] == 'N':
            linha = int(random.randint(0, 4))
            coluna = int(random.randint(0, 9))

        tab_oculto[linha][coluna] = 'N'

        return int(linha), int(coluna)

def atirarJogador ():
    linhaTiro = int(input("Qual linha você deseja atacar? "))

    while linhaTiro not in (0, 1, 2, 3, 4):
        print("Linha inválida! ")

        linhaTiro = int(input("Qual linha você deseja atacar? "))

    colunaTiro = int(input("Qual coluna você deseja atacar? "))

    while colunaTiro not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
        print("Coluna inválida! ")

        colunaTiro = int(input("Qual coluna você deseja atacar? "))

    while tab_oculto[linhaTiro][colunaTiro] == 'X' or tab_oculto[linhaTiro][colunaTiro] == 'O':

        linhaTiro = int(input("Qual linha você deseja atacar? "))
        colunaTiro = int(input("Qual coluna você deseja atacar? "))

    return int(linhaTiro), int(colunaTiro)

def atirarComputador ():
    linhaComputador = int(random.randint(0, 4))
    colunaComputador = int(random.randint(0, 9))

    while jogador[linhaComputador][colunaComputador] == 'X' or jogador[linhaComputador][colunaComputador] == 'O':
        linhaComputador = int(random.randint(0, 4))
        colunaComputador = int(random.randint(0, 9))

    return linhaComputador, colunaComputador

tabuleiro(jogador)
navios = 5

while navios != 0:
    linhaJogador, colunaJogador = NavioJogador()
    NavioComputador(tab_oculto)
    tabuleiro(jogador)
    navios -= 1

print("Vamos começar! Tente acertar o navio do computador!")

pontuacaoJogador = 0
pontuacaoComputador = 0
naviosComputador = 5
naviosJogador = 5

while True:
    print("JOGADOR")
    tabuleiro(jogador)

    print("COMPUTADOR")
    tabuleiro(computador)

    print("PONTUAÇÃO")
    print("Jogador: ", pontuacaoJogador, "Computador:" , pontuacaoComputador)
    print("Navios do Jogador:" , naviosJogador, "Navios do Computador:", naviosComputador)

    linhaTiro, colunaTiro = atirarJogador()

    #Fizemos esse teste para verificar se estava funcionando print(computador[linhaTiro][colunaTiro], " ", 'N')
                                                            #print(computador[linhaTiro][colunaTiro] == 'N')

    if tab_oculto[linhaTiro][colunaTiro] == '-':
        print("-" * 15)
        print("Você já escolheu essa posição! ")
        print("-" * 15)

    elif tab_oculto[linhaTiro][colunaTiro] == 'X':
        print("-" * 15)
        print("Você já acertou esse navio! ")
        print("-" * 15)

    elif tab_oculto[linhaTiro][colunaTiro] == 'N':
        print("-" * 15)
        print("Você derrubou um navio! ")
        print("-" * 15)

        tab_oculto[linhaTiro][colunaTiro] = 'X'
        computador[linhaTiro][colunaTiro] = 'X'

        pontuacaoJogador += 1
        naviosComputador -= 1

    else:
        print("-" * 15)
        print("Você errou! ")
        print("-" * 15)

        tab_oculto[linhaTiro][colunaTiro] = '-'
        computador[linhaTiro][colunaTiro] = '-'

    if pontuacaoJogador == 5:
        print("-" * 30)
        print("Você destruiu todos os navios inimigos!! ")
        print("-" * 30)
        break
    print("Agora é a vez do Computador.")

    linhaTiroComputador, colunaTiroComputador = atirarComputador()

    if jogador[linhaTiroComputador][colunaTiroComputador] == 'N':
        print("O Computador atirou na linha: ", linhaTiroComputador, "e na coluna: ", colunaTiroComputador)
        print("E acertou o seu navio!")
        print("-" * 15)

        jogador[linhaTiroComputador][colunaTiroComputador] = 'X'
        pontuacaoComputador += 1
        naviosJogador -= 1

    else:
        print("O Computador atirou na linha: ", linhaTiroComputador, "e na coluna: ", colunaTiroComputador)
        print("E não acertou o tiro!")
        print("-" * 15)

        jogador[linhaTiroComputador][colunaTiroComputador] = '-'

    if pontuacaoComputador == 5:
        print("-" * 30)
        print("O computador derrubou todos os seus navios!")
        print("-" * 30)
        break

print("-" * 30)
print("Batalha Naval - Feito por: Luis Felipe, Breno Webber, Leonardo Rendaki e Jonatas da Costa.")
print("     ---           Obrigado por jogar!!!      ---      ")
print("-" * 30)