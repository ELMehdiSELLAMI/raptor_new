# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Impacts_table.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgImpacts(object):
    def setupUi(self, dlgImpacts):
        dlgImpacts.setObjectName("dlgImpacts")
        dlgImpacts.setWindowModality(QtCore.Qt.NonModal)
        dlgImpacts.resize(400, 300)
        self.tblImpacts = QtWidgets.QTableWidget(dlgImpacts)
        self.tblImpacts.setGeometry(QtCore.QRect(10, 0, 380, 300))
        self.tblImpacts.setObjectName("tblImpacts")
        self.tblImpacts.setColumnCount(3)
        self.tblImpacts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblImpacts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblImpacts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblImpacts.setHorizontalHeaderItem(2, item)

        self.retranslateUi(dlgImpacts)
        QtCore.QMetaObject.connectSlotsByName(dlgImpacts)

    def retranslateUi(self, dlgImpacts):
        _translate = QtCore.QCoreApplication.translate
        dlgImpacts.setWindowTitle(_translate("dlgImpacts", "Impacts  table"))
        item = self.tblImpacts.horizontalHeaderItem(0)
        item.setText(_translate("dlgImpacts", "Project"))
        item = self.tblImpacts.horizontalHeaderItem(1)
        item.setText(_translate("dlgImpacts", "Type"))
        item = self.tblImpacts.horizontalHeaderItem(2)
        item.setText(_translate("dlgImpacts", "Distance"))

