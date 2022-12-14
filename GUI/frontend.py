# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui/frontend.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1164, 822)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.gridLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.zh_radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.zh_radioButton.setChecked(True)
        self.zh_radioButton.setObjectName("zh_radioButton")
        self.gridLayout.addWidget(self.zh_radioButton, 1, 0, 1, 1)
        self.en_radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.en_radioButton.setObjectName("en_radioButton")
        self.gridLayout.addWidget(self.en_radioButton, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 2)
        self.single_radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.single_radioButton.setChecked(True)
        self.single_radioButton.setObjectName("single_radioButton")
        self.gridLayout_2.addWidget(self.single_radioButton, 1, 0, 1, 1)
        self.seq_radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.seq_radioButton.setObjectName("seq_radioButton")
        self.gridLayout_2.addWidget(self.seq_radioButton, 1, 1, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.splitter_2)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.result_textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget_3)
        self.result_textBrowser.setObjectName("result_textBrowser")
        self.gridLayout_3.addWidget(self.result_textBrowser, 1, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.splitter_2)
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.recognition_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.recognition_pushButton.setObjectName("recognition_pushButton")
        self.gridLayout_6.addWidget(self.recognition_pushButton, 1, 0, 1, 1)
        self.record_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.record_pushButton.setObjectName("record_pushButton")
        self.gridLayout_6.addWidget(self.record_pushButton, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.splitter_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1164, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.zh_radioButton.setText(_translate("MainWindow", "??????"))
        self.en_radioButton.setText(_translate("MainWindow", "??????"))
        self.label_2.setText(_translate("MainWindow", "??????????????????????????????"))
        self.label_3.setText(_translate("MainWindow", "????????????????????????????????????"))
        self.single_radioButton.setText(_translate("MainWindow", "????????????"))
        self.seq_radioButton.setText(_translate("MainWindow", "????????????"))
        self.label.setText(_translate("MainWindow", "??????????????????"))
        self.recognition_pushButton.setText(_translate("MainWindow", "????????????"))
        self.record_pushButton.setText(_translate("MainWindow", "????????????"))
