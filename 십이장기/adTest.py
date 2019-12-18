import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from getSet import makeMap
from movePiece import move


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setGeometry(550, 200, 1000, 700)
        self.setWindowTitle("12 LongTime")

        # 사용자 인터페이스
        self.turn = 1
        self.turnMessage = '{0} player'.format(self.turn)
        self.choseMessage = QLabel(self.turnMessage, self)
        self.choseMessage.setFont(QtGui.QFont("궁서", 20))
        self.choseMessage.move(150, 550)

        self.message = '相'
        self.stateMessage = QLabel('相', self)
        self.stateMessage.setFont(QtGui.QFont("궁서", 50))
        self.stateMessage.setStyleSheet("background:white")
        self.stateMessage.move(300, 530)
        self.stateMessage.resize(70, 70)

        self.resultMessage = QLabel("' 'P WIN", self)
        self.resultMessage.setFont(QtGui.QFont("궁서", 20))
        self.resultMessage.move(650, 550)

        firstPlayer = QLabel("1P", self)
        firstPlayer.setFont(QtGui.QFont("궁서", 20))
        firstPlayer.setStyleSheet("color:blue")
        secondPlayer = QLabel("2P", self)
        secondPlayer.setFont(QtGui.QFont("궁서", 20))
        secondPlayer.setStyleSheet("color:red")

        firstPlayer.move(650, 50)
        secondPlayer.move(650, 280)

        self.a_StealButton = QPushButton("", self)
        self.a_StealButton.setFont(QtGui.QFont("궁서", 10))
        self.a_StealButton.setStyleSheet("color:blue")
        self.a_StealButton.resize(50, 50)
        self.a_StealButton.move(650, 110)

        self.b_StealButton = QPushButton("", self)
        self.b_StealButton.setFont(QtGui.QFont("궁서", 10))
        self.b_StealButton.setStyleSheet("color:blue")
        self.b_StealButton.resize(50, 50)
        self.b_StealButton.move(720, 110)

        self.c_StealButton = QPushButton("", self)
        self.c_StealButton.setFont(QtGui.QFont("궁서", 10))
        self.c_StealButton.setStyleSheet("color:blue")
        self.c_StealButton.resize(50, 50)
        self.c_StealButton.move(790, 110)

        self.d_StealButton = QPushButton("", self)
        self.d_StealButton.setFont(QtGui.QFont("궁서", 10))
        self.d_StealButton.setStyleSheet("color:blue")
        self.d_StealButton.resize(50, 50)
        self.d_StealButton.move(650, 200)

        self.e_StealButton = QPushButton("", self)
        self.e_StealButton.setFont(QtGui.QFont("궁서", 10))
        self.e_StealButton.setStyleSheet("color:blue")
        self.e_StealButton.resize(50, 50)
        self.e_StealButton.move(720, 200)

        self.f_StealButton = QPushButton("", self)
        self.f_StealButton.setFont(QtGui.QFont("궁서", 10))
        self.f_StealButton.setStyleSheet("color:blue")
        self.f_StealButton.resize(50, 50)
        self.f_StealButton.move(790, 200)

        self.g_StealButton = QPushButton("", self)
        self.g_StealButton.setFont(QtGui.QFont("궁서", 10))
        self.g_StealButton.setStyleSheet("color:blue")
        self.g_StealButton.resize(50, 50)
        self.g_StealButton.move(650, 340)

        self.h_StealButton = QPushButton("", self)
        self.h_StealButton.setFont(QtGui.QFont("궁서", 10))
        self.h_StealButton.setStyleSheet("color:blue")
        self.h_StealButton.resize(50, 50)
        self.h_StealButton.move(720, 340)

        self.i_StealButton = QPushButton("", self)
        self.i_StealButton.setFont(QtGui.QFont("궁서", 10))
        self.i_StealButton.setStyleSheet("color:blue")
        self.i_StealButton.resize(50, 50)
        self.i_StealButton.move(790, 340)

        self.j_StealButton = QPushButton("", self)
        self.j_StealButton.setFont(QtGui.QFont("궁서", 10))
        self.j_StealButton.setStyleSheet("color:blue")
        self.j_StealButton.resize(50, 50)
        self.j_StealButton.move(650, 430)

        self.k_StealButton = QPushButton("", self)
        self.k_StealButton.setFont(QtGui.QFont("궁서", 10))
        self.k_StealButton.setStyleSheet("color:blue")
        self.k_StealButton.resize(50, 50)
        self.k_StealButton.move(720, 430)

        self.l_StealButton = QPushButton("", self)
        self.l_StealButton.setFont(QtGui.QFont("궁서", 10))
        self.l_StealButton.setStyleSheet("color:blue")
        self.l_StealButton.resize(50, 50)
        self.l_StealButton.move(790, 430)

        # 장기 map
        self.A_button = QPushButton(makeMap.gameMap[0][0], self)
        self.A_button.setFont(QtGui.QFont("궁서", 20))
        self.A_button.setStyleSheet("background:yellow")
        self.A_button.resize(100, 100)
        self.A_button.move(50, 50)
        self.A_button.setObjectName('00')

        self.B_button = QPushButton(makeMap.gameMap[0][1], self)
        self.B_button.setFont(QtGui.QFont("궁서", 20))
        self.B_button.setStyleSheet("")
        self.B_button.resize(100, 100)
        self.B_button.move(200, 50)
        self.B_button.setObjectName('01')

        self.C_button = QPushButton(makeMap.gameMap[0][2], self)
        self.C_button.setFont(QtGui.QFont("궁서", 20))
        self.C_button.setStyleSheet("")
        self.C_button.resize(100, 100)
        self.C_button.move(350, 50)
        self.C_button.setObjectName('02')

        self.D_button = QPushButton(makeMap.gameMap[0][3], self)
        self.D_button.setFont(QtGui.QFont("궁서", 20))
        self.D_button.setStyleSheet("background:teal")
        self.D_button.resize(100, 100)
        self.D_button.move(500, 50)
        self.D_button.setObjectName('03')

        self.E_button = QPushButton(makeMap.gameMap[1][0], self)
        self.E_button.setFont(QtGui.QFont("궁서", 20))
        self.E_button.setStyleSheet("background:yellow")
        self.E_button.resize(100, 100)
        self.E_button.move(50, 200)
        self.E_button.setObjectName('10')

        self.F_button = QPushButton(makeMap.gameMap[1][1], self)
        self.F_button.setFont(QtGui.QFont("궁서", 20))
        self.F_button.setStyleSheet("")
        self.F_button.resize(100, 100)
        self.F_button.move(200, 200)
        self.F_button.setObjectName('11')

        self.G_button = QPushButton(makeMap.gameMap[1][2], self)
        self.G_button.setFont(QtGui.QFont("궁서", 20))
        self.G_button.setStyleSheet("")
        self.G_button.resize(100, 100)
        self.G_button.move(350, 200)
        self.G_button.setObjectName('12')

        self.H_button = QPushButton(makeMap.gameMap[1][3], self)
        self.H_button.setFont(QtGui.QFont("궁서", 20))
        self.H_button.setStyleSheet("background:teal")
        self.H_button.resize(100, 100)
        self.H_button.move(500, 200)
        self.H_button.setObjectName('13')

        self.I_button = QPushButton(makeMap.gameMap[2][0], self)
        self.I_button.setFont(QtGui.QFont("궁서", 20))
        self.I_button.setStyleSheet("background:yellow")
        self.I_button.resize(100, 100)
        self.I_button.move(50, 350)
        self.I_button.setObjectName('20')

        self.J_button = QPushButton(makeMap.gameMap[2][1], self)
        self.J_button.setFont(QtGui.QFont("궁서", 20))
        self.J_button.setStyleSheet("")
        self.J_button.resize(100, 100)
        self.J_button.move(200, 350)
        self.J_button.setObjectName('21')

        self.K_button = QPushButton(makeMap.gameMap[2][2], self)
        self.K_button.setFont(QtGui.QFont("궁서", 20))
        self.K_button.setStyleSheet("")
        self.K_button.resize(100, 100)
        self.K_button.move(350, 350)
        self.K_button.setObjectName('22')

        self.L_button = QPushButton(makeMap.gameMap[2][3], self)
        self.L_button.setFont(QtGui.QFont("궁서", 20))
        self.L_button.setStyleSheet("background:teal")
        self.L_button.resize(100, 100)
        self.L_button.move(500, 350)
        self.L_button.setObjectName('23')

        # 클릭 이후 상태창


        #pybutton = QPushButton('Click me', self)
        self.A_button.clicked.connect(self.mapClickMethod)
        self.B_button.clicked.connect(self.mapClickMethod)
        self.C_button.clicked.connect(self.mapClickMethod)
        self.D_button.clicked.connect(self.mapClickMethod)
        self.E_button.clicked.connect(self.mapClickMethod)
        self.F_button.clicked.connect(self.mapClickMethod)
        self.G_button.clicked.connect(self.mapClickMethod)
        self.H_button.clicked.connect(self.mapClickMethod)
        self.I_button.clicked.connect(self.mapClickMethod)
        self.J_button.clicked.connect(self.mapClickMethod)
        self.K_button.clicked.connect(self.mapClickMethod)
        self.L_button.clicked.connect(self.mapClickMethod)
        #pybutton.resize(100,32)
        #pybutton.move(50, 50)
        self.a_StealButton.clicked.connect(self.put1pPiece)
        self.b_StealButton.clicked.connect(self.put1pPiece)
        self.c_StealButton.clicked.connect(self.put1pPiece)
        self.d_StealButton.clicked.connect(self.put1pPiece)
        self.e_StealButton.clicked.connect(self.put1pPiece)
        self.f_StealButton.clicked.connect(self.put1pPiece)

        self.g_StealButton.clicked.connect(self.put2pPiece)
        self.h_StealButton.clicked.connect(self.put2pPiece)
        self.i_StealButton.clicked.connect(self.put2pPiece)
        self.j_StealButton.clicked.connect(self.put2pPiece)
        self.k_StealButton.clicked.connect(self.put2pPiece)
        self.l_StealButton.clicked.connect(self.put2pPiece)


        self.currentPosition = [0,0]
        self.location = [0,0]

    def reMake(self):
        self.turn = 2 ** ((self.turn - 1) % 2)
        self.A_button.setText(makeMap.gameMap[0][0])
        self.B_button.setText(makeMap.gameMap[0][1])
        self.C_button.setText(makeMap.gameMap[0][2])
        self.D_button.setText(makeMap.gameMap[0][3])
        self.E_button.setText(makeMap.gameMap[1][0])
        self.F_button.setText(makeMap.gameMap[1][1])
        self.G_button.setText(makeMap.gameMap[1][2])
        self.H_button.setText(makeMap.gameMap[1][3])
        self.I_button.setText(makeMap.gameMap[2][0])
        self.J_button.setText(makeMap.gameMap[2][1])
        self.K_button.setText(makeMap.gameMap[2][2])
        self.L_button.setText(makeMap.gameMap[2][3])
        self.turnMessage = '{0} player'.format(self.turn)
        self.choseMessage.setText(self.turnMessage)

        if ('王' in makeMap.deck1p) or ('王' in makeMap.deck2p):
            print('1234')
            if self.turn == 1:
                message = '{0} player WIN'.format(2)
            else:
                message = '{0} player WIN'.format(1)
            self.resultMessage.setText(message)

        try:
            self.a_StealButton.setText(makeMap.deck1p[0])
            self.b_StealButton.setText(makeMap.deck1p[1])
            self.c_StealButton.setText(makeMap.deck1p[2])
            self.d_StealButton.setText(makeMap.deck1p[3])
            self.e_StealButton.setText(makeMap.deck1p[4])
            self.f_StealButton.setText(makeMap.deck1p[5])
        except:
            print(makeMap.deck1p)

        try:
            self.g_StealButton.setText(makeMap.deck2p[0])
            self.h_StealButton.setText(makeMap.deck2p[1])
            self.i_StealButton.setText(makeMap.deck2p[4])
            self.j_StealButton.setText(makeMap.deck2p[5])
            self.k_StealButton.setText(makeMap.deck2p[2])
            self.l_StealButton.setText(makeMap.deck2p[3])
        except:
            print(makeMap.deck1p)

    def put1pPiece(self):
        if self.turn == 1:
            button = self.sender()
            key = button.text()
            self.message = key
            print(self.message)
            self.stateMessage.setText(self.message)

    def put2pPiece(self):
        if self.turn == 2:
            button = self.sender()
            key = button.text()
            self.message = key
            print(self.message)
            self.stateMessage.setText(self.message)

    def mapClickMethod(self):
        print(self.turn)
        print(makeMap.deck1p)
        print(makeMap.deck2p)

        button = self.sender()
        if str(self.turn) in makeMap.gameMap[int(button.objectName()[0])][int(button.objectName()[1])]:
            self.currentPosition = [int(button.objectName()[0]), int(button.objectName()[1])]
            key = button.text()
            self.message = key
            self.stateMessage.setText(self.message)
        else:
            self.location = [int(button.objectName()[0]), int(button.objectName()[1])]

            if len(self.message) != 1:
                if '子' in self.message:
                    tmp = move.soldier(self.currentPosition, self.location, self.turn)
                    if not(tmp):
                        self.turn += 1
                        self.message = ''
                        self.reMake()

                elif '將' in self.message :
                    tmp = move.firstGeneral(self.currentPosition, self.location, self.turn)
                    if not(tmp):
                        self.turn += 1
                        self.message = ''
                        self.reMake()

                elif '王' in self.message :
                    tmp = move.King(self.currentPosition, self.location, self.turn)
                    if not(tmp):
                        self.turn += 1
                        self.message = ''
                        self.reMake()

                elif '相' in self.message :
                    tmp = move.secGeneral(self.currentPosition, self.location, self.turn)
                    if not(tmp):
                        self.turn += 1
                        self.message = ''
                        self.reMake()

                elif '侯' in self.message:
                    tmp = move.thrGeneral(self.currentPosition, self.location, self.turn)
                    if not(tmp):
                        self.turn += 1
                        self.message = ''
                        self.reMake()
            else:
                if makeMap.gameMap[int(button.objectName()[0])][int(button.objectName()[1])] == ' ':
                    makeMap.gameMap[int(button.objectName()[0])][int(button.objectName()[1])] = self.message + str(self.turn)
                    if self.turn == 1:
                        makeMap.deck1p.remove(self.message)
                    else:
                        makeMap.deck2p.remove(self.message)
                    self.turn += 1
                    self.message = ''

                    self.a_StealButton.setText('')
                    self.b_StealButton.setText('')
                    self.c_StealButton.setText('')
                    self.d_StealButton.setText('')
                    self.e_StealButton.setText('')
                    self.f_StealButton.setText('')

                    self.g_StealButton.setText('')
                    self.h_StealButton.setText('')
                    self.i_StealButton.setText('')
                    self.j_StealButton.setText('')
                    self.k_StealButton.setText('')
                    self.l_StealButton.setText('')

                    self.reMake()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())