from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtCore import pyqtSlot, QObject
from main_window import Ui_MainWindow


app = QtWidgets.QApplication(sys.argv)




# class MainSub(Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#






# Main windows
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


sys.exit(app.exec_())
