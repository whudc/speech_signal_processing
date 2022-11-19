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
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.zh_radioButton = QtWidgets.QRadioButton(self.widget)
        self.zh_radioButton.setChecked(True)
        self.zh_radioButton.setObjectName("zh_radioButton")
        self.horizontalLayout.addWidget(self.zh_radioButton)
        self.en_radioButton = QtWidgets.QRadioButton(self.widget)
        self.en_radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.en_radioButton.setObjectName("en_radioButton")
        self.horizontalLayout.addWidget(self.en_radioButton)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.start_record_train_pushButton = QtWidgets.QPushButton(self.widget1)
        self.start_record_train_pushButton.setObjectName("start_record_train_pushButton")
        self.gridLayout_6.addWidget(self.start_record_train_pushButton, 0, 0, 1, 1)
        self.start_train_pushButton = QtWidgets.QPushButton(self.widget1)
        self.start_train_pushButton.setObjectName("start_train_pushButton")
        self.gridLayout_6.addWidget(self.start_train_pushButton, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 3, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.digital_select_comboBox = QtWidgets.QComboBox(self.widget1)
        self.digital_select_comboBox.setObjectName("digital_select_comboBox")
        self.digital_select_comboBox.addItem("")
        self.digital_select_comboBox.addItem("")
        self.digital_select_comboBox.addItem("")
        self.digital_select_comboBox.addItem("")
        self.digital_select_comboBox.addItem("")
        self.digital_select_comboBox.addItem("")
        self.digital_select_comboBox.addItem("")
        self.digital_select_comboBox.addItem("")
        self.digital_select_comboBox.addItem("")
        self.digital_select_comboBox.addItem("")
        self.gridLayout_3.addWidget(self.digital_select_comboBox, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.digital_sequence_textEdit = QtWidgets.QTextEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digital_sequence_textEdit.sizePolicy().hasHeightForWidth())
        self.digital_sequence_textEdit.setSizePolicy(sizePolicy)
        self.digital_sequence_textEdit.setObjectName("digital_sequence_textEdit")
        self.gridLayout_4.addWidget(self.digital_sequence_textEdit, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_8, 0, 0, 1, 2)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)
        self.machine_learning_result_textBrowser = QtWidgets.QTextBrowser(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_learning_result_textBrowser.sizePolicy().hasHeightForWidth())
        self.machine_learning_result_textBrowser.setSizePolicy(sizePolicy)
        self.machine_learning_result_textBrowser.setObjectName("machine_learning_result_textBrowser")
        self.gridLayout_9.addWidget(self.machine_learning_result_textBrowser, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 1, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_9, 1, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.deep_learning_result_textBrowser = QtWidgets.QTextBrowser(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deep_learning_result_textBrowser.sizePolicy().hasHeightForWidth())
        self.deep_learning_result_textBrowser.setSizePolicy(sizePolicy)
        self.deep_learning_result_textBrowser.setObjectName("deep_learning_result_textBrowser")
        self.gridLayout_10.addWidget(self.deep_learning_result_textBrowser, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_10.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_10.addWidget(self.label_7, 1, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_10, 2, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.start_record_test_pushButton = QtWidgets.QPushButton(self.widget_2)
        self.start_record_test_pushButton.setObjectName("start_record_test_pushButton")
        self.gridLayout_12.addWidget(self.start_record_test_pushButton, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_12, 3, 0, 1, 2)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.ml_radioButton = QtWidgets.QRadioButton(self.widget_2)
        self.ml_radioButton.setChecked(True)
        self.ml_radioButton.setObjectName("ml_radioButton")
        self.gridLayout_11.addWidget(self.ml_radioButton, 0, 0, 1, 1)
        self.dl_radioButton = QtWidgets.QRadioButton(self.widget_2)
        self.dl_radioButton.setObjectName("dl_radioButton")
        self.gridLayout_11.addWidget(self.dl_radioButton, 1, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_11, 1, 1, 2, 1)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.single_digital_radioButton = QtWidgets.QRadioButton(self.widget_3)
        self.single_digital_radioButton.setChecked(True)
        self.single_digital_radioButton.setObjectName("single_digital_radioButton")
        self.gridLayout_14.addWidget(self.single_digital_radioButton, 0, 0, 1, 1)
        self.digital_sequence_radioButton = QtWidgets.QRadioButton(self.widget_3)
        self.digital_sequence_radioButton.setObjectName("digital_sequence_radioButton")
        self.gridLayout_14.addWidget(self.digital_sequence_radioButton, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.widget_3, 2, 0, 1, 1)
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
        self.zh_radioButton.setText(_translate("MainWindow", "中文"))
        self.en_radioButton.setText(_translate("MainWindow", "英文"))
        self.label.setText(_translate("MainWindow", "Train"))
        self.start_record_train_pushButton.setText(_translate("MainWindow", "录制声音"))
        self.start_train_pushButton.setText(_translate("MainWindow", "开始训练"))
        self.digital_select_comboBox.setItemText(0, _translate("MainWindow", "0"))
        self.digital_select_comboBox.setItemText(1, _translate("MainWindow", "1"))
        self.digital_select_comboBox.setItemText(2, _translate("MainWindow", "2"))
        self.digital_select_comboBox.setItemText(3, _translate("MainWindow", "3"))
        self.digital_select_comboBox.setItemText(4, _translate("MainWindow", "4"))
        self.digital_select_comboBox.setItemText(5, _translate("MainWindow", "5"))
        self.digital_select_comboBox.setItemText(6, _translate("MainWindow", "6"))
        self.digital_select_comboBox.setItemText(7, _translate("MainWindow", "7"))
        self.digital_select_comboBox.setItemText(8, _translate("MainWindow", "8"))
        self.digital_select_comboBox.setItemText(9, _translate("MainWindow", "9"))
        self.label_8.setText(_translate("MainWindow", "请选择录制的数字："))
        self.label_2.setText(_translate("MainWindow", "请输入录制的序列："))
        self.label_3.setText(_translate("MainWindow", "Test"))
        self.label_4.setText(_translate("MainWindow", "Machine Learning"))
        self.label_6.setText(_translate("MainWindow", "检测结果为："))
        self.label_5.setText(_translate("MainWindow", "Deep Learning"))
        self.label_7.setText(_translate("MainWindow", "检测结果为："))
        self.start_record_test_pushButton.setText(_translate("MainWindow", "录制声音"))
        self.ml_radioButton.setText(_translate("MainWindow", "机器学习"))
        self.dl_radioButton.setText(_translate("MainWindow", "深度学习"))
        self.single_digital_radioButton.setText(_translate("MainWindow", "单个数字"))
        self.digital_sequence_radioButton.setText(_translate("MainWindow", "数字序列"))
