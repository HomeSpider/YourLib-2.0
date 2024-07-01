import sys, os, datetime, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QApplication, QHBoxLayout, QVBoxLayout, \
    QTextEdit, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QFrame, QScrollArea, QGridLayout, QComboBox, QMessageBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QSignalMapper
from PyQt5.QtGui import QIcon, QFont, QColor, QMouseEvent

import sqlite3

from ToChange import ToChange

class ToRead(QWidget):
    def __init__(self, login):
        super().__init__()

        self.conn = sqlite3.connect("geschloss.db")
        self.cursor = self.conn.cursor()

        self.login = login

        self.init_ui()

        self.show()

    def init_ui(self):

        self.window = QWidget(self)
        self.resize(600, 850)
        self.move(400, 100)
        self.setWindowTitle('ToRead')
        self.setWindowIcon(QIcon('icon.bmp'))

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#00CED1"))
        self.pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor("#7FFFD4"))
        self.setPalette(self.pal)

        self.vbox = QVBoxLayout(self)

        self.hbox = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()
        self.hbox7 = QHBoxLayout()

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox6)
        self.vbox.addLayout(self.hbox7)

        self.label = QLabel(self.login)
        self.label.setFont(QFont('TimesNewRoman', 18))
        self.label.setMinimumSize(450, 10)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("border: 10px solid white;")
        self.hbox.addWidget(self.label)

        self.vbox11 = QVBoxLayout()
        self.vbox12 = QVBoxLayout()
        self.hbox1.addLayout(self.vbox11)
        self.hbox1.addLayout(self.vbox12)
        self.vbox21 = QVBoxLayout()
        self.vbox22 = QVBoxLayout()
        self.hbox2.addLayout(self.vbox21)
        self.hbox2.addLayout(self.vbox22)
        self.vbox31 = QVBoxLayout()
        self.vbox32 = QVBoxLayout()
        self.hbox3.addLayout(self.vbox31)
        self.hbox3.addLayout(self.vbox32)
        self.vbox41 = QVBoxLayout()
        self.vbox42 = QVBoxLayout()
        self.hbox4.addLayout(self.vbox41)
        self.hbox4.addLayout(self.vbox42)
        self.vbox51 = QVBoxLayout()
        self.vbox52 = QVBoxLayout()
        self.hbox5.addLayout(self.vbox51)
        self.hbox5.addLayout(self.vbox52)
        self.vbox61 = QVBoxLayout()
        self.vbox62 = QVBoxLayout()
        self.hbox6.addLayout(self.vbox61)
        self.hbox6.addLayout(self.vbox62)

        self.buttonl = QPushButton("<", self)
        self.buttonl.setMaximumSize(90, 50)
        self.buttonl.setFont(QFont('TimesNewRoman', 12))
        self.buttonl.clicked.connect(self.back)
        self.buttonr = QPushButton(">", self)
        self.buttonr.setFont(QFont('TimesNewRoman', 12))
        self.buttonr.setMaximumSize(90, 50)
        self.buttonr.clicked.connect(self.front)
        self.labels = QComboBox()
        self.labels.setFont(QFont('TimesNewRoman', 18))
        self.labels.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
        self.c_boxes()
        self.buttons = QPushButton("Search", self)
        self.buttons.setFont(QFont('TimesNewRoman', 12))
        self.buttons.setMaximumSize(120, 50)
        self.buttons.clicked.connect(self.search)

        self.hbox7.addWidget(self.buttonl)
        self.hbox7.addWidget(self.labels)
        self.hbox7.addWidget(self.buttons)
        self.hbox7.addWidget(self.buttonr)

        self.num_page = 1
        self.full_box(self.num_page)

    def c_boxes(self):
        sql = self.cursor.execute(""" select Tegs, Tegs1, Tegs2, Tegs3, Tegs4, Tegs5 from Texts 
                                    where Login = '{}' """.format(self.login))
        list1 = []

        for i in sql.fetchall():
            for j in i:
                if j != '0' or j == "''":
                    list1.append(j)
        for i in list1:
            while list1.count(i) > 1:
                list1.pop(list1.index(i))

        for i in list1:
            self.labels.addItem(i)

    def full_box(self, n, search=0):
        if search == 0:
            sql = self.cursor.execute(""" select ID, Name, Date from Texts
                                    where Login = '{}' and
                                    ID > '{}' and
                                   ID < '{}'""".format(self.login, n-1, n+12))
        elif search == 1:
            text = self.labels.currentText()
            sql = self.cursor.execute("""select ID, Name, Date from Texts 
                                                                    WHERE Tegs like "{0}" OR Tegs1 like "{0}" OR Tegs2 like "{0}" OR Tegs3 like "{0}" OR Tegs4 like "{0}" OR Tegs5 like "{0}"
                                                                    and ID > "{1}" and ID < "{2}" 
                                                                    and Login = '{3}' """.format(text, n - 1, n + 12, self.login))
        self.conn.commit()

        counter = 0
        self.worklist = []
        for i in sql.fetchall():
            counter += 1
            self.worklist.append(i)

        counter2 = 0
        if counter <= 12:
            for i in self.worklist:
                self.full_boxW(i)
                counter2 += 1
                self.make_sense(counter2)

    def full_boxW(self, i):
        self.text = "<b>{}</b>".format(i[1])+"\n<i>{}</i>".format(i[2][:-16])

    def make_sense(self, n):
        if n == 1:
            self.label1 = QLabel("")
            self.label1.setFont(QFont('TimesNewRoman', 18))
            self.label1.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
            self.label1.setWordWrap(True)
            self.label1.setMaximumSize(300, 80)
            self.vbox11.addWidget(self.label1)
            self.label1.setText(self.text)
            self.button1 = QPushButton("Edit", self)
            self.button1.setFont(QFont('TimesNewRoman', 11))
            self.button1.clicked.connect(self.open_1)
            self.vbox11.addWidget(self.button1)
        elif n == 2:
            self.label2 = QLabel("")
            self.label2.setFont(QFont('TimesNewRoman', 18))
            self.label2.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
            self.label2.setMaximumSize(300, 80)
            self.label2.setWordWrap(True)
            self.vbox12.addWidget(self.label2)
            self.label2.setText(self.text)
            self.button2 = QPushButton("Edit", self)
            self.button2.setFont(QFont('TimesNewRoman', 11))
            self.button2.clicked.connect(self.open_2)
            self.vbox12.addWidget(self.button2)
        elif n == 3:
            self.label3 = QLabel("")
            self.label3.setFont(QFont('TimesNewRoman', 18))
            self.label3.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
            self.label3.setMaximumSize(300, 80)
            self.label3.setWordWrap(True)
            self.vbox21.addWidget(self.label3)
            self.label3.setText(self.text)
            self.button3 = QPushButton("Edit", self)
            self.button3.setFont(QFont('TimesNewRoman', 11))
            self.button3.clicked.connect(self.open_3)
            self.vbox21.addWidget(self.button3)
        elif n == 4:
            self.label4 = QLabel("")
            self.label4.setFont(QFont('TimesNewRoman', 18))
            self.label4.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
            self.label4.setMaximumSize(300, 80)
            self.label4.setWordWrap(True)
            self.vbox22.addWidget(self.label4)
            self.label4.setText(self.text)
            self.button4 = QPushButton("Edit", self)
            self.button4.setFont(QFont('TimesNewRoman', 11))
            self.button4.clicked.connect(self.open_4)
            self.vbox22.addWidget(self.button4)
        elif n == 5:
            self.label5 = QLabel("")
            self.label5.setFont(QFont('TimesNewRoman', 18))
            self.label5.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
            self.label5.setMaximumSize(300, 80)
            self.label5.setWordWrap(True)
            self.vbox31.addWidget(self.label5)
            self.label5.setText(self.text)
            self.button5 = QPushButton("Edit", self)
            self.button5.setFont(QFont('TimesNewRoman', 11))
            self.button5.clicked.connect(self.open_5)
            self.vbox31.addWidget(self.button5)
        elif n == 6:
            self.label6 = QLabel("")
            self.label6.setFont(QFont('TimesNewRoman', 18))
            self.label6.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
            self.label6.setMaximumSize(300, 80)
            self.label6.setWordWrap(True)
            self.vbox32.addWidget(self.label6)
            self.label6.setText(self.text)
            self.button6 = QPushButton("Edit", self)
            self.button6.setFont(QFont('TimesNewRoman', 11))
            self.button6.clicked.connect(self.open_6)
            self.vbox32.addWidget(self.button6)
        elif n == 7:
            self.label7 = QLabel("")
            self.label7.setFont(QFont('TimesNewRoman', 18))
            self.label7.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
            self.label7.setMaximumSize(300, 80)
            self.label7.setWordWrap(True)
            self.vbox41.addWidget(self.label7)
            self.label7.setText(self.text)
            self.button7 = QPushButton("Edit", self)
            self.button7.setFont(QFont('TimesNewRoman', 11))
            self.button7.clicked.connect(self.open_7)
            self.vbox41.addWidget(self.button7)
        elif n == 8:
            self.label8 = QLabel("")
            self.label8.setFont(QFont('TimesNewRoman', 18))
            self.label8.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
            self.label8.setMaximumSize(300, 80)
            self.label8.setWordWrap(True)
            self.vbox42.addWidget(self.label8)
            self.label8.setText(self.text)
            self.button8 = QPushButton("Edit", self)
            self.button8.setFont(QFont('TimesNewRoman', 11))
            self.button8.clicked.connect(self.open_8)
            self.vbox42.addWidget(self.button8)
        elif n == 9:
            self.label9 = QLabel("")
            self.label9.setFont(QFont('TimesNewRoman', 18))
            self.label9.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
            self.label9.setMaximumSize(300, 80)
            self.label9.setWordWrap(True)
            self.vbox51.addWidget(self.label9)
            self.label9.setText(self.text)
            self.button9 = QPushButton("Edit", self)
            self.button9.setFont(QFont('TimesNewRoman', 11))
            self.button9.clicked.connect(self.open_9)
            self.vbox51.addWidget(self.button9)
        elif n == 10:
            self.label10 = QLabel("")
            self.label10.setFont(QFont('TimesNewRoman', 18))
            self.label10.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
            self.label10.setMaximumSize(300, 80)
            self.label10.setWordWrap(True)
            self.vbox52.addWidget(self.label10)
            self.label10.setText(self.text)
            self.button10 = QPushButton("Edit", self)
            self.button10.setFont(QFont('TimesNewRoman', 11))
            self.button10.clicked.connect(self.open_10)
            self.vbox52.addWidget(self.button10)
        elif n == 11:
            self.label11 = QLabel("")
            self.label11.setFont(QFont('TimesNewRoman', 18))
            self.label11.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
            self.label11.setMaximumSize(300, 80)
            self.label11.setWordWrap(True)
            self.vbox61.addWidget(self.label11)
            self.label11.setText(self.text)
            self.button11 = QPushButton("Edit", self)
            self.button11.setFont(QFont('TimesNewRoman', 11))
            self.button11.clicked.connect(self.open_11)
            self.vbox61.addWidget(self.button11)
        elif n == 12:
            self.label12 = QLabel("")
            self.label12.setFont(QFont('TimesNewRoman', 18))
            self.label12.setStyleSheet('border-style: solid; border-width: 1px; border-color: white;')
            self.label12.setMaximumSize(300, 80)
            self.label12.setWordWrap(True)
            self.vbox62.addWidget(self.label12)
            self.label12.setText(self.text)
            self.button12 = QPushButton("Edit", self)
            self.button12.setFont(QFont('TimesNewRoman', 11))
            self.button12.clicked.connect(self.open_12)
            self.vbox62.addWidget(self.button12)

    def open_1(self):
        num = self.num_page%12
        name = self.name_find(num)
        self.toChange = ToChange(self.login, name)
        self.toChange.show()
    def open_2(self):
        num = (self.num_page % 12)+1
        name = self.name_find(num)
        self.toChange = ToChange(self.login, name)
        self.toChange.show()
    def open_3(self):
        num = (self.num_page % 12)+2
        name = self.name_find(num)
        self.toChange = ToChange(self.login, name)
        self.toChange.show()
    def open_4(self):
        num = (self.num_page % 12)+3
        name = self.name_find(num)
        self.toChange = ToChange(self.login, name)
        self.toChange.show()
    def open_5(self):
        num = (self.num_page % 12)+4
        name = self.name_find(num)
        self.toChange = ToChange(self.login, name)
        self.toChange.show()
    def open_6(self):
        num = (self.num_page % 12)+5
        name = self.name_find(num)
        self.toChange = ToChange(self.login, name)
        self.toChange.show()
    def open_7(self):
        num = (self.num_page % 12)+6
        name = self.name_find(num)
        self.toChange = ToChange(self.login, name)
        self.toChange.show()
    def open_8(self):
        num = (self.num_page % 12)+7
        name = self.name_find(num)
        self.toChange = ToChange(self.login, name)
        self.toChange.show()
    def open_9(self):
        num = (self.num_page % 12)+8
        name = self.name_find(num)
        self.toChange = ToChange(self.login, name)
        self.toChange.show()
    def open_10(self):
        num = (self.num_page % 12)+9
        name = self.name_find(num)
        self.toChange = ToChange(self.login, name)
        self.toChange.show()
    def open_11(self):
        num = (self.num_page % 12)+10
        name = self.name_find(num)
        self.toChange = ToChange(self.login, name)
        self.toChange.show()
    def open_12(self):
        num = (self.num_page % 12)+11
        name = self.name_find(num)
        self.toChange = ToChange(self.login, name)
        self.toChange.show()

    def name_find(self, num):
        sql = self.cursor.execute(""" select Name from Texts
                                            where Login = '{}' and
                                            ID = '{}'""".format(self.login, num))
        name = ""
        for i in sql.fetchall():
            for j in i:
                name = j
        return name

    def notext(self):
        try:
            self.label1.setParent(None)
            self.label2.setParent(None)
            self.label3.setParent(None)
            self.label4.setParent(None)
            self.label5.setParent(None)
            self.label6.setParent(None)
            self.label7.setParent(None)
            self.label8.setParent(None)
            self.label9.setParent(None)
            self.label10.setParent(None)
            self.label11.setParent(None)
            self.label12.setParent(None)

            self.button1.setParent(None)
            self.button2.setParent(None)
            self.button3.setParent(None)
            self.button4.setParent(None)
            self.button5.setParent(None)
            self.button6.setParent(None)
            self.button7.setParent(None)
            self.button8.setParent(None)
            self.button9.setParent(None)
            self.button10.setParent(None)
            self.button11.setParent(None)
            self.button12.setParent(None)
        except:
           pass

    def back(self):
        self.num_page -= 12
        self.notext()
        self.full_box(self.num_page)
        self.update()
    def front(self):
        self.num_page += 12
        self.notext()
        self.full_box(self.num_page)
        self.update()

    def search(self):
        self.notext()
        self.full_box(self.num_page, 1)
        self.update()
