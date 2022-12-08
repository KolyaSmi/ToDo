import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon

import functions.functions
from interfase.MainWindow import Ui_MainWindow, Add_Box


class ToDo(QtWidgets.QMainWindow):
    def __init__(self):
        super(ToDo, self).__init__()
        num_aff = -1
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.affairs = functions.functions.initJson()

        if self.affairs != None:
            for x in self.affairs["affairs"]:
                self.ui.add_affairs(self, x)
                num_aff += 1

        self.ui.addButton.clicked.connect(lambda: self.new_affairs(num_aff))

    def new_affairs(self, num_aff):
        add = Add_Box(self)
        num_aff += 1
        add.exec()
        # self.affairs = functions.functions.new_affairs_json(self.affairs, "дело 4", "Нужно делать", "10.11.2022", 1)
        # self.ui.add_affairs(self, self.affairs["affairs"][num_aff])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ToDo()
    window.show()

    sys.exit(app.exec())

#python -m PyQt6.uic.pyuic -x MainWindow.ui -o ./interfase/MainWindow.py