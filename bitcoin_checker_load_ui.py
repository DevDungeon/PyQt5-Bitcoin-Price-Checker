import requests
import sys
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic


class FetchPrice(QThread):

    done_signal = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        data = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json').json()
        price = data['bpi']['USD']['rate']
        self.done_signal.emit(price)


class RealMainWindow:
    def __init__(self):

        # Setup ui
        self.ui = uic.loadUi("templates/main_window.ui")

        # Create fetch thread
        self.thread = FetchPrice()

        # Connect signals
        self.ui.priceCheckButton.clicked.connect(self.update_price)

    def update_price(self):
        print('Updating price')
        self.ui.priceCheckButton.setEnabled(False)
        self.thread.start()
        self.thread.done_signal.connect(self.price_fetched)

    def price_fetched(self, result):
        self.ui.bitcoinPriceLabel.setText('$%s' % result)
        self.ui.priceCheckButton.setEnabled(True)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    real_main_window = RealMainWindow()
    real_main_window.ui.show()
    sys.exit(app.exec_())

