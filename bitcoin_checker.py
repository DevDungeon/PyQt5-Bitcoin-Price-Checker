import requests
import sys
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow


class FetchPrice(QThread):
    done_signal = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        data = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json').json()
        price = data['bpi']['USD']['rate']
        self.done_signal.emit(price)


class RealMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create fetch thread
        self.thread = FetchPrice()

        # Connect signals
        self.ui.priceCheckButton.clicked.connect(self.update_price)

    def update_price(self):
        print('Updating price')
        self.ui.priceCheckButton.setEnabled(False)
        self.thread.done_signal.connect(self.price_fetched)
        self.thread.start()

    def price_fetched(self, result):
        self.ui.bitcoinPriceLabel.setText('$%s' % result)
        self.ui.priceCheckButton.setEnabled(True)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    real_main_window = RealMainWindow()
    real_main_window.show()
    sys.exit(app.exec_())

