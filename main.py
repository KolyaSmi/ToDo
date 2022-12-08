import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon

import functions.functions
from interfase.MainWindow import Ui_MainWindow, Add_Box


class ToDo(QtWidgets.QMainWindow):
    def __init__(self):
        super(ToDo, self).__init__()
        self.num_aff = -1
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.affairs = functions.functions.initJson()

        if self.affairs != None:
            for x in self.affairs["affairs"]:
                self.ui.add_affairs(self, x)
                self.num_aff += 1

        self.ui.addButton.clicked.connect(lambda: self.new_affairs())

    def new_affairs(self):
        add = Add_Box(self)

        add.button_add.clicked.connect(lambda: {self.new_json(add)})

        add.exec()


    def new_json(self, add):
        if add.priority_1.isChecked():
            add.priority = 1
        if add.priority_2.isChecked():
            add.priority = 2
        if add.priority_3.isChecked():
            add.priority = 3
        self.affairs = functions.functions.new_affairs_json(self.affairs, add.name.toPlainText(), add.text.toPlainText(),
                                                            add.data.toPlainText(), add.priority)
        self.num_aff += 1
        self.ui.add_affairs(self, self.affairs["affairs"][self.num_aff])
        add.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ToDo()
    window.show()

    sys.exit(app.exec())

#python -m PyQt6.uic.pyuic -x MainWindow.ui -o ./interfase/MainWindow.py