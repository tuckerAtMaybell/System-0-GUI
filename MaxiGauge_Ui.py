# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\TuckerVana\PycharmProjects\GUI Project 2.0\PyGMI-master\PyGMI_files\Instruments_panels\MaxiGauge.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Panel(object):
    def setupUi(self, Panel):
        # print("frigg in setupUI")
        Panel.setObjectName("Panel")
        Panel.resize(592, 568)
        self.gridLayout = QtWidgets.QGridLayout(Panel)
        self.gridLayout.setObjectName("gridLayout")
        self.monitor = QtWidgets.QCheckBox(Panel)
        self.monitor.setCheckable(True)
        self.monitor.setChecked(False)
        self.monitor.setObjectName("monitor")
        self.gridLayout.addWidget(self.monitor, 0, 0, 1, 1)
        self.f_disp = QtWidgets.QLabel(Panel)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.f_disp.setFont(font)
        self.f_disp.setAutoFillBackground(False)
        self.f_disp.setStyleSheet("background-color: rgb(0, 1, 0);\n"
"color: rgb(250, 28, 51);")
        self.f_disp.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.f_disp.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.f_disp.setScaledContents(False)
        self.f_disp.setAlignment(QtCore.Qt.AlignCenter)
        self.f_disp.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.f_disp.setObjectName("f_disp")
        self.gridLayout.addWidget(self.f_disp, 0, 1, 1, 1)
        self.label_47 = QtWidgets.QLabel(Panel)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.gridLayout.addWidget(self.label_47, 1, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(Panel)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 1, 1, 1, 1)
        self.refresh_rate = QtWidgets.QDoubleSpinBox(Panel)
        self.refresh_rate.setMinimumSize(QtCore.QSize(91, 0))
        self.refresh_rate.setAlignment(QtCore.Qt.AlignCenter)
        self.refresh_rate.setDecimals(1)
        self.refresh_rate.setMaximum(9999999.0)
        self.refresh_rate.setSingleStep(0.5)
        self.refresh_rate.setProperty("value", 2.0)
        self.refresh_rate.setObjectName("refresh_rate")
        self.gridLayout.addWidget(self.refresh_rate, 2, 0, 1, 1)
        self.f_disp_2 = QtWidgets.QLabel(Panel)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.f_disp_2.setFont(font)
        self.f_disp_2.setAutoFillBackground(False)
        self.f_disp_2.setStyleSheet("background-color: rgb(0, 1, 0);\n"
"color: rgb(250, 28, 51);")
        self.f_disp_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.f_disp_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.f_disp_2.setScaledContents(False)
        self.f_disp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.f_disp_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.f_disp_2.setObjectName("f_disp_2")
        self.gridLayout.addWidget(self.f_disp_2, 2, 1, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Panel)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 3, 1, 1, 1)
        self.f_disp_3 = QtWidgets.QLabel(Panel)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.f_disp_3.setFont(font)
        self.f_disp_3.setAutoFillBackground(False)
        self.f_disp_3.setStyleSheet("background-color: rgb(0, 1, 0);\n"
"color: rgb(250, 28, 51);")
        self.f_disp_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.f_disp_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.f_disp_3.setScaledContents(False)
        self.f_disp_3.setAlignment(QtCore.Qt.AlignCenter)
        self.f_disp_3.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.f_disp_3.setObjectName("f_disp_3")
        self.gridLayout.addWidget(self.f_disp_3, 4, 1, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Panel)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 5, 1, 1, 1)
        self.f_disp_4 = QtWidgets.QLabel(Panel)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.f_disp_4.setFont(font)
        self.f_disp_4.setAutoFillBackground(False)
        self.f_disp_4.setStyleSheet("background-color: rgb(0, 1, 0);\n"
"color: rgb(250, 28, 51);")
        self.f_disp_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.f_disp_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.f_disp_4.setScaledContents(False)
        self.f_disp_4.setAlignment(QtCore.Qt.AlignCenter)
        self.f_disp_4.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.f_disp_4.setObjectName("f_disp_4")
        self.gridLayout.addWidget(self.f_disp_4, 6, 1, 1, 1)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(Panel)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout.addWidget(self.lcdNumber_4, 7, 1, 1, 1)
        self.f_disp_5 = QtWidgets.QLabel(Panel)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.f_disp_5.setFont(font)
        self.f_disp_5.setAutoFillBackground(False)
        self.f_disp_5.setStyleSheet("background-color: rgb(0, 1, 0);\n"
"color: rgb(250, 28, 51);")
        self.f_disp_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.f_disp_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.f_disp_5.setScaledContents(False)
        self.f_disp_5.setAlignment(QtCore.Qt.AlignCenter)
        self.f_disp_5.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.f_disp_5.setObjectName("f_disp_5")
        self.gridLayout.addWidget(self.f_disp_5, 8, 1, 1, 1)
        self.lcdNumber_5 = QtWidgets.QLCDNumber(Panel)
        self.lcdNumber_5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.gridLayout.addWidget(self.lcdNumber_5, 9, 1, 1, 1)
        self.f_disp_6 = QtWidgets.QLabel(Panel)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.f_disp_6.setFont(font)
        self.f_disp_6.setAutoFillBackground(False)
        self.f_disp_6.setStyleSheet("background-color: rgb(0, 1, 0);\n"
"color: rgb(250, 28, 51);")
        self.f_disp_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.f_disp_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.f_disp_6.setScaledContents(False)
        self.f_disp_6.setAlignment(QtCore.Qt.AlignCenter)
        self.f_disp_6.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.f_disp_6.setObjectName("f_disp_6")
        self.gridLayout.addWidget(self.f_disp_6, 10, 1, 1, 1)
        self.lcdNumber_6 = QtWidgets.QLCDNumber(Panel)
        self.lcdNumber_6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.gridLayout.addWidget(self.lcdNumber_6, 11, 1, 1, 1)

        self.retranslateUi(Panel)
        self.refresh_rate.valueChanged['QString'].connect(Panel.update_timer_timeout) # type: ignore
        self.monitor.stateChanged['int'].connect(Panel.monitor) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Panel)

    def retranslateUi(self, Panel):
        _translate = QtCore.QCoreApplication.translate
        Panel.setWindowTitle(_translate("Panel", "MaxiGauge"))
        self.monitor.setText(_translate("Panel", "Monitor"))
        self.f_disp.setText(_translate("Panel", "Pressure Sensor 1"))
        self.label_47.setText(_translate("Panel", "Refresh rate"))
        self.refresh_rate.setSuffix(_translate("Panel", " secs"))
        self.f_disp_2.setText(_translate("Panel", "Pressure Sensor 2"))
        self.f_disp_3.setText(_translate("Panel", "Pressure Sensor 3"))
        self.f_disp_4.setText(_translate("Panel", "Pressure Sensor 4"))
        self.f_disp_5.setText(_translate("Panel", "Pressure Sensor 5"))
        self.f_disp_6.setText(_translate("Panel", "Pressure Sensor 6"))
