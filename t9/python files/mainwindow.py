# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Feb 15 19:49:03 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import resource_rc


CARD_WIDTH = 69
CARD_HEIGHT = 100
CARD_SIZE = QtCore.QSize(CARD_WIDTH-5, CARD_HEIGHT-5)
BUTTON_SIZE = QtCore.QSize(CARD_WIDTH, CARD_HEIGHT)

try:
    _fromUtf8 = QtCore.QString
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):

    HAND = []
    PIT = []
    SCORE_SELF = (0,0)
    SCORE_OPPONENT = (0,0)

    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(CARD_WIDTH*12, CARD_HEIGHT*6)
        MainWindow.setStyleSheet(_fromUtf8("background-image:url(:/backgrounds/background.jpg)"))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(CARD_WIDTH*12, CARD_HEIGHT*6))
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setStyleSheet(_fromUtf8("background:transparent"))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.opponentScore = QtGui.QGroupBox(self.centralWidget)
        self.opponentScore.setTitle(_fromUtf8(""))
        self.opponentScore.setObjectName(_fromUtf8("opponentScore"))
        # <--------- Opponent Score --------->
        self.OpponentScoreCardFront = QtGui.QPushButton(self.opponentScore)
        self.OpponentScoreCardFront.setGeometry(QtCore.QRect(40, 0, CARD_WIDTH, CARD_HEIGHT))
        self.OpponentScoreCardFront.setMinimumSize(BUTTON_SIZE)
        self.OpponentScoreCardFront.setText(_fromUtf8(""))
        self.OpponentScoreCardFront.setObjectName(_fromUtf8("OpponentScoreCardFront"))
        self.OpponentScoreCardBack = QtGui.QPushButton(self.opponentScore)
        self.OpponentScoreCardBack.setGeometry(QtCore.QRect(70, 0, CARD_WIDTH, CARD_HEIGHT))
        self.OpponentScoreCardBack.setMinimumSize(BUTTON_SIZE)
        self.OpponentScoreCardBack.setText(_fromUtf8(""))
        self.OpponentScoreCardBack.setObjectName(_fromUtf8("OpponentScoreCardBack"))
        self.gridLayout.addWidget(self.opponentScore, 0, 0, 1, 1)

        # <--------- Self Score --------->
        self.SelfScore = QtGui.QGroupBox(self.centralWidget)
        self.SelfScore.setTitle(_fromUtf8(""))
        self.SelfScore.setObjectName(_fromUtf8("SelfScore"))
        self.SelfScoreCardFront = QtGui.QPushButton(self.SelfScore)
        self.SelfScoreCardFront.setGeometry(QtCore.QRect(50, 10, CARD_WIDTH, CARD_HEIGHT))
        self.SelfScoreCardFront.setMinimumSize(BUTTON_SIZE)
        self.SelfScoreCardFront.setText(_fromUtf8(""))
        self.SelfScoreCardFront.setObjectName(_fromUtf8("SelfScoreCardFront"))
        self.SelfScoreCardBack = QtGui.QPushButton(self.SelfScore)
        self.SelfScoreCardBack.setGeometry(QtCore.QRect(80, 10, CARD_WIDTH, CARD_HEIGHT))
        self.SelfScoreCardBack.setMinimumSize(BUTTON_SIZE)
        self.SelfScoreCardBack.setText(_fromUtf8(""))
        self.SelfScoreCardBack.setObjectName(_fromUtf8("SelfScoreCardBack"))
        self.gridLayout.addWidget(self.SelfScore, 3, 2, 1, 1)


        self.emptyBox2 = QtGui.QGroupBox(self.centralWidget)
        self.emptyBox2.setTitle(_fromUtf8(""))
        self.emptyBox2.setFlat(True)
        self.emptyBox2.setObjectName(_fromUtf8("emptyBox2"))
        self.gridLayout.addWidget(self.emptyBox2, 3, 0, 1, 1)


        # <--------- Trump Box --------->
        self.emptyBox1 = QtGui.QGroupBox(self.centralWidget)
        self.emptyBox1.setTitle(_fromUtf8(""))
        self.emptyBox1.setFlat(True)
        self.emptyBox1.setObjectName(_fromUtf8("emptyBox1"))
        self.TrumpCard = QtGui.QPushButton(self.emptyBox1)
        self.TrumpCard.setGeometry(QtCore.QRect(90, 10, CARD_WIDTH, CARD_HEIGHT))
        self.TrumpCard.setMinimumSize(BUTTON_SIZE)
        self.TrumpCard.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/backs/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TrumpCard.setIcon(icon)
        self.TrumpCard.setIconSize(CARD_SIZE)
        self.TrumpCard.setObjectName(_fromUtf8("TrumpCard"))
        self.gridLayout.addWidget(self.emptyBox1, 0, 2, 1, 1)
        # <--------- Left Player's Hand --------->
        self.LeftHand = QtGui.QGroupBox(self.centralWidget)
        self.LeftHand.setMinimumSize(CARD_WIDTH, CARD_HEIGHT*3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(12)
        font.setItalic(True)
        self.LeftHand.setFont(font)
        self.LeftHand.setObjectName(_fromUtf8("LeftHand"))
        self.gridLayout.addWidget(self.LeftHand, 1, 0, 2, 1)

        # <--------- Right Player's Hand --------->
        self.RightHand = QtGui.QGroupBox(self.centralWidget)
        self.RightHand.setMinimumSize(QtCore.QSize(CARD_WIDTH, CARD_HEIGHT*3))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(12)
        font.setItalic(True)
        self.RightHand.setFont(font)
        self.RightHand.setObjectName(_fromUtf8("RightHand"))
        self.gridLayout.addWidget(self.RightHand, 1, 2, 2, 1)


        # <--------- Bottom Player's Hand --------->
        self.BottomHand = QtGui.QGroupBox(self.centralWidget)
        self.BottomHand.setMinimumSize(CARD_WIDTH*3, CARD_HEIGHT*1.5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.BottomHand.setFont(font)
        self.BottomHand.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.BottomHand.setObjectName(_fromUtf8("BottomHand"))
        self.gridLayout.addWidget(self.BottomHand, 3, 1, 1, 1)


        # <--------- Top Player's Hand --------->
        self.TopHand = QtGui.QGroupBox(self.centralWidget)
        self.TopHand.setMinimumSize(CARD_WIDTH*3, CARD_HEIGHT*1.5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(12)
        font.setItalic(True)
        self.TopHand.setFont(font)
        self.TopHand.setObjectName(_fromUtf8("TopHand"))
        self.gridLayout.addWidget(self.TopHand, 0, 1, 1, 1)

        # <--------- Pit --------->
        self.Pit = QtGui.QGroupBox(self.centralWidget)
        self.Pit.setTitle(_fromUtf8(""))
        self.Pit.setObjectName(_fromUtf8("Pit"))
        W = CARD_WIDTH*4
        H = CARD_HEIGHT*2.5
        self.LeftPit = QtGui.QPushButton(self.Pit)
        self.LeftPit.setGeometry(QtCore.QRect(W/2-CARD_WIDTH,H/2-CARD_HEIGHT/2, CARD_WIDTH, CARD_HEIGHT))
        self.LeftPit.setMinimumSize(BUTTON_SIZE)
        self.LeftPit.setText(_fromUtf8(""))
        self.LeftPit.setObjectName(_fromUtf8("LeftPit"))
        self.TopPit = QtGui.QPushButton(self.Pit)
        self.TopPit.setGeometry(QtCore.QRect(W/2-CARD_WIDTH/2,H/2-CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT))
        self.TopPit.setMinimumSize(BUTTON_SIZE)
        self.TopPit.setText(_fromUtf8(""))
        self.TopPit.setObjectName(_fromUtf8("TopPit"))
        self.RightPit = QtGui.QPushButton(self.Pit)
        self.RightPit.setGeometry(QtCore.QRect(W/2,H/2-CARD_HEIGHT/2, CARD_WIDTH, CARD_HEIGHT))
        self.RightPit.setMinimumSize(BUTTON_SIZE)
        self.RightPit.setText(_fromUtf8(""))
        self.RightPit.setObjectName(_fromUtf8("RightPit"))
        self.BottomPit = QtGui.QPushButton(self.Pit)
        self.BottomPit.setGeometry(QtCore.QRect(W/2-CARD_WIDTH/2,H/2, CARD_WIDTH, CARD_HEIGHT))
        self.BottomPit.setMinimumSize(BUTTON_SIZE)
        self.BottomPit.setText(_fromUtf8(""))
        self.BottomPit.setObjectName(_fromUtf8("BottomPit"))
        self.gridLayout.addWidget(self.Pit, 1, 1, 2, 1)


        self.addCards()

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.GameMenu = QtGui.QMenu(self.menuBar)
        self.GameMenu.setFont(font)
        self.GameMenu.setObjectName(_fromUtf8("GameMenu"))
        self.NewGameMenu = QtGui.QMenu(self.GameMenu)
        self.NewGameMenu.setFont(font)
        self.NewGameMenu.setObjectName(_fromUtf8("NewGameMenu"))
        self.HelpMenu = QtGui.QMenu(self.menuBar)
        self.HelpMenu.setFont(font)
        self.HelpMenu.setObjectName(_fromUtf8("HelpMenu"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setFont(font)
        self.mainToolBar.setStyleSheet(_fromUtf8("background:transparent"))
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setStyleSheet(_fromUtf8("background:transparent"))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.SaveGame = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveGame.setIcon(icon1)
        self.SaveGame.setFont(font)
        self.SaveGame.setObjectName(_fromUtf8("SaveGame"))
        self.LoadGame = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LoadGame.setIcon(icon2)
        self.LoadGame.setFont(font)
        self.LoadGame.setObjectName(_fromUtf8("LoadGame"))
        self.Exit = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit.setIcon(icon3)
        self.Exit.setFont(font)
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.Help = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Help.setIcon(icon4)
        self.Help.setFont(font)
        self.Help.setObjectName(_fromUtf8("Help"))
        self.Preferences = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Preferences.setIcon(icon5)
        self.Preferences.setFont(font)
        self.Preferences.setObjectName(_fromUtf8("Preferences"))
        self.JoinGame = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/join.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.JoinGame.setIcon(icon6)
        self.JoinGame.setFont(font)
        self.JoinGame.setObjectName(_fromUtf8("JoinGame"))
        self.SinglePlayer = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/user.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SinglePlayer.setIcon(icon7)
        self.SinglePlayer.setFont(font)
        self.SinglePlayer.setObjectName(_fromUtf8("SinglePlayer"))
        self.CreateGame = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/create.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CreateGame.setIcon(icon8)
        self.CreateGame.setFont(font)
        self.CreateGame.setObjectName(_fromUtf8("CreateGame"))
        self.NewGameMenu.addAction(self.CreateGame)
        self.NewGameMenu.addAction(self.JoinGame)
        self.NewGameMenu.addAction(self.SinglePlayer)
        self.GameMenu.addAction(self.NewGameMenu.menuAction())
        self.GameMenu.addAction(self.SaveGame)
        self.GameMenu.addAction(self.LoadGame)
        self.GameMenu.addSeparator()
        self.GameMenu.addAction(self.Preferences)
        self.GameMenu.addSeparator()
        self.GameMenu.addAction(self.Exit)
        self.HelpMenu.addAction(self.Help)
        self.menuBar.addAction(self.GameMenu.menuAction())
        self.menuBar.addAction(self.HelpMenu.menuAction())
        self.mainToolBar.addAction(self.CreateGame)
        self.mainToolBar.addAction(self.JoinGame)
        self.mainToolBar.addAction(self.SinglePlayer)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.SaveGame)
        self.mainToolBar.addAction(self.LoadGame)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.Preferences)
        self.mainToolBar.addAction(self.Help)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.Exit)
        self.CreateGame.connect(self.CreateGame, QtCore.SIGNAL("triggered()"), createGameTriggered)
        self.LoadGame.connect(self.LoadGame, QtCore.SIGNAL("triggered()"), loadGameTriggered)
        self.SaveGame.connect(self.SaveGame, QtCore.SIGNAL("triggered()"), self.saveGameTriggered)
        self.JoinGame.connect(self.JoinGame, QtCore.SIGNAL("triggered()"), joinGameTriggered)
        self.SinglePlayer.connect(self.SinglePlayer, QtCore.SIGNAL("triggered()"), singlePlayerTriggered)
        self.Preferences.connect(self.Preferences, QtCore.SIGNAL("triggered()"), preferencesTriggered)
        self.Help.connect(self.Help, QtCore.SIGNAL("triggered()"), helpTriggered)
        self.Exit.connect(self.Exit, QtCore.SIGNAL("triggered()"), exitTriggered)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def saveGameTriggered(self):
        #print "action 4"
        return


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "twenty9", None, QtGui.QApplication.UnicodeUTF8))
        self.LeftHand.setTitle(QtGui.QApplication.translate("MainWindow", "PlayerName", None, QtGui.QApplication.UnicodeUTF8))
        self.RightHand.setTitle(QtGui.QApplication.translate("MainWindow", "PlayerName", None, QtGui.QApplication.UnicodeUTF8))
        self.BottomHand.setTitle(QtGui.QApplication.translate("MainWindow", "PlayerName", None, QtGui.QApplication.UnicodeUTF8))
        self.TopHand.setTitle(QtGui.QApplication.translate("MainWindow", "PlayerName", None, QtGui.QApplication.UnicodeUTF8))
        self.GameMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Game", None, QtGui.QApplication.UnicodeUTF8))
        self.NewGameMenu.setTitle(QtGui.QApplication.translate("MainWindow", "New Game", None, QtGui.QApplication.UnicodeUTF8))
        self.HelpMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveGame.setText(QtGui.QApplication.translate("MainWindow", "Save Game", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveGame.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadGame.setText(QtGui.QApplication.translate("MainWindow", "Load Game", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadGame.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.Exit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.Help.setText(QtGui.QApplication.translate("MainWindow", "Open Readme", None, QtGui.QApplication.UnicodeUTF8))
        self.Help.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.Preferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.Preferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.JoinGame.setText(QtGui.QApplication.translate("MainWindow", "Join Game", None, QtGui.QApplication.UnicodeUTF8))
        self.JoinGame.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+J", None, QtGui.QApplication.UnicodeUTF8))
        self.SinglePlayer.setText(QtGui.QApplication.translate("MainWindow", "Single Player", None, QtGui.QApplication.UnicodeUTF8))
        self.SinglePlayer.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.CreateGame.setText(QtGui.QApplication.translate("MainWindow", "Create Game", None, QtGui.QApplication.UnicodeUTF8))
        self.CreateGame.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))

    def addCards(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/backs/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # <--------- Left Player's Cards --------->
        self.LeftCard = QtGui.QPushButton(self.LeftHand)
        self.LeftCard.setGeometry(QtCore.QRect(80, 30, CARD_WIDTH, CARD_HEIGHT))
        self.LeftCard.setMinimumSize(BUTTON_SIZE)
        self.LeftCard.setText(_fromUtf8(""))
        self.LeftCard.setIcon(icon)
        self.LeftCard.setIconSize(CARD_SIZE)
        self.LeftCard.setObjectName(_fromUtf8("LeftCard"))

        # <--------- Right Player's Cards --------->
        self.RightCard = QtGui.QPushButton(self.RightHand)
        self.RightCard.setGeometry(QtCore.QRect(90, 30, CARD_WIDTH, CARD_HEIGHT))
        self.RightCard.setMinimumSize(BUTTON_SIZE)
        self.RightCard.setText(_fromUtf8(""))
        self.RightCard.setIcon(icon)
        self.RightCard.setIconSize(CARD_SIZE)
        self.RightCard.setObjectName(_fromUtf8("RightCard"))

        # <--------- Bottom Player's Cards --------->
        self.BottomCard = QtGui.QPushButton(self.BottomHand)
        self.BottomCard.setGeometry(QtCore.QRect(10, 30, CARD_WIDTH, CARD_HEIGHT))
        self.BottomCard.setMinimumSize(BUTTON_SIZE)
        self.BottomCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BottomCard.setObjectName(_fromUtf8("BottomCard"))

        # <--------- Top Player's Card --------->
        self.TopCard = QtGui.QPushButton(self.TopHand)
        self.TopCard.setGeometry(QtCore.QRect(0, 30, CARD_WIDTH, CARD_HEIGHT))
        self.TopCard.setMinimumSize(BUTTON_SIZE)
        self.TopCard.setText(_fromUtf8(""))
        self.TopCard.setIcon(icon)
        self.TopCard.setIconSize(CARD_SIZE)
        self.TopCard.setObjectName(_fromUtf8("TopCard"))

def createGameTriggered():
    global dialog
    dialog = QtGui.QDialog()
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    beforeserverformat.setupUi(dialog)
    dialog.show()
    #print "action 1"
    return
    
def joinGameTriggered():
    global dialog
    dialog = QtGui.QDialog()
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    joingameformat.setupUi(dialog)
    dialog.show()
    #print "action 2"
    return
def loadGameTriggered():
    global dialog
    dialog = QtGui.QDialog()
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    openformat.setupUi(dialog)
    dialog.show()
    #print "action 3"
    return
def preferencesTriggered():
    global dialog
    dialog = QtGui.QDialog()
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    settingsformat.setupUi(dialog)
    dialog.show()
    #print "action 5"
    return
def helpTriggered():
    #print "action 6"
    return
def singlePlayerTriggered():
    #print "action 7"
    return
def exitTriggered():
    window.close()
    #print "action 8"
    return

#<---------This starts the application------->
app = QtGui.QApplication(sys.argv)
import beforeserver,bid,joingame,open,settings,settrump
window = QtGui.QMainWindow()
program = Ui_MainWindow()
program.setupUi(window)
window.show()
beforeserverformat = beforeserver.Ui_Dialog()
bidformat = bid.Ui_Dialog()
joingameformat = joingame.Ui_Dialog()
openformat = open.Ui_Dialog()
settingsformat = settings.Ui_Dialog()
settrumpformat = settrump.Ui_Dialog()
sys.exit(app.exec_())