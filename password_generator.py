import sys
from win32clipboard import OpenClipboard, EmptyClipboard, SetClipboardText, CloseClipboard, CF_UNICODETEXT
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
from senha import Ui_MainWindow
from random import shuffle, choices


class Password(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowIcon(QtGui.QIcon('password.ico'))
        self.generate_button.clicked.connect(self.generate_password)
        self.copy_button.clicked.connect(self.copy_to_clipboard)

    def generate_password(self):
        self.copy_button.setEnabled(True)
        caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        tam = int(self.len_password_button.text())

        if self.yes_button.isChecked():
            caracteres_especiais = '_@.&'

            if tam >= 8 and tam <= 16:
                num_esp = 3
            elif tam >= 17 and tam <= 36:
                num_esp = 6
            else:
                num_esp = 9

            password = choices(caracteres_especiais, k=num_esp)
            carac = choices(caracteres, k=tam - num_esp)
            password += carac
            while password[0] in caracteres_especiais:
                shuffle(password)

            password = ''.join(password)
            self.output_label.setText(password)
        else:
            password = choices(caracteres, k=tam)
            shuffle(password)
            password = ''.join(password)
            self.output_label.setText(password)

    def copy_to_clipboard(self):
        OpenClipboard()
        EmptyClipboard()
        SetClipboardText(self.output_label.text(), CF_UNICODETEXT)
        CloseClipboard()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    senha = Password()
    senha.show()
    qt.exec_()
