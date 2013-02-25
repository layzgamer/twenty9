# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverpage.ui'
#
# Created: Fri Feb 15 23:49:08 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(441, 294)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Clients = QtGui.QListView(Dialog)
        self.Clients.setObjectName(_fromUtf8("Clients"))
        self.verticalLayout.addWidget(self.Clients)
        self.ChatBox = QtGui.QTextBrowser(Dialog)
        self.ChatBox.setObjectName(_fromUtf8("ChatBox"))
        self.verticalLayout.addWidget(self.ChatBox)
        self.Chat = QtGui.QLineEdit(Dialog)
        self.Chat.setObjectName(_fromUtf8("Chat"))
        self.verticalLayout.addWidget(self.Chat)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.InsertBot = QtGui.QPushButton(Dialog)
        self.InsertBot.setObjectName(_fromUtf8("InsertBot"))
        self.verticalLayout_2.addWidget(self.InsertBot)
        self.MoveUp = QtGui.QPushButton(Dialog)
        self.MoveUp.setObjectName(_fromUtf8("MoveUp"))
        self.verticalLayout_2.addWidget(self.MoveUp)
        self.MoveDown = QtGui.QPushButton(Dialog)
        self.MoveDown.setObjectName(_fromUtf8("MoveDown"))
        self.verticalLayout_2.addWidget(self.MoveDown)
        self.Remove = QtGui.QPushButton(Dialog)
        self.Remove.setObjectName(_fromUtf8("Remove"))
        self.verticalLayout_2.addWidget(self.Remove)
        self.Start = QtGui.QPushButton(Dialog)
        self.Start.setObjectName(_fromUtf8("Start"))
        self.verticalLayout_2.addWidget(self.Start)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.Enter = QtGui.QPushButton(Dialog)
        self.Enter.setObjectName(_fromUtf8("Enter"))
        self.verticalLayout_2.addWidget(self.Enter)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.InsertBot.setText(QtGui.QApplication.translate("Dialog", "Insert Bot", None, QtGui.QApplication.UnicodeUTF8))
        self.MoveUp.setText(QtGui.QApplication.translate("Dialog", "Move Up", None, QtGui.QApplication.UnicodeUTF8))
        self.MoveDown.setText(QtGui.QApplication.translate("Dialog", "Move Down", None, QtGui.QApplication.UnicodeUTF8))
        self.Remove.setText(QtGui.QApplication.translate("Dialog", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.Start.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.Enter.setText(QtGui.QApplication.translate("Dialog", "Enter", None, QtGui.QApplication.UnicodeUTF8))

