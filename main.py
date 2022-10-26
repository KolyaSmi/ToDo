from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QLabel, QMainWindow, QVBoxLayout, QWidget

import sys # Только для доступа к аргументам командной строки

# Приложению нужен один (и только один) экземпляр QApplication.
# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
class MainWindow(QMainWindow):
  def __init__(self):
    #super().__init__()
    super(MainWindow, self).__init__()

    self.button_is_checked = True

    self.setFixedSize(QSize(1200, 700))

    self.setWindowTitle("To-Do")

    self.label = QLabel()

    self.input = QLineEdit()
    self.input.textChanged.connect(self.label.setText)
    self.input.setFixedSize(200, 50)
    f = self.input.font()
    f.setPointSize(20)
    self.input.setFont(f)

    layout = QVBoxLayout()
    layout.addWidget(self.input)
    layout.addWidget(self.label)

    container = QWidget()
    container.setLayout(layout)

    self.setCentralWidget(container)

    # button = QPushButton("Press Me!")
    #
    # button.setCheckable(True)#Для отслеживания события click
    # button.clicked.connect(self.toggleButton)#Запуск функции по клику
    # button.setChecked(self.button_is_checked)

    # Устанавливаем центральный виджет Window.
    # self.setCentralWidget(button)

  def toggleButton(self, checked):
    self.button_is_checked = checked

    print(self.button_is_checked)

app = QApplication(sys.argv)

# Создаём виджет Qt — окно.
#window = QWidget()
window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()

# Приложение не доберётся сюда, пока вы не выйдете и цикл