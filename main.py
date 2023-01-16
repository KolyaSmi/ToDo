import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialogButtonBox

from functions import functions, config
from interfase.MainWindow import Ui_MainWindow
from interfase.Add_window import Add_Box
from interfase.Edit_window import Edit_Box


class ToDo(QtWidgets.QMainWindow):
    def __init__(self):
        super(ToDo, self).__init__()
        config.affairs = functions.initJson()
        config.affairs_story = functions.init_story_json()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.repaint_Box()
        self.ui.add_story()

        self.init_buttons()

    def init_buttons(self):
        self.ui.addButton.clicked.connect(lambda: self.new_affairs_window())
        self.ui.sortPrior.clicked.connect(lambda: self.sort_button_on(1))
        self.ui.sortData.clicked.connect(lambda: self.sort_button_on(2))
        self.ui.sortName.clicked.connect(lambda: self.sort_button_on(3))
        self.ui.buttonStory.clicked.connect(lambda: self.button_story_on())
        self.ui.del_button_story.clicked.connect(lambda: self.dialog_window())

    def new_affairs_window(self):
        add = Add_Box(self)

        add.button_add.clicked.connect(lambda: {self.button_add_cliched(add)})

        add.exec()

    def button_add_cliched(self, add):
        if add.checkRegulations():
            if add.priority_1.isChecked():
                add.priority = 1
            if add.priority_2.isChecked():
                add.priority = 2
            if add.priority_3.isChecked():
                add.priority = 3
            config.affairs = functions.new_affairs_json(config.affairs, add.name.toPlainText(), add.text.toPlainText(),
                                                        add.data.toPlainText(), add.priority)
            if config.sort_id == 1:
                config.affairs = functions.sort_json_prior()
            if config.sort_id == 2:
                config.affairs = functions.sort_json_data()
            if config.sort_id == 3:
                config.affairs = functions.sort_json_name()
            self.ui.repaint_Box()
            add.close()

    def sort_button_on(self, n):
        if n == 1:
            functions.sort_json_prior()
            self.ui.repaint_Box()
            self.ui.sortPrior.setChecked(True)
            self.ui.sortData.setChecked(False)
            self.ui.sortName.setChecked(False)
        if n == 2:
            functions.sort_json_data()
            self.ui.repaint_Box()
            self.ui.sortPrior.setChecked(False)
            self.ui.sortData.setChecked(True)
            self.ui.sortName.setChecked(False)
        if n == 3:
            functions.sort_json_name()
            self.ui.repaint_Box()
            self.ui.sortPrior.setChecked(False)
            self.ui.sortData.setChecked(False)
            self.ui.sortName.setChecked(True)
        config.sort_id = n

    def button_story_on(self):
        if config.status_button_story:
            self.ui.addButton.setVisible(True)
            self.ui.del_button_story.setVisible(False)
            self.ui.sortName.setVisible(True)
            self.ui.sortData.setVisible(True)
            self.ui.sortPrior.setVisible(True)
            self.ui.show_affairs()
            self.ui.hide_story()
            config.status_button_story = False
        else:
            self.ui.addButton.setVisible(False)
            self.ui.del_button_story.setVisible(True)
            self.ui.sortName.setVisible(False)
            self.ui.sortData.setVisible(False)
            self.ui.sortPrior.setVisible(False)
            self.ui.hide_affairs()
            self.ui.show_story()
            config.status_button_story = True

    def dialog_window(self):
        massage = QtWidgets.QDialog()

        massage.setWindowTitle("Удаление")
        massage.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Yes | QDialogButtonBox.StandardButton.No)
        massage.buttonBox.accepted.connect(lambda: self.del_accept(massage))
        massage.buttonBox.rejected.connect(lambda: self.close_dialog(massage))

        massage.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel("Вы действительно хотите очистить историю?")
        massage.layout.addWidget(message)
        massage.layout.addWidget(massage.buttonBox)
        massage.setLayout(massage.layout)

        massage.exec()

    def close_dialog(self, massage):
        massage.close()

    def del_accept(self, massage):
        self.ui.del_story()
        functions.del_story_json()
        massage.close()

    def edit_affair(self, edit):
        if edit.checkRegulations():
            if edit.priority_1.isChecked():
                edit.priority = 1
            if edit.priority_2.isChecked():
                edit.priority = 2
            if edit.priority_3.isChecked():
                edit.priority = 3


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ToDo()
    window.show()

    sys.exit(app.exec())

#python -m PyQt6.uic.pyuic -x MainWindow.ui -o ./interfase/MainWindow.py