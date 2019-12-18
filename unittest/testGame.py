import unittest
import secondAD
import getSet

class testGame(unittest.TestCase):

    def testCase1(self):
        secondAD.gameMain('move', [1, 1], [1, 2])

    def testCase2(self):
        getSet.makeMap.gameMap = [['相1', ' ', ' ', '將2'], ['王1', '子1', '子2', '王2'], ['將1', ' ', ' ', '相2']]
        getSet.makeMap.deck1p = []
        getSet.makeMap.deck2p = []

        secondAD.gameMain('move', [1, 1], [1, 2])
        secondAD.gameMain('move', [1, 3], [1, 2])
        secondAD.gameMain('select', 0,[0,1])

if __name__ == '__main__':
    unittest.main()