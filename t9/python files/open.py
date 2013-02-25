# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Open.ui'
#
# Created: Fri Feb 15 23:48:51 2013
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
        Dialog.resize(265, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.FileBrowser = QtGui.QTreeView(Dialog)
        self.FileBrowser.setObjectName(_fromUtf8("FileBrowser"))
        self.verticalLayout.addWidget(self.FileBrowser)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.FileName = QtGui.QLineEdit(Dialog)
        self.FileName.setObjectName(_fromUtf8("FileName"))
        self.horizontalLayout.addWidget(self.FileName)
        self.Open = QtGui.QPushButton(Dialog)
        self.Open.setObjectName(_fromUtf8("Open"))
        self.horizontalLayout.addWidget(self.Open)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.Open.setText(QtGui.QApplication.translate("Dialog", "Open", None, QtGui.QApplication.UnicodeUTF8))

