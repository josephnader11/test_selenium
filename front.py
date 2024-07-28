# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 491)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 791, 491))
        self.tabWidget.setStyleSheet("QWidget {\n"
"    background-color: #2e2e2e;\n"
"    color: #f0f0f0;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #4caf50;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 14px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #f0f0f0;\n"
"    font-size: 40px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border-top: 2px solid #4caf50;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #2e2e2e;\n"
"    color: #f0f0f0;\n"
"    padding: 10px;\n"
"    border: 1px solid #4caf50;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #4caf50;\n"
"    color: white;\n"
"}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(260, 290, 251, 45))
        self.label_3.setStyleSheet("QLabel {\n"
"    color: #f0f0f0;\n"
"    font-size: 10px;\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(470, 170, 251, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.run_Button = QtWidgets.QPushButton(self.tab)
        self.run_Button.setGeometry(QtCore.QRect(70, 320, 131, 44))
        self.run_Button.setObjectName("run_Button")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(200, 40, 265, 100))
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.browse_btn = QtWidgets.QPushButton(self.tab)
        self.browse_btn.setGeometry(QtCore.QRect(70, 260, 131, 40))
        self.browse_btn.setMaximumSize(QtCore.QSize(200, 40))
        self.browse_btn.setStyleSheet("")
        self.browse_btn.setObjectName("browse_btn")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plotting Tool"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.run_Button.setText(_translate("MainWindow", "Run"))
        self.label.setText(_translate("MainWindow", "HTML To Excel"))
        self.browse_btn.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Email"))
