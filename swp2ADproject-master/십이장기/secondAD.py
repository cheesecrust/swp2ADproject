from movePiece import move
from getSet import makeMap
from selectPiece import select

def gameMain():

    gameMap = makeMap.gameMap
    deck1 = makeMap.deck1p
    deck2 = makeMap.deck2p
    cnt = 1

    for i in gameMap:
        print(i)
    print('player1: ', deck1)
    print('player2: ', deck2)

    while finish(deck1, deck2):
        if cnt % 2 == 0:
            print('2 player turn')
        else:
            print('1 player turn')
        WhatToDo = input()

        if WhatToDo == 'move':

            target = list(map(int, input().split()))
            location = list(map(int, input().split()))

            if '子' in gameMap[target[0]][target[1]]:
                if move.soldier(target,location,cnt):
                    continue
            elif '相' in gameMap[target[0]][target[1]]:
                if move.secGeneral(target,location,cnt):
                    continue
            elif '將' in gameMap[target[0]][target[1]]:
                if move.firstGeneral(target,location,cnt):
                    continue
            elif '王' in gameMap[target[0]][target[1]]:
                if move.King(target,location,cnt):
                    continue
            elif '侯' in gameMap[target[0]][target[1]]:
                if move.thrGeneral(target, location, cnt):
                    continue
            else:
                print('다시 입력 하세요')
                continue

        else:

            target = int(input())
            location = list(map(int, input().split()))
            select.putPiece(target,location,cnt)

        for i in gameMap:
            print(i)
        print('player1: ', deck1)
        print('player2: ', deck2)
        cnt += 1
    else:
        if '王2' in deck1:
            print('player 1 win')
        else:
            print('player 2 win')

def finish(deck1, deck2):

    if '王2' in deck1 or '王1' in deck2:
        return False
    else:
        return True

if __name__ == '__main__':
    gameMain()
