# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'joingame.ui'
#
# Created: Fri Feb 15 23:48:27 2013
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
        self.window = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(268, 121)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.NameLabel = QtGui.QLabel(Dialog)
        self.NameLabel.setObjectName(_fromUtf8("NameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.NameLabel)
        self.Name = QtGui.QLineEdit(Dialog)
        self.Name.setObjectName(_fromUtf8("Name"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.Name)
        self.ServerLabel = QtGui.QLabel(Dialog)
        self.ServerLabel.setObjectName(_fromUtf8("ServerLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.ServerLabel)
        self.Server = QtGui.QLineEdit(Dialog)
        self.Server.setObjectName(_fromUtf8("Server"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.Server)
        self.PortLabel = QtGui.QLabel(Dialog)
        self.PortLabel.setObjectName(_fromUtf8("PortLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.PortLabel)
        self.Port = QtGui.QLineEdit(Dialog)
        self.Port.setObjectName(_fromUtf8("Port"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.Port)
        self.verticalLayout.addLayout(self.formLayout)
        self.Join = QtGui.QPushButton(Dialog)
        self.Join.setObjectName(_fromUtf8("Join"))
        self.verticalLayout.addWidget(self.Join)
        self.Join.connect(self.Join, QtCore.SIGNAL("clicked()"),self.verify)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def verify(self):
        if self.Name.text() != None and self.Server.text()!= None and self.Port.text()!= None:
            createClient(self)
            self.window.close()
        return
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Join Game", None, QtGui.QApplication.UnicodeUTF8))
        self.NameLabel.setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.ServerLabel.setText(QtGui.QApplication.translate("Dialog", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.PortLabel.setText(QtGui.QApplication.translate("Dialog", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.Join.setText(QtGui.QApplication.translate("Dialog", "Join", None, QtGui.QApplication.UnicodeUTF8))
    
from PyQt4 import QtNetwork
import serverpage
dialogjg = QtGui.QDialog()
serverpageformat = serverpage.Ui_Dialog()

def createClient(Dialog):
    global name,socket
    socket = QtNetwork.QTcpSocket()
    name = str(Dialog.Name.text())
    server = str(Dialog.Server.text())
    port = int(Dialog.Port.text())
    socket.connectToHost(server, port)
    QtCore.QObject.connect(socket, QtCore.SIGNAL("connected()"),connectionSuccessful)
    return

def connectionSuccessful():
    print "Connected!"
    socket.write(QtCore.QByteArray("name:"+name))
    serverpageformat.setupUi(dialogjg)
    dialogjg.show()
    return
