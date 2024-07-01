import sys, os, datetime, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QApplication, QHBoxLayout, QVBoxLayout, \
    QTextEdit, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QFrame, QScrollArea, QGridLayout, QComboBox, QMessageBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QSignalMapper
from PyQt5.QtGui import QIcon, QFont, QColor, QMouseEvent
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

import sqlite3

class ToStat(QWidget):
    def __init__(self, login):
        super().__init__()

        self.conn = sqlite3.connect("geschloss.db")
        self.cursor = self.conn.cursor()

        self.TodayDay()
        self.login = login

        self.init_ui()

        self.show()

    def init_ui(self):

        self.window = QWidget(self)
        self.resize(600, 850)
        self.move(400, 100)
        self.setWindowTitle('ToStat')
        self.setWindowIcon(QIcon('tostat.jpg'))

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#6FFFD9"))
        self.pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor("#BDFFEE"))
        self.setPalette(self.pal)

        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout(self)
        self.hbox2 = QHBoxLayout(self)
        hbox3 = QHBoxLayout(self)
        hbox4 = QHBoxLayout(self)
        vbox.addLayout(hbox)
        vbox.addLayout(self.hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        self.date = QComboBox(self)
        self.date.setFont(QFont('TimesNewRoman', 12))
        list = ["All time", "Today", "Week", "Month", "3 Months"]
        for i in list:
            self.date.addItem(i)
        hbox.addWidget(self.date)

        self.button = QPushButton("ReCreate", self)
        self.button.setFont(QFont('TimesNewRoman', 12))
        self.button.clicked.connect(self.ReCreate)
        hbox.addWidget(self.button)

        self.get_activity()

        self.win = pg.GraphicsLayoutWidget(show=True)
        self.plt1 = self.win.addPlot()
        self.bgi = pg.BarGraphItem(x=self.nums, height=self.words, width=1,
                                                           brush='w')

        self.plt1.addItem(self.bgi)
        self.hbox2.addWidget(self.win)

    def TodayDay (self):
        self.time = str(datetime.datetime.now())
        self.year = self.time[:4]
        self.month = self.time[5:-19]
        self.day = self.time[8:-16]

    def get_activity(self):
        sql = self.cursor.execute(""" select Date, NumWords from Activity 
                                            where Login = '{}' """.format(self.login))
        self.cursor = self.conn.cursor()

        self.dates = []
        self.words = []
        self.nums = []
        n = 1

        for i in sql.fetchall():
            self.dates.append(i[0])
            self.words.append(i[1])
            self.nums.append(n)
            n += 1

    def ReCreate(self):
        text = self.date.currentText()

        sql = self.cursor.execute(""" select Date, NumWords from Activity 
                                                                where Login = '{}'""".format(self.login))
        self.cursor = self.conn.cursor()
        n = -1
        k = 1
        self.words = []
        self.nums = []
        worklist = []
        today = 0

        if text == "Today":
            self.nums = [int(self.day), int(self.day)+1, int(self.day)+2]
            for i in sql.fetchall():
                if i[0][:4] == self.year and i[0][5:-19] == self.month and i[0][8:-16] == self.day:
                    today += i[1]
            self.words = [today, 0, 0]
            self.make_graph()
        elif text == "Week":
            for i in sql.fetchall():
                worklist.append(i)
            for i in range(1, 8):
                try:
                    self.words.append(worklist[n][1])
                except:
                    break
                n += -1
                self.nums.append(k)
                k += 1
            self.words.reverse()
            self.make_graph()
        elif text == "Month":
            for i in sql.fetchall():
                worklist.append(i)
            for i in range(1, 32):
                try:
                    self.words.append(worklist[n][1])
                except:
                    break
                n += -1
                self.nums.append(k)
                k += 1
            self.words.reverse()
            self.make_graph()
        elif text == "3 Months":
            for i in sql.fetchall():
                worklist.append(i)
            for i in range(1, 93):
                try:
                    self.words.append(worklist[n][1])
                except:
                    break
                n += -1
                self.nums.append(k)
                k += 1
            self.words.reverse()
            self.make_graph()
        elif text == "All time":
            self.get_activity()
            self.make_graph()


    def make_graph(self):
        self.win.setParent(None)

        self.win = pg.GraphicsLayoutWidget(show=True)
        self.plt1 = self.win.addPlot()
        self.bgi = pg.BarGraphItem(x=self.nums, height=self.words, width=1,
                                   brush='w')

        self.plt1.addItem(self.bgi)
        self.hbox2.addWidget(self.win)

