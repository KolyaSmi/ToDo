import re

from PyQt6 import QtCore, QtGui, QtWidgets

from functions import functions, config

class Add_Box (QtWidgets.QDialog):
    def __init__(self, parent= None):
        super(Add_Box, self).__init__(parent)

        self.priority = 1

        self.resize(762, 263)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.bg = QtWidgets.QFrame(self)
        self.bg.setGeometry(QtCore.QRect(0, 0, 762, 263))
        self.bg.setStyleSheet("background-image: url(resources/bg_1_add.png);")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 762, 263))
        self.frame.setEnabled(True)
        self.frame.setStyleSheet("background-color: rgba(249, 249, 249, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        self.name = QtWidgets.QTextEdit(self.frame)
        self.name.setGeometry(QtCore.QRect(133, 20, 429, 31))
        self.name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.name.setStyleSheet("background-color: rgba(225, 225, 225, 150);"
                                "outline: none;"
                                "border: none;"
                                "border-radius: 10px;"
                                "font-size: 19px;"
                                "padding-left: 10px;")
        self.name.setPlaceholderText("Name")

        self.data = QtWidgets.QTextEdit(self.frame)
        self.data.setGeometry(QtCore.QRect(581, 20, 161, 31))
        self.data.setStyleSheet("background-color: rgba(225, 225, 225, 150);"
                                "border: none;"
                                "border-radius: 10px;"
                                "font-size: 19px;"
                                "padding-left: 10px;")
        self.data.setPlaceholderText("01.01.2022")

        self.text = QtWidgets.QTextEdit(self.frame)
        self.text.setGeometry(QtCore.QRect(20, 71, 722, 120))
        self.text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text.setStyleSheet("background-color: rgba(225, 225, 225, 150);"
                                "border: none;"
                                "border-radius: 10px;"
                                "font-size: 19px;"
                                "padding-left: 10px;")
        self.text.setPlaceholderText("Text")

        self.priority_1 = QtWidgets.QPushButton(self.frame)
        self.priority_1.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.priority_1.setCheckable(True)
        self.priority_1.setChecked(True)
        self.priority_1.setStyleSheet("QPushButton {"
                                      "background-color: rgb(169, 220, 170);"
                                      "border-top-left-radius: 10px;"
                                      "border-bottom-left-radius: 10px;"
                                      "outline: none;"
                                      "}"
                                      "QPushButton:checked {"
                                      "background-color: rgb(80, 172, 83);"
                                      "border-top-left-radius: 10px;"
                                      "border-bottom-left-radius: 10px;"
                                      "outline: none;"
                                      "}")
        self.priority_1.clicked.connect(lambda: self.toggle_button(1))

        self.priority_2 = QtWidgets.QPushButton(self.frame)
        self.priority_2.setGeometry(QtCore.QRect(51, 20, 31, 31))
        self.priority_2.setCheckable(True)
        self.priority_2.setChecked(False)
        self.priority_2.setStyleSheet("QPushButton {"
                                      "background-color: rgb(234, 218, 194);"
                                      "border: none"
                                      "}"
                                      "QPushButton:checked {"
                                      "background-color: rgb(242, 177, 9);"
                                      "border: none"
                                      "}")
        self.priority_2.clicked.connect(lambda: self.toggle_button(2))

        self.priority_3 = QtWidgets.QPushButton(self.frame)
        self.priority_3.setGeometry(QtCore.QRect(82, 20, 31, 31))
        self.priority_3.setCheckable(True)
        self.priority_3.setChecked(False)
        self.priority_3.setStyleSheet("QPushButton {"
                                      "background-color: rgb(226, 166, 166);"
                                      "border-top-right-radius: 10px;"
                                      "border-bottom-right-radius: 10px;"
                                      "}"
                                      "QPushButton:checked {"
                                      "background-color: rgb(202, 71, 71);"
                                      "border-top-right-radius: 10px;"
                                      "border-bottom-right-radius: 10px;"
                                      "}")
        self.priority_3.clicked.connect(lambda: self.toggle_button(3))

        self.button_add = QtWidgets.QPushButton(self.frame)
        self.button_add.setGeometry(QtCore.QRect(710, 210, 32, 32))
        self.button_add.setStyleSheet("QPushButton {"
                                      "border: none;"
                                      "outline: none;"
                                      "background-color: rgb(169, 220, 170);"
                                      "background-image: url(resources/apply_add_button.png);"
                                      "border-radius: 10px;"
                                      "}"
                                      "QPushButton:hover {"
                                      "border: none;"
                                      "outline: none;"
                                      "background-color: rgb(80, 172, 83);"
                                      "background-image: url(resources/apply_add_button_hover.png);"
                                      "border-radius: 10px"
                                      "}")

    def checkRegulations(self):
        check = True
        pattern = re.compile('(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$')
        if self.name.toPlainText() == "":
            self.name.setStyleSheet("background-color: rgb(226, 166, 166);"
                                    "border: none;"
                                    "border-radius: 10px;"
                                    "font-size: 19px;"
                                    "padding-left: 10px;")
            check = False
        else:
            self.name.setStyleSheet("background-color: rgba(225, 225, 225, 150);"
                                    "border: none;"
                                    "border-radius: 10px;"
                                    "font-size: 19px;"
                                    "padding-left: 10px;")
            check = True
        data = self.data.toPlainText()
        if data != "":
            data = re.sub(r'\.', '/', data)
            if not re.search(pattern, data):
                self.data.setStyleSheet("background-color: rgb(226, 166, 166);"
                                        "border: none;"
                                        "border-radius: 10px;"
                                        "font-size: 19px;"
                                        "padding-left: 10px;")
                check = False
            else:
                self.data.setStyleSheet("background-color: rgba(225, 225, 225, 150);"
                                        "border: none;"
                                        "border-radius: 10px;"
                                        "font-size: 19px;"
                                        "padding-left: 10px;")
                check = True
        return check

    def toggle_button(self, n):
        if n == 1:
            self.priority_1.setChecked(True)
            self.priority_2.setChecked(False)
            self.priority_3.setChecked(False)
        if n == 2:
            self.priority_1.setChecked(False)
            self.priority_2.setChecked(True)
            self.priority_3.setChecked(False)
        if n == 3:
            self.priority_1.setChecked(False)
            self.priority_2.setChecked(False)
            self.priority_3.setChecked(True)