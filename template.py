# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1033, 707)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 16, 972, 621))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.h_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setObjectName("h_layout")
        self.b_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b_button.setObjectName("b_button")
        self.h_layout.addWidget(self.b_button)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.h_layout.addItem(spacerItem)
        self.v_layout = QtWidgets.QVBoxLayout()
        self.v_layout.setObjectName("v_layout")
        self.date_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        self.date_label.setFont(font)
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label.setObjectName("date_label")
        self.v_layout.addWidget(self.date_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.v_layout.addItem(spacerItem1)
        self.g_layout = QtWidgets.QGridLayout()
        self.g_layout.setObjectName("g_layout")
        self.t7_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.t7_label.setFont(font)
        self.t7_label.setObjectName("t7_label")
        self.g_layout.addWidget(self.t7_label, 6, 1, 1, 1)
        self.is_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.is_label.setFont(font)
        self.is_label.setObjectName("is_label")
        self.g_layout.addWidget(self.is_label, 8, 0, 1, 1)
        self.t10_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.t10_label.setFont(font)
        self.t10_label.setObjectName("t10_label")
        self.g_layout.addWidget(self.t10_label, 9, 1, 1, 1)
        self.t9_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.t9_label.setFont(font)
        self.t9_label.setObjectName("t9_label")
        self.g_layout.addWidget(self.t9_label, 8, 1, 1, 1)
        self.aj_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.aj_label.setFont(font)
        self.aj_label.setObjectName("aj_label")
        self.g_layout.addWidget(self.aj_label, 6, 0, 1, 1)
        self.t1_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.t1_label.setFont(font)
        self.t1_label.setObjectName("t1_label")
        self.g_layout.addWidget(self.t1_label, 0, 1, 1, 1)
        self.s_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.s_label.setFont(font)
        self.s_label.setObjectName("s_label")
        self.g_layout.addWidget(self.s_label, 2, 0, 1, 1)
        self.ds_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.ds_label.setFont(font)
        self.ds_label.setObjectName("ds_label")
        self.g_layout.addWidget(self.ds_label, 3, 0, 1, 1)
        self.dj_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.dj_label.setFont(font)
        self.dj_label.setObjectName("dj_label")
        self.g_layout.addWidget(self.dj_label, 4, 0, 1, 1)
        self.t4_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.t4_label.setFont(font)
        self.t4_label.setObjectName("t4_label")
        self.g_layout.addWidget(self.t4_label, 3, 1, 1, 1)
        self.fj_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.fj_label.setFont(font)
        self.fj_label.setObjectName("fj_label")
        self.g_layout.addWidget(self.fj_label, 1, 0, 1, 1)
        self.t2_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.t2_label.setFont(font)
        self.t2_label.setObjectName("t2_label")
        self.g_layout.addWidget(self.t2_label, 1, 1, 1, 1)
        self.t6_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.t6_label.setFont(font)
        self.t6_label.setObjectName("t6_label")
        self.g_layout.addWidget(self.t6_label, 5, 1, 1, 1)
        self.fs_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.fs_label.setFont(font)
        self.fs_label.setObjectName("fs_label")
        self.g_layout.addWidget(self.fs_label, 0, 0, 1, 1)
        self.t3_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.t3_label.setFont(font)
        self.t3_label.setObjectName("t3_label")
        self.g_layout.addWidget(self.t3_label, 2, 1, 1, 1)
        self.m_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.m_label.setFont(font)
        self.m_label.setObjectName("m_label")
        self.g_layout.addWidget(self.m_label, 7, 0, 1, 1)
        self.as_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.as_label.setFont(font)
        self.as_label.setObjectName("as_label")
        self.g_layout.addWidget(self.as_label, 5, 0, 1, 1)
        self.t8_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.t8_label.setFont(font)
        self.t8_label.setObjectName("t8_label")
        self.g_layout.addWidget(self.t8_label, 7, 1, 1, 1)
        self.t5_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.t5_label.setFont(font)
        self.t5_label.setObjectName("t5_label")
        self.g_layout.addWidget(self.t5_label, 4, 1, 1, 1)
        self.ij_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.ij_label.setFont(font)
        self.ij_label.setObjectName("ij_label")
        self.g_layout.addWidget(self.ij_label, 9, 0, 1, 1)
        self.v_layout.addLayout(self.g_layout)
        self.h_layout.addLayout(self.v_layout)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.h_layout.addItem(spacerItem2)
        self.f_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.f_button.setObjectName("f_button")
        self.h_layout.addWidget(self.f_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1033, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setTearOffEnabled(False)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSettigns = QtWidgets.QAction(MainWindow)
        self.actionSettigns.setObjectName("actionSettigns")
        self.actionQuit_2 = QtWidgets.QAction(MainWindow)
        self.actionQuit_2.setObjectName("actionQuit_2")
        self.menuFile.addAction(self.actionSettigns)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_2)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b_button.setText(_translate("MainWindow", "Backwards"))
        self.date_label.setText(_translate("MainWindow", "Date"))
        self.t7_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Time7</p></body></html>"))
        self.is_label.setText(_translate("MainWindow", "Isha Start"))
        self.t10_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Time10</p></body></html>"))
        self.t9_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Time9</p></body></html>"))
        self.aj_label.setText(_translate("MainWindow", "Asr Jamat"))
        self.t1_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Time1</p></body></html>"))
        self.s_label.setText(_translate("MainWindow", "Sunrise"))
        self.ds_label.setText(_translate("MainWindow", "Dhuhr Start"))
        self.dj_label.setText(_translate("MainWindow", "Dhuhr Jamat"))
        self.t4_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Time4</p></body></html>"))
        self.fj_label.setText(_translate("MainWindow", "Fajr Jamat"))
        self.t2_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Time2</p></body></html>"))
        self.t6_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Time6</p></body></html>"))
        self.fs_label.setText(_translate("MainWindow", "Fajr Start"))
        self.t3_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Time3</p></body></html>"))
        self.m_label.setText(_translate("MainWindow", "Maghrib"))
        self.as_label.setText(_translate("MainWindow", "Asr Start"))
        self.t8_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Time8</p></body></html>"))
        self.t5_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Time5</p></body></html>"))
        self.ij_label.setText(_translate("MainWindow", "Isha Jamat"))
        self.f_button.setText(_translate("MainWindow", "Forwards"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionSettigns.setText(_translate("MainWindow", "Settings"))
        self.actionQuit_2.setText(_translate("MainWindow", "Quit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

