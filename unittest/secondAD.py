from movePiece import move
from getSet import makeMap
from selectPiece import select

def gameMain(WhatToDo, target, location):

    gameMap = makeMap.gameMap
    deck1 = makeMap.deck1p
    deck2 = makeMap.deck2p
    cnt = 1

    # for i in gameMap:
    #     print(i)
    # print('player1: ', deck1)
    # print('player2: ', deck2)

    if WhatToDo == 'move':

        if '子' in gameMap[target[0]][target[1]]:
            move.soldier(target,location,cnt)

        elif '相' in gameMap[target[0]][target[1]]:
            move.secGeneral(target,location,cnt)

        elif '將' in gameMap[target[0]][target[1]]:
            move.firstGeneral(target,location,cnt)

        elif '王' in gameMap[target[0]][target[1]]:
            cnt -= 1
            move.King(target,location,cnt)

        elif '侯' in gameMap[target[0]][target[1]]:
            move.thrGeneral(target, location, cnt)

        else:
            print('다시 입력 하세요')


    elif WhatToDo == 'select':
        select.putPiece(target,location,cnt)

    for i in gameMap:
        print(i)
    print(deck1)
    print(deck2)
    cnt += 1
    # else:
    #     if '王2' in deck1:
    #         print('player 1 win')
    #     else:
    #         print('player 2 win')

def finish(deck1, deck2):

    if '王2' in deck1 or '王1' in deck2:
        return False
    else:
        return True

if __name__ == '__main__':
    gameMain()
