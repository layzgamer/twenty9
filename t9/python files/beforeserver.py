# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beforeserver.ui'
#
# Created: Fri Feb 15 23:48:03 2013
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
        Dialog.resize(431, 41)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.Name = QtGui.QLineEdit(Dialog)
        self.Name.setObjectName(_fromUtf8("Name"))
        self.horizontalLayout.addWidget(self.Name)
        self.Create = QtGui.QPushButton(Dialog)
        self.Create.setObjectName(_fromUtf8("Create"))
        self.horizontalLayout.addWidget(self.Create)
        self.Create.connect(self.Create, QtCore.SIGNAL("clicked()"),self.verify)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def verify(self):
        name = self.Name.text()
        if name == None:
            pass
        else :
            createServer(name)
            self.window.close()
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Enter Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.Create.setText(QtGui.QApplication.translate("Dialog", "Create", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtNetwork
import serverpage,Server,joingame
dialogbs = QtGui.QDialog()
server1 = Server.Server()
socket = QtNetwork.QTcpSocket()
serverpageformat = serverpage.Ui_Dialog()
    
def createServer(client):
        global name
        server1.start()
        name = client
        joingameformat = joingame.Ui_Dialog()
        joingameformat.setupUi(dialogbs)
        joingameformat.Name.setText(name)
        joingameformat.Server.setText(server1.server.serverAddress().toString())
        joingameformat.Port.setText(str(server1.server.serverPort()))
        joingameformat.Join.click()
        """
        serverpageformat.setupUi(dialogbs)
        dialogbs.show()
        address = str(server1.server.serverAddress())
        port = int(server1.server.serverPort())
        server1.join()
        socket.connectToHost(address, port)
        socket.connect(socket, QtCore.SIGNAL("connected"),connectionEstablished)
        """
    
def connectionEstablished():
    print "Created and connected!"
    