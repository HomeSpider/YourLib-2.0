import sys, os, datetime, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QApplication, QHBoxLayout, QVBoxLayout, \
    QTextEdit, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QFrame, QScrollArea, QGridLayout, QComboBox, QMessageBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QSignalMapper
from PyQt5.QtGui import QIcon, QFont, QColor, QMouseEvent, QPixmap

import sqlite3

class ToMoney(QWidget):
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
        self.setWindowTitle('ToMoney')
        self.setWindowIcon(QIcon('tomoney.png'))

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#6FFFD9"))
        self.pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor("#BDFFEE"))
        self.setPalette(self.pal)

        self.vbox = QVBoxLayout(self)
        self.vbox81 = QVBoxLayout(self)
        self.vbox82 = QVBoxLayout(self)
        self.hbox = QHBoxLayout(self)
        self.hbox2 = QHBoxLayout(self)
        self.hbox3 = QHBoxLayout(self)
        self.hbox4 = QHBoxLayout(self)
        self.hbox5 = QHBoxLayout(self)
        self.hbox6 = QHBoxLayout(self)
        self.hbox7 = QHBoxLayout(self)
        self.hbox8 = QHBoxLayout(self)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox6)
        self.vbox.addLayout(self.hbox7)
        self.vbox.addLayout(self.hbox8)

        self.hbox8.addLayout(self.vbox81)
        self.hbox8.addLayout(self.vbox82)

        self.getNum()
        self.TodayGoal()

        self.label = QLabel("Personal Goal:")
        self.label.setFont(QFont('TimesNewRoman', 26))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("border: 6px dotted white;")
        self.hbox.addWidget(self.label)

        self.label2 = QLabel(str(self.words)+" / "+str(self.num1))
        self.label2.setFont(QFont('TimesNewRoman', 20))
        self.label2.setAlignment(QtCore.Qt.AlignRight)
        self.hbox2.addWidget(self.label2)

        self.label3 = QLabel("Day complete:")
        self.label3.setFont(QFont('TimesNewRoman', 26))
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setStyleSheet("border: 6px dotted white;")
        self.hbox3.addWidget(self.label3)

        self.label4 = QLabel(str(self.days)+" / "+str(self.num2))
        self.label4.setFont(QFont('TimesNewRoman', 20))
        self.label4.setAlignment(QtCore.Qt.AlignRight)
        self.hbox4.addWidget(self.label4)

        self.label5 = QLabel("Pay FOR:")
        self.label5.setFont(QFont('TimesNewRoman', 26))
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setStyleSheet("border: 6px dotted white;")
        self.hbox5.addWidget(self.label5)

        self.label6 = QLabel(str(self.num3)+" words")
        self.label6.setFont(QFont('TimesNewRoman', 20))
        self.label6.setAlignment(QtCore.Qt.AlignRight)
        self.hbox6.addWidget(self.label6)

        self.label7 = QLabel(str(self.num4)+" dollars")
        self.label7.setFont(QFont('TimesNewRoman', 20))
        self.label7.setAlignment(QtCore.Qt.AlignRight)
        self.hbox7.addWidget(self.label7)

        if self.num3 * self.num4 == 0:
            self.label8 = QLabel("Earned: "+str(0)+"$")
        else:
            self.label8 = QLabel("Earned: " + str(self.earns / self.num3 * self.num4) + "$")
        self.label8.setFont(QFont('TimesNewRoman', 26))
        self.label8.setAlignment(QtCore.Qt.AlignCenter)
        self.label8.setStyleSheet("border: 6px dotted white;")
        self.vbox81.addWidget(self.label8)

        self.button = QPushButton("", self)
        self.button.setMaximumSize(50, 50)
        self.pixmap = QPixmap("sett2.png")
        self.pixmap = self.pixmap.scaled(150, 150)
        self.button.setIcon(QIcon(self.pixmap))
        self.button.clicked.connect(self.Param)
        self.vbox82.addWidget(self.button)

        self.button2 = QPushButton("", self)
        self.button2.setMaximumSize(50, 50)
        self.pixmap2 = QPixmap("sett.png")
        self.pixmap2 = self.pixmap2.scaled(50, 50)
        self.button2.setIcon(QIcon(self.pixmap2))
        self.button2.clicked.connect(self.ReNew)
        self.vbox82.addWidget(self.button2)

    def TodayGoal(self):
        sql = self.cursor.execute("""select Date, NumWords from Activity where Login = '{}'""".format(self.login))
        self.conn.commit()

        self.TodayDay()

        self.words = 0
        self.earns = 0

        for i in sql.fetchall():
            if i[0][:4] == self.year and i[0][5:-19] == self.month and i[0][8:-16] == self.day:
                self.words += i[1]
            if i[0][:4] == self.year and i[0][5:-19] == self.month:
                self.earns += i[1]

        sql = self.cursor.execute("""select Date, GoalComplete from Activity where Login = '{}'""".format(self.login))
        self.conn.commit()

        self.days = 0

        for i in sql.fetchall():
            if i[0][:4] == self.year and i[0][5:-19] == self.month:
                self.days += i[1]

    def TodayDay (self):
        self.time = str(datetime.datetime.now())
        self.year = self.time[:4]
        self.month = self.time[5:-19]
        self.day = self.time[8:-16]

    def Param(self):
        self.Param = Param(self.login)
        self.Param.show()

    def ReNew(self):
        self.getNum()
        self.label2.setText(str(self.words)+" / "+str(self.num1))
        self.label4.setText(str(self.days)+" / "+str(self.num2))
        self.label6.setText(str(self.num3)+" words")
        self.label7.setText(str(self.num4)+" dollars")
        if self.num3 * self.num4 == 0:
            self.label8.setText("Earned: " + str(0) + "$")
        else:
            self.label8.setText("Earned: " + str(self.earns / self.num3 * self.num4) + "$")
        self.update()

    def getNum(self):
        sql = self.cursor.execute("""select * from Goals where Login = '{}'""".format(self.login))
        self.conn.commit()

        worklist = []

        for i in sql.fetchall():
            for j in i:
                worklist.append(j)

        if worklist:
            self.num1 = worklist[2]
            self.num2 = worklist[3]
            self.num3 = worklist[4]
            self.num4 = worklist[5]
        else:
            self.num1 = "0"
            self.num2 = "0"
            self.num3 = "0"
            self.num4 = "0"

class Param(QWidget):
    def __init__(self, login):
        super().__init__()

        self.conn = sqlite3.connect("geschloss.db")
        self.cursor = self.conn.cursor()

        self.login = login

        self.init_ui()

        self.show()

    def init_ui(self):
        self.window = QWidget(self)
        self.resize(600, 400)
        self.move(400, 100)
        self.setWindowTitle('Parameters')
        self.setWindowIcon(QIcon('tomoney.png'))

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#6FFFD9"))
        self.pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor("#BDFFEE"))
        self.setPalette(self.pal)

        self.vbox = QVBoxLayout(self)
        self.hbox = QHBoxLayout(self)
        self.hbox2 = QHBoxLayout(self)
        self.hbox3 = QHBoxLayout(self)
        self.hbox4 = QHBoxLayout(self)
        self.hbox5 = QHBoxLayout(self)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)

        self.label = QLabel("Words/day Goal:")
        self.label.setFont(QFont('TimesNewRoman', 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.hbox.addWidget(self.label)

        self.place = QLineEdit(self)
        self.place.setFont(QFont('TimesNewRoman', 18))
        self.place.setAlignment(QtCore.Qt.AlignRight)
        self.place.setMaximumSize(250, 50)
        self.hbox.addWidget(self.place)

        self.label2 = QLabel("Day/month Goal:")
        self.label2.setFont(QFont('TimesNewRoman', 20))
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.hbox2.addWidget(self.label2)

        self.place2 = QLineEdit(self)
        self.place2.setFont(QFont('TimesNewRoman', 18))
        self.place2.setAlignment(QtCore.Qt.AlignRight)
        self.place2.setMaximumSize(250, 50)
        self.hbox2.addWidget(self.place2)

        self.label3 = QLabel("Num words payed:")
        self.label3.setFont(QFont('TimesNewRoman', 20))
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.hbox3.addWidget(self.label3)

        self.place3 = QLineEdit(self)
        self.place3.setFont(QFont('TimesNewRoman', 18))
        self.place3.setAlignment(QtCore.Qt.AlignRight)
        self.place3.setMaximumSize(250, 50)
        self.hbox3.addWidget(self.place3)

        self.label4 = QLabel("Sum payed:")
        self.label4.setFont(QFont('TimesNewRoman', 20))
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.hbox4.addWidget(self.label4)

        self.place4 = QLineEdit(self)
        self.place4.setFont(QFont('TimesNewRoman', 18))
        self.place4.setAlignment(QtCore.Qt.AlignRight)
        self.place4.setMaximumSize(250, 50)
        self.hbox4.addWidget(self.place4)

        self.button = QPushButton("Save", self)
        self.button.setFont(QFont('TimesNewRoman', 20))
        self.button.clicked.connect(self.Save)
        self.hbox5.addWidget(self.button)

        self.getNum()

    def getNum(self):
        sql = self.cursor.execute("""select * from Goals where Login = '{}'""".format(self.login))
        self.conn.commit()

        worklist = []

        for i in sql.fetchall():
            for j in i:
                worklist.append(j)

        if worklist:
            self.place.setText(str(worklist[2]))
            self.place2.setText(str(worklist[3]))
            self.place3.setText(str(worklist[4]))
            self.place4.setText(str(worklist[5]))
        else:
            self.place.setText('0')
            self.place2.setText('0')
            self.place3.setText('0')
            self.place4.setText('0')

    def Save(self):
        place = self.place.text()
        place2 = self.place2.text()
        place3 = self.place3.text()
        place4 = self.place4.text()

        try:
            sql = self.cursor.execute(""" UPDATE Goals 
                         SET WordsGoal = {}, 
                         DayGoal = {}, 
                         WordsPay = {}, 
                         SumPay = {}
                         where Login = '{}' """.format(place, place2, place3, place4, self.login))
            self.conn.commit()
        except:
            sql = self.cursor.execute(""" INSERT INTO Goals (Login, WordsGoal, DayGoal, WordsPay, SumPay)
                                     VALUES('{}', {}, {}, {}, {})""".format(self.login, place, place2, place3, place4))
            self.conn.commit()

        self.close()
