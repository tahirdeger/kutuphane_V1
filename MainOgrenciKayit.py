# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainOgrenciKayit.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainOgernciKayit(object):
    def setupUi(self, MainOgernciKayit):
        MainOgernciKayit.setObjectName("MainOgernciKayit")
        MainOgernciKayit.resize(461, 194)
        self.centralwidget = QtWidgets.QWidget(MainOgernciKayit)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbl_no = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lbl_no.setFont(font)
        self.lbl_no.setObjectName("lbl_no")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_no)
        self.txt_no = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_no.setFont(font)
        self.txt_no.setObjectName("txt_no")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_no)
        self.lbl_ogrenciadi = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lbl_ogrenciadi.setFont(font)
        self.lbl_ogrenciadi.setObjectName("lbl_ogrenciadi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_ogrenciadi)
        self.txt_ogrenciadi = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_ogrenciadi.setFont(font)
        self.txt_ogrenciadi.setObjectName("txt_ogrenciadi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_ogrenciadi)
        self.lbl_ogrencisoyadi = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.lbl_ogrencisoyadi.setFont(font)
        self.lbl_ogrencisoyadi.setObjectName("lbl_ogrencisoyadi")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_ogrencisoyadi)
        self.txt_ogrencisoyadi = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_ogrencisoyadi.setFont(font)
        self.txt_ogrencisoyadi.setObjectName("txt_ogrencisoyadi")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_ogrencisoyadi)
        self.btn_tamam = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tamam.setGeometry(QtCore.QRect(70, 120, 141, 31))
        self.btn_tamam.setObjectName("btn_tamam")
        self.btn_iptal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_iptal.setGeometry(QtCore.QRect(230, 120, 141, 31))
        self.btn_iptal.setObjectName("btn_iptal")
        MainOgernciKayit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainOgernciKayit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 21))
        self.menubar.setObjectName("menubar")
        MainOgernciKayit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainOgernciKayit)
        self.statusbar.setObjectName("statusbar")
        MainOgernciKayit.setStatusBar(self.statusbar)

        self.retranslateUi(MainOgernciKayit)
        QtCore.QMetaObject.connectSlotsByName(MainOgernciKayit)

    def retranslateUi(self, MainOgernciKayit):
        _translate = QtCore.QCoreApplication.translate
        MainOgernciKayit.setWindowTitle(_translate("MainOgernciKayit", "Öğrenci kayıt bilgileri"))
        self.lbl_no.setText(_translate("MainOgernciKayit", "Öğrencinin numarası"))
        self.lbl_ogrenciadi.setText(_translate("MainOgernciKayit", "Öğrencinin adı"))
        self.lbl_ogrencisoyadi.setText(_translate("MainOgernciKayit", "Öğrencinin soyadı"))
        self.btn_tamam.setText(_translate("MainOgernciKayit", "Kaydet"))
        self.btn_iptal.setText(_translate("MainOgernciKayit", "İptal"))
