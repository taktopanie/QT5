# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kontrola_arduino.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 489)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(310, 30, 421, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.Kontrola_diod_check = QtWidgets.QCheckBox(self.frame)
        self.Kontrola_diod_check.setGeometry(QtCore.QRect(10, 10, 121, 23))
        self.Kontrola_diod_check.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Kontrola_diod_check.setAutoFillBackground(False)
        self.Kontrola_diod_check.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Kontrola_diod_check.setChecked(False)
        self.Kontrola_diod_check.setObjectName("Kontrola_diod_check")
        
        self.Dioda1_widget = QtWidgets.QWidget(self.frame)
        self.Dioda1_widget.setGeometry(QtCore.QRect(30, 40, 101, 121))
        self.Dioda1_widget.setObjectName("Dioda1_widget")
        
        self.Button_OFF_Dioda1 = QtWidgets.QRadioButton(self.Dioda1_widget)
        self.Button_OFF_Dioda1.setGeometry(QtCore.QRect(10, 80, 112, 23))
        self.Button_OFF_Dioda1.setChecked(False)
        self.Button_OFF_Dioda1.setObjectName("Button_OFF_Dioda1")
        self.Button_ON_Dioda1 = QtWidgets.QRadioButton(self.Dioda1_widget)
        self.Button_ON_Dioda1.setGeometry(QtCore.QRect(10, 40, 112, 23))
        self.Button_ON_Dioda1.setObjectName("Button_ON_Dioda1")
        
        self.Label_Dioda1 = QtWidgets.QLabel(self.Dioda1_widget)
        self.Label_Dioda1.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.Label_Dioda1.setObjectName("Label_Dioda1")
        
        self.Dioda2_widget = QtWidgets.QWidget(self.frame)
        self.Dioda2_widget.setGeometry(QtCore.QRect(160, 40, 101, 121))
        self.Dioda2_widget.setObjectName("Dioda2_widget")
        
        self.Button_OFF_Dioda2 = QtWidgets.QRadioButton(self.Dioda2_widget)
        self.Button_OFF_Dioda2.setGeometry(QtCore.QRect(10, 80, 112, 23))
        self.Button_OFF_Dioda2.setChecked(False)
        self.Button_OFF_Dioda2.setObjectName("Button_OFF_Dioda2")
        
        self.Button_ON_Dioda2 = QtWidgets.QRadioButton(self.Dioda2_widget)
        self.Button_ON_Dioda2.setGeometry(QtCore.QRect(10, 40, 112, 23))
        self.Button_ON_Dioda2.setObjectName("Button_ON_Dioda2")
        
        self.Label_Dioda2 = QtWidgets.QLabel(self.Dioda2_widget)
        self.Label_Dioda2.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.Label_Dioda2.setObjectName("Label_Dioda2")
        
        self.Dioda3_widget = QtWidgets.QWidget(self.frame)
        self.Dioda3_widget.setGeometry(QtCore.QRect(290, 40, 101, 121))
        self.Dioda3_widget.setObjectName("Dioda3_widget")
        
        self.Button_OFF_Dioda3 = QtWidgets.QRadioButton(self.Dioda3_widget)
        self.Button_OFF_Dioda3.setGeometry(QtCore.QRect(10, 80, 112, 23))
        self.Button_OFF_Dioda3.setChecked(False)
        self.Button_OFF_Dioda3.setObjectName("Button_OFF_Dioda3")
        
        self.Button_ON_Dioda3 = QtWidgets.QRadioButton(self.Dioda3_widget)
        self.Button_ON_Dioda3.setGeometry(QtCore.QRect(10, 40, 112, 23))
        self.Button_ON_Dioda3.setObjectName("Button_ON_Dioda3")
        
        self.Label_Dioda3 = QtWidgets.QLabel(self.Dioda3_widget)
        self.Label_Dioda3.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.Label_Dioda3.setObjectName("Label_Dioda3")
        
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(310, 240, 421, 191))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(290, 110, 111, 51))
        self.pushButton.setObjectName("pushButton")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 50, 171, 81))
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 131, 17))
        self.label_2.setObjectName("label_2")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 251, 131))
        self.label.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 22))
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
        self.Kontrola_diod_check.setText(_translate("MainWindow", "Kontrola diod"))
        self.Button_OFF_Dioda1.setText(_translate("MainWindow", "OFF"))
        self.Button_ON_Dioda1.setText(_translate("MainWindow", "ON"))
        self.Label_Dioda1.setText(_translate("MainWindow", "Dioda 1"))
        self.Button_OFF_Dioda2.setText(_translate("MainWindow", "OFF"))
        self.Button_ON_Dioda2.setText(_translate("MainWindow", "ON"))
        self.Label_Dioda2.setText(_translate("MainWindow", "Dioda 2"))
        self.Button_OFF_Dioda3.setText(_translate("MainWindow", "OFF"))
        self.Button_ON_Dioda3.setText(_translate("MainWindow", "ON"))
        self.Label_Dioda3.setText(_translate("MainWindow", "Dioda 3"))
        self.pushButton.setText(_translate("MainWindow", "Pomiar\n"
"napięcia"))
        self.label_2.setText(_translate("MainWindow", "Wartość napięcia :"))
        self.label.setText(_translate("MainWindow", "Interfejs główny"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

