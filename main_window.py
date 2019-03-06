# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import requests as requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal


class FetchPrice(QThread):
    done_signal = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        data = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json').json()
        price = data['bpi']['USD']['rate']
        self.done_signal.emit(price)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(299, 183)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.priceCheckButton = QtWidgets.QPushButton(self.centralwidget)
        self.priceCheckButton.setGeometry(QtCore.QRect(80, 70, 89, 25))
        self.priceCheckButton.setObjectName("priceCheckButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 21))
        self.label.setObjectName("label")
        self.bitcoinPriceLabel = QtWidgets.QLabel(self.centralwidget)
        self.bitcoinPriceLabel.setGeometry(QtCore.QRect(160, 20, 67, 17))
        self.bitcoinPriceLabel.setObjectName("bitcoinPriceLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 299, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.priceCheckButton.clicked.connect(self.update_price)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def update_price(self):
        thread = FetchPrice()
        thread.done_signal.connect(self.price_fetched)
        thread.start()
        thread.wait()

    def price_fetched(self, result):
        self.bitcoinPriceLabel.setText('$%s' % result)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.priceCheckButton.setText(_translate("MainWindow", "Check Price"))
        self.label.setText(_translate("MainWindow", "Bitcoin Price (USD): "))
        self.bitcoinPriceLabel.setText(_translate("MainWindow", "N/A"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
