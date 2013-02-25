# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bid.ui'
#
# Created: Fri Feb 15 23:47:39 2013
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
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(283, 281)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.BidLog = QtGui.QTextBrowser(Dialog)
        self.BidLog.setObjectName(_fromUtf8("BidLog"))
        self.verticalLayout.addWidget(self.BidLog)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Bid = QtGui.QSpinBox(Dialog)
        self.Bid.setMinimum(16)
        self.Bid.setMaximum(33)
        self.Bid.setObjectName(_fromUtf8("Bid"))
        self.horizontalLayout.addWidget(self.Bid)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Place Bid", None, QtGui.QApplication.UnicodeUTF8))

