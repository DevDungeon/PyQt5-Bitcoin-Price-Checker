import requests
from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QMainWindow
from main_window import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)


class FetchPrice(QThread):
    done_signal = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        data = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json').json()
        price = data['bpi']['USD']['rate']
        self.done_signal.emit(price)


class RealMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup_slots(self):
        self.priceCheckButton.clicked.connect(self.update_price)

    def update_price(self):
        print('Updating price')
        thread = FetchPrice()
        thread.done_signal.connect(self.price_fetched)
        thread.start()
        thread.wait()

    def price_fetched(self, result):
        self.bitcoinPriceLabel.setText('$%s' % result)


if __name__ == '__main__':
    MainWindow = QtWidgets.QMainWindow()

    ui = RealMainWindow()
    ui.setupUi(MainWindow)
    ui.setup_slots()
    MainWindow.show()

    sys.exit(app.exec_())
