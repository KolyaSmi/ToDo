import sys
from PyQt6 import QtCore, QtGui, QtWidgets

from functions import functions, config
from interfase.MainWindow import Ui_MainWindow
from interfase.Add_window import Add_Box


class ToDo(QtWidgets.QMainWindow):
    def __init__(self):
        super(ToDo, self).__init__()
        config.affairs = functions.initJson()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.repaint_Box()

        self.init_buttons()

    def init_buttons(self):
        self.ui.addButton.clicked.connect(lambda: self.new_affairs_window())
        self.ui.sortPrior.clicked.connect(lambda: functions.sort_button_on(self.ui, 1))
        self.ui.sortData.clicked.connect(lambda: functions.sort_button_on(self.ui, 2))
        self.ui.sortName.clicked.connect(lambda: functions.sort_button_on(self.ui, 3))

    def new_affairs_window(self):
        add = Add_Box(self)

        add.button_add.clicked.connect(lambda: {self.button_add_cliched(add)})

        add.exec()

    def button_add_cliched(self, add):
        config.affairs = functions.update_json()
        if add.checkRegulations():
            if add.priority_1.isChecked():
                add.priority = 1
            if add.priority_2.isChecked():
                add.priority = 2
            if add.priority_3.isChecked():
                add.priority = 3
            config.affairs = functions.new_affairs_json(config.affairs, add.name.toPlainText(), add.text.toPlainText(),
                                                        add.data.toPlainText(), add.priority)
            self.ui.add_affairs(self, config.affairs["affairs"][config.num_add + 1])
            add.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ToDo()
    window.show()

    sys.exit(app.exec())

#python -m PyQt6.uic.pyuic -x MainWindow.ui -o ./interfase/MainWindow.py