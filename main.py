from random import randint
from time import sleep

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
player = '\033[1:32mO\033[m'
com = '\033[1:31mX\033[m'
gameOver = False

def ifAvailable(pos, play):  #Verifica se é possível fazer a jogada desejada.
    if pos < 1 or pos > 9:
        if play == player:
            print('Posição inválida! Escolha uma posição de 1 a 9.')
            newPos = int(input('Qual posição deseja jogar? '))
            print('')
            ifAvailable(newPos, player)
        else:
            newPos = randint(1, 9)
            ifAvailable(newPos, com)
    else:
        if pos == 1:
            if board[0][0] == player or board[0][0] == com:
                if play == player:
                    print('Posição já preenchida! Escolha outra posição.')
                    newPos = int(input('Qual posição deseja jogar? '))
                    print('')
                    ifAvailable(newPos, player)
                else:
                    newPos = randint(1, 9)
                    ifAvailable(newPos, com)
            else:
                board[0][0] = play
        if pos == 2:
            if board[0][1] == player or board[0][1] == com:
                if play == player:
                    print('Posição já preenchida! Escolha outra posição.')
                    newPos = int(input('Qual posição deseja jogar? '))
                    print('')
                    ifAvailable(newPos, player)
                else:
                    newPos = randint(1, 9)
                    ifAvailable(newPos, com)
            else:
                board[0][1] = play
        if pos == 3:
            if board[0][2] == player or board[0][2] == com:
                if play == player:
                    print('Posição já preenchida! Escolha outra posição.')
                    newPos = int(input('Qual posição deseja jogar? '))
                    print('')
                    ifAvailable(newPos, player)
                else:
                    newPos = randint(1, 9)
                    ifAvailable(newPos, com)
            else:
                board[0][2] = play
        if pos == 4:
            if board[1][0] == player or board[1][0] == com:
                if play == player:
                    print('Posição já preenchida! Escolha outra posição.')
                    newPos = int(input('Qual posição deseja jogar? '))
                    print('')
                    ifAvailable(newPos, player)
                else:
                    newPos = randint(1, 9)
                    ifAvailable(newPos, com)
            else:
                board[1][0] = play
        if pos == 5:
            if board[1][1] == player or board[1][1] == com:
                if play == player:
                    print('Posição já preenchida! Escolha outra posição.')
                    newPos = int(input('Qual posição deseja jogar? '))
                    print('')
                    ifAvailable(newPos, player)
                else:
                    newPos = randint(1, 9)
                    ifAvailable(newPos, com)
            else:
                board[1][1] = play
        if pos == 6:
            if board[1][2] == player or board[1][2] == com:
                if play == player:
                    print('Posição já preenchida! Escolha outra posição.')
                    newPos = int(input('Qual posição deseja jogar? '))
                    print('')
                    ifAvailable(newPos, player)
                else:
                    newPos = randint(1, 9)
                    ifAvailable(newPos, com)
            else:
                board[1][2] = play
        if pos == 7:
            if board[2][0] == player or board[2][0] == com:
                if play == player:
                    print('Posição já preenchida! Escolha outra posição.')
                    newPos = int(input('Qual posição deseja jogar? '))
                    print('')
                    ifAvailable(newPos, player)
                else:
                    newPos = randint(1, 9)
                    ifAvailable(newPos, com)
            else:
                board[2][0] = play
        if pos == 8:
            if board[2][1] == player or board[2][1] == com:
                if play == player:
                    print('Posição já preenchida! Escolha outra posição.')
                    newPos = int(input('Qual posição deseja jogar? '))
                    print('')
                    ifAvailable(newPos, player)
                else:
                    newPos = randint(1, 9)
                    ifAvailable(newPos, com)
            else:
                board[2][1] = play
        if pos == 9:
            if board[2][2] == player or board[2][2] == com:
                if play == player:
                    print('Posição já preenchida! Escolha outra posição.')
                    newPos = int(input('Qual posição deseja jogar? '))
                    print('')
                    ifAvailable(newPos, player)
                else:
                    newPos = randint(1, 9)
                    ifAvailable(newPos, com)
            else:
                board[2][2] = play

def printBoard(): # Exibe o tabuleiro.
    line1 = '+-------+-------+-------+'
    line2 = '|       |       |       |'
    for i in range(3):
        print(line1)
        print(line2)
        print('|   {}   |   {}   |   {}   |'.format(board[i][0], board[i][1], board[i][2]))
        print(line2)
    print(line1)
    print('=' * 25)

def comTurn(): # Realiza a jogada do computador.
    print('Vez do computador.')
    sleep(2)
    comPos = randint(1, 9)
    ifAvailable(comPos, com)
    printBoard()
    print('')
    endGame()

def playerTurn():  # Realiza a jogada do player.
    print('Sua vez!')
    myTurn = int(input('Qual posição deseja jogar? '))
    print('')
    ifAvailable(myTurn, player)
    printBoard()
    print('')
    endGame()

def endGame(): # Define as condições para fim de jogo.
    p1 = board[0][0]
    p2 = board[0][1]
    p3 = board[0][2]
    p4 = board[1][0]
    p5 = board[1][1]
    p6 = board[1][2]
    p7 = board[2][0]
    p8 = board[2][1]
    p9 = board[2][2]
    global gameOver
    if p1 == p2 and p2 == p3 and p3 == player or \
    p4 == p5 and p5 == p6 and p6 == player or \
    p7 == p8 and p8 == p9 and p9 == player or \
    p1 == p4 and p4 == p7 and p7 == player or \
    p2 == p5 and p5 == p8 and p8 == player or \
    p3 == p6 and p6 == p9 and p9 == player or \
    p1 == p5 and p5 == p9 and p9 == player or \
    p3 == p5 and p5 == p7 and p7 == player:
        print('VITÓRIA!!!\nPARABÉNS!!! Você ganhou.')
        gameOver = True
        return gameOver
    elif p1 == p2 and p2 == p3 and p3 == com or \
    p4 == p5 and p5 == p6 and p6 == com or \
    p7 == p8 and p8 == p9 and p9 == com or \
    p1 == p4 and p4 == p7 and p7 == com or \
    p2 == p5 and p5 == p8 and p8 == com or \
    p3 == p6 and p6 == p9 and p9 == com or \
    p1 == p5 and p5 == p9 and p9 == com or \
    p3 == p5 and p5 == p7 and p7 == com:
        print('DERROTA!\nQUE PENA! Você perdeu.')
        gameOver = True
        return gameOver
    elif p1 != 1 and p2 != 2 and p3 != 3 and \
    p4 != 4 and p5 != 5 and p6 != 6 and \
    p7 != 7 and p8 != 8 and p9 != 9:
        gameOver = True
        print('EMPATE!!!\nDEU VELHA!!!')
        return gameOver

    else:
        gameOver = False
        return gameOver

print('')
print('Bem-vindo ao Tic-Tac-Toe!')
print('=' * 25)
print('')
print('\033[4mRegras do jogo\033[m:')
print('Você jogará com {} e o computador com {}.'.format(player, com))
print('A primeira jogada é do computador.')
print('Vence quem primeiro fizer uma sequência de três símbolos iguais na horizontal, vertical ou diagonal.')
print('BOA SORTE!!!')
print('')
print('=' * 25)
print('Vez do computador...')
print('')
board[1][1] = com
sleep(1)
printBoard()
print('')
while gameOver == False:
    playerTurn()
    if gameOver == False:
        comTurn()
else:
    print('FIM DE JOGO!')