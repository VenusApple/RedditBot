# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(626, 701)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 551, 311))
        self.groupBox.setObjectName("groupBox")
        self.label_url = QtWidgets.QLabel(self.groupBox)
        self.label_url.setGeometry(QtCore.QRect(20, 40, 71, 20))
        self.label_url.setObjectName("label_url")
        self.lineEdit_url = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_url.setGeometry(QtCore.QRect(120, 40, 411, 31))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.comboBox_type = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_type.setGeometry(QtCore.QRect(80, 90, 141, 31))
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.label_type = QtWidgets.QLabel(self.groupBox)
        self.label_type.setGeometry(QtCore.QRect(20, 90, 47, 31))
        self.label_type.setObjectName("label_type")
        self.label_count1 = QtWidgets.QLabel(self.groupBox)
        self.label_count1.setGeometry(QtCore.QRect(20, 140, 251, 31))
        self.label_count1.setObjectName("label_count1")
        self.label_number_account = QtWidgets.QLabel(self.groupBox)
        self.label_number_account.setGeometry(QtCore.QRect(20, 200, 231, 21))
        self.label_number_account.setObjectName("label_number_account")
        self.spinBox_vote = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_vote.setGeometry(QtCore.QRect(290, 141, 161, 31))
        self.spinBox_vote.setMaximum(999999)
        self.spinBox_vote.setObjectName("spinBox_vote")
        self.spinBox_account = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_account.setGeometry(QtCore.QRect(290, 200, 161, 31))
        self.spinBox_account.setMaximum(999999)
        self.spinBox_account.setObjectName("spinBox_account")
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_start.setGeometry(QtCore.QRect(150, 260, 241, 41))
        self.pushButton_start.setObjectName("pushButton_start")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 340, 551, 311))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_url_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_url_2.setGeometry(QtCore.QRect(20, 40, 71, 20))
        self.label_url_2.setObjectName("label_url_2")
        self.lineEdit_url_comment = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_url_comment.setGeometry(QtCore.QRect(120, 40, 411, 31))
        self.lineEdit_url_comment.setObjectName("lineEdit_url_comment")
        self.comboBox_type_comment = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_type_comment.setGeometry(QtCore.QRect(80, 90, 141, 31))
        self.comboBox_type_comment.setObjectName("comboBox_type_comment")
        self.comboBox_type_comment.addItem("")
        self.comboBox_type_comment.addItem("")
        self.label_type_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_type_2.setGeometry(QtCore.QRect(20, 90, 47, 31))
        self.label_type_2.setObjectName("label_type_2")
        self.label_count1_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_count1_2.setGeometry(QtCore.QRect(20, 140, 251, 31))
        self.label_count1_2.setObjectName("label_count1_2")
        self.label_number_account_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_number_account_2.setGeometry(QtCore.QRect(20, 200, 231, 21))
        self.label_number_account_2.setObjectName("label_number_account_2")
        self.spinBox_vote_comment = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_vote_comment.setGeometry(QtCore.QRect(290, 141, 161, 31))
        self.spinBox_vote_comment.setMaximum(999999)
        self.spinBox_vote_comment.setObjectName("spinBox_vote_comment")
        self.spinBox_account_comment = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_account_comment.setGeometry(QtCore.QRect(290, 200, 161, 31))
        self.spinBox_account_comment.setMaximum(999999)
        self.spinBox_account_comment.setObjectName("spinBox_account_comment")
        self.pushButton_start_comment = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_start_comment.setGeometry(QtCore.QRect(150, 260, 241, 41))
        self.pushButton_start_comment.setObjectName("pushButton_start_comment")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Post"))
        self.label_url.setText(_translate("Dialog", "Url"))
        self.comboBox_type.setItemText(0, _translate("Dialog", "Up"))
        self.comboBox_type.setItemText(1, _translate("Dialog", "Down"))
        self.label_type.setText(_translate("Dialog", "Type :"))
        self.label_count1.setText(_translate("Dialog", "Count Of Upvote or Downvote :"))
        self.label_number_account.setText(_translate("Dialog", "Number of accounts/windows  : "))
        self.pushButton_start.setText(_translate("Dialog", "Start"))
        self.groupBox_2.setTitle(_translate("Dialog", "Comment"))
        self.label_url_2.setText(_translate("Dialog", "Url"))
        self.comboBox_type_comment.setItemText(0, _translate("Dialog", "Up"))
        self.comboBox_type_comment.setItemText(1, _translate("Dialog", "Down"))
        self.label_type_2.setText(_translate("Dialog", "Type :"))
        self.label_count1_2.setText(_translate("Dialog", "Count Of Upvote or Downvote :"))
        self.label_number_account_2.setText(_translate("Dialog", "Number of accounts/windows  : "))
        self.pushButton_start_comment.setText(_translate("Dialog", "Start"))
