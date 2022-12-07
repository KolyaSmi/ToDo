import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon

import functions.functions
from interfase.MainWindow import Ui_MainWindow


class ToDo(QtWidgets.QMainWindow):
    def __init__(self):
        super(ToDo, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.affairs = functions.functions.initJson()
        for x in self.affairs:
            self.ui.add_affairs(self, x)
        self.ui.addButton.clicked.connect(lambda: self.new_affairs())

    # def new_affairs(self):
        # functions.functions.
        # self.ui.add_affairs(self, self.affairs)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ToDo()
    window.show()

    sys.exit(app.exec())

#python -m PyQt6.uic.pyuic -x MainWindow.ui -o ./interfase/MainWindow.py