from getSet import makeMap

def cross(target, location):
    checkList = [[target[0] + 1, target[1]], [target[0], target[1] + 1], [target[0] - 1, target[1]],
                 [target[0], target[1] - 1]]

    if location in checkList:
        return True
    else:
        return False


def diagnol(target, location):
    checkList = [[target[0] + 1, target[1] + 1], [target[0] - 1, target[1] + 1], [target[0] - 1, target[1] - 1],
                 [target[0] + 1, target[1] - 1]]

    if location in checkList:
        return True
    else:
        return False

def halfDiagnol(target, location):
    checkList = [[target[0] + 1, target[1] + 1], [target[0] - 1, target[1] + 1]]

    if location in checkList:
        return True
    else:
        return False

class move:


    def King(target, location,cnt):
        if cross(target, location) or diagnol(target, location):

            if makeMap.gameMap[location[0]][location[1]] != ' ' and cnt % 2 == 0:
                if '侯' in makeMap.gameMap[location[0]][location[1]]:
                    makeMap.deck2p.append('子')
                else:
                    makeMap.deck2p.append(makeMap.gameMap[location[0]][location[1]][0])
            elif makeMap.gameMap[location[0]][location[1]] != ' ' and cnt % 2 != 0:
                if '侯' in makeMap.gameMap[location[0]][location[1]]:
                    makeMap.deck1p.append('子')
                else:
                    makeMap.deck1p.append(makeMap.gameMap[location[0]][location[1]][0])

            makeMap.gameMap[location[0]][location[1]] = makeMap.gameMap[target[0]][target[1]]
            makeMap.gameMap[target[0]][target[1]] = ' '
            return False
        else:
            print('다시 입력')
            return True


    def soldier(target, location, cnt):
        print(target)
        print(location)
        if location[0] == target[0] and location[1] - target[1] == 1:

            if makeMap.gameMap[location[0]][location[1]] != ' ' and cnt % 2 == 0:
                if '侯' in makeMap.gameMap[location[0]][location[1]]:
                    makeMap.deck2p.append('子')
                else:
                    makeMap.deck2p.append(makeMap.gameMap[location[0]][location[1]][0])

            elif makeMap.gameMap[location[0]][location[1]] != ' ' and cnt % 2 != 0:
                if '侯' in makeMap.gameMap[location[0]][location[1]]:
                    makeMap.deck1p.append('子')
                else:
                    makeMap.deck1p.append(makeMap.gameMap[location[0]][location[1]][0])


            if location[1] == 0 and cnt % 2 == 0:
                makeMap.gameMap[location[0]][location[1]] = '侯2'
                makeMap.gameMap[target[0]][target[1]] = ' '

            elif location[1] == 3 and cnt % 2 != 0:
                makeMap.gameMap[location[0]][location[1]] = '侯1'
                makeMap.gameMap[target[0]][target[1]] =  ' '

            else:
                makeMap.gameMap[location[0]][location[1]] = makeMap.gameMap[target[0]][target[1]]
                makeMap.gameMap[target[0]][target[1]] =  ' '
            return False
        else:
            print('다시 입력')
            return True

    def firstGeneral(target, location,cnt):

        if cross(target,location):

            if makeMap.gameMap[location[0]][location[1]] != ' ' and cnt % 2 == 0:
                if '侯' in makeMap.gameMap[location[0]][location[1]]:
                    makeMap.deck2p.append('子')
                else:
                    makeMap.deck2p.append(makeMap.gameMap[location[0]][location[1]][0])

            elif makeMap.gameMap[location[0]][location[1]] != ' ' and cnt % 2 != 0:
                if '侯' in makeMap.gameMap[location[0]][location[1]]:
                    makeMap.deck1p.append('子')
                else:
                    makeMap.deck1p.append(makeMap.gameMap[location[0]][location[1]][0])

            makeMap.gameMap[location[0]][location[1]] = makeMap.gameMap[target[0]][target[1]]
            makeMap.gameMap[target[0]][target[1]] = ' '
            return False

        else:
            print('다시입력')
            return True

    def secGeneral(target, location,cnt):

        if diagnol(target,location):

            if makeMap.gameMap[location[0]][location[1]] != ' ' and cnt % 2 == 0:
                if '侯' in makeMap.gameMap[location[0]][location[1]]:
                    makeMap.deck2p.append('子')
                else:
                    makeMap.deck2p.append(makeMap.gameMap[location[0]][location[1]][0])

            elif makeMap.gameMap[location[0]][location[1]] != ' ' and cnt % 2 != 0:
                if '侯' in makeMap.gameMap[location[0]][location[1]]:
                    makeMap.deck1p.append('子')
                else:
                    makeMap.deck1p.append(makeMap.gameMap[location[0]][location[1]][0])

            makeMap.gameMap[location[0]][location[1]] = makeMap.gameMap[target[0]][target[1]]
            makeMap.gameMap[target[0]][target[1]] = ' '
            return False

        else:
            print('다시 입력')
            return True

    def thrGeneral(target, location, cnt):

        if cross(target,location) or halfDiagnol(target,location) :

            if makeMap.gameMap[location[0]][location[1]] != ' ' and cnt % 2 == 0:
                if '侯' in makeMap.gameMap[location[0]][location[1]]:
                    makeMap.deck2p.append('子')
                else:
                    makeMap.deck2p.append(makeMap.gameMap[location[0]][location[1]][0])

            elif makeMap.gameMap[location[0]][location[1]] != ' ' and cnt % 2 != 0:
                if '侯' in makeMap.gameMap[location[0]][location[1]]:
                    makeMap.deck1p.append('子')
                else:
                    makeMap.deck1p.append(makeMap.gameMap[location[0]][location[1]][0])

            makeMap.gameMap[location[0]][location[1]] = makeMap.gameMap[target[0]][target[1]]
            makeMap.gameMap[target[0]][target[1]] = ' '
            return False

        else:
            print('다시 입력')
            return True