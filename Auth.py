import sys, os, datetime, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QApplication, QHBoxLayout, QVBoxLayout, \
    QTextEdit, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QFrame, QScrollArea, QGridLayout, QComboBox, QMessageBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QSignalMapper
from PyQt5.QtGui import QIcon, QFont, QColor, QMouseEvent
from cryptography.fernet import Fernet

import sqlite3

from DB import DB
from Main import Main


class Auth(QWidget):
    def __init__(self):
        super().__init__()

        self.window = QWidget(self)
        self.resize(500, 200)
        self.move(400, 100)
        self.setWindowTitle('Log in')
        self.setWindowIcon(QIcon('icon.bmp'))

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#4682B4"))
        self.pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor("#5F9EA0"))
        self.setPalette(self.pal)

        self.DB = DB()

        self.conn = sqlite3.connect("geschloss.db")
        self.cursor = self.conn.cursor()

        self.vbox = QVBoxLayout(self)

        label = QLabel("Login")
        label.setFont(QFont('TimesNewRoman', 18))
        label.setMinimumSize(200, 50)
        self.login_line = QLineEdit(self)
        self.login_line.setFont(QFont('TimesNewRoman', 18))
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(label)
        self.hbox.addWidget(self.login_line)

        label2 = QLabel("Password")
        label2.setFont(QFont('TimesNewRoman', 18))
        label2.setMinimumSize(200, 50)
        self.password_line = QLineEdit(self)
        self.password_line.setFont(QFont('TimesNewRoman', 18))
        self.password_line.setEchoMode(QLineEdit.Password)
        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(label2)
        self.hbox2.addWidget(self.password_line)

        self.go_reg = QPushButton("Register", self)
        self.go_reg.clicked.connect(self.register)
        self.go_reg.setFont(QFont('TimesNewRoman', 15))
        self.go_next = QPushButton("Log in", self)
        self.go_next.clicked.connect(self.log_in)
        self.go_next.setFont(QFont('TimesNewRoman', 15))
        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(self.go_reg)
        self.hbox3.addWidget(self.go_next)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)

        self.show()

    def register(self):
        login = self.login_line.text()
        password = self.password_line.text()

        sql = self.cursor.execute(""" INSERT INTO Users (Login, Password)
                                        VALUES('{}', '{}') """.format(login, password))
        self.conn.commit()

        self.close()

        self.Main = Main(login)

        # new_pass = self.cript(password)

    def cript(self, password):
        key = b'xe-TWnSBJRcdkCQfQofB6yBkkwjxwDFIUvH_HWVgT3I='
        cipher_suite = Fernet(key)
        new_pass = cipher_suite.encrypt(f'{password}'.encode('utf-8'))
        return new_pass

    def log_in(self):
        login = self.login_line.text()
        password = self.password_line.text()
        self.enter = login

        lp_list = []
        lp_list.append(login)
        lp_list.append(password)
        self.check(lp_list)

    def check(self, to_check):
        check = False
        check2 = False
        sql = self.cursor.execute("""select Login from Users """)
        for k in sql.fetchall():
            for j in k:
                if j == to_check[0]:
                    check = True

        sql = self.cursor.execute("""select Password from Users """)
        for k in sql.fetchall():
            for j in k:
                if j == to_check[1]:
                    check2 = True

        if check != True or check2 != True:
            self.n_cor = QMessageBox.critical(self, "Check your input data",
                                              "Wrong login or password",
                                              defaultButton=QMessageBox.Ok)
        else:
            self.close()
            self.Main = Main(self.enter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Auth()
    sys.exit(app.exec_())
