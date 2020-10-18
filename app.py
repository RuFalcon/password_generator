from PyQt5.QtWidgets import (
    QWidget,
    QSlider,
    QLabel,
    QApplication,
    QMainWindow,
    QCheckBox,
    QLineEdit)
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import sys
import random
import string


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('password.ui', self)

        self.setGeometry(200, 200, 800, 553)
        self.setWindowIcon(QIcon('images/password.svg'))

        self.setFixedHeight(553)
        self.setFixedWidth(800)

        self.lowcase_letters = string.ascii_lowercase
        self.upcase_letters = string.ascii_uppercase
        self.digits = string.digits
        self.punctuation = string.punctuation

        self.password_characters = self.lowcase_letters + \
            self.upcase_letters + self.digits

        self.check_lowcase = self.findChild(QCheckBox, "check_lowcase")
        self.state_changed(self.check_lowcase)

        self.check_upcase = self.findChild(QCheckBox, "check_upcase")
        self.state_changed(self.check_upcase)

        self.check_numbers = self.findChild(QCheckBox, "check_numbers")
        self.state_changed(self.check_numbers)

        self.check_symbols = self.findChild(QCheckBox, "check_symbols")
        self.state_changed(self.check_symbols)

        self.slider = self.findChild(QSlider, "horizontalSlider")
        self.slider.valueChanged.connect(self.changed_slider)

        self.password = self.findChild(QLineEdit, "password")
        self.password_length = self.findChild(QLabel, "password_length")

        self.get_random_password(int(self.password_length.text()))

    def state_changed(self, checkbox):
        """Отслеживаем изменения нажатия чекбоксов и вызываем функцию change_password"""
        return checkbox.stateChanged.connect(self.change_password)

    def changed_slider(self):
        """Отслеживаем значение слайдера и пересобираем пароль с такой же длиной"""
        value = self.slider.value()
        self.password_length.setText(str(value))
        self.get_random_password(value)

    def get_random_password(self, length):
        """Собираем пароль с заданной длиной"""
        password = ''.join(random.choice(self.password_characters)
                           for i in range(length))
        self.password.setText(str(password))

    def change_password(self):
        """Меняем пароль в зависимости от включенных чекбоксов"""
        self.password_characters = 'x'
        if self.check_lowcase.isChecked():
            self.password_characters += self.lowcase_letters
        if self.check_upcase.isChecked():
            self.password_characters += self.upcase_letters
        if self.check_numbers.isChecked():
            self.password_characters += self.digits
        if self.check_symbols.isChecked():
            self.password_characters += self.punctuation

        self.get_random_password(int(self.password_length.text()))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
