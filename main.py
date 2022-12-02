# from interfase import MainWindow
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from interfase.MainWindow import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.main = Ui_MainWindow()
        self.main.setupUi(self)
        self.main.createPoint(self)
        self.main.createPoint(self)


app = QtWidgets.QApplication(sys.argv)
application = CurrencyConv()
application.show()

sys.exit(app.exec())

#python -m PyQt6.uic.pyuic -x MainWindow.ui -o ./interfase/MainWindow.py