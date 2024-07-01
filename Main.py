import sys, os, datetime, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QApplication, QHBoxLayout, QVBoxLayout, \
    QTextEdit, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QFrame, QScrollArea, QGridLayout, QComboBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QSignalMapper
from PyQt5.QtGui import QIcon, QFont, QColor, QMouseEvent, QPixmap

import sqlite3, random
import pyqtgraph as pg

from ToWrite import ToWrite
from ToRead import ToRead
from ToStat import ToStat
from ToMoney import ToMoney

class Main(QWidget):
    def __init__(self, login):
        super(Main, self).__init__()

        self.conn = sqlite3.connect("geschloss.db")
        self.cursor = self.conn.cursor()

        self.login = login

        self.init_ui()

        self.show()

    def init_ui(self):

        self.window = QWidget(self)
        self.resize(600, 800)
        self.move(400, 100)
        self.setWindowTitle('ToWrite')
        self.setWindowIcon(QIcon('icon.bmp'))

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#00CED1"))
        self.pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor("#7FFFD4"))
        self.setPalette(self.pal)

        self.vbox = QVBoxLayout(self)

        self.label = QLabel("")
        self.label.setFont(QFont('TimesNewRoman', 18))
        self.label.setMinimumSize(450, 10)
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        self.TodayDay()

        label11 = QLabel("Words:")
        label11.setFont(QFont('TimesNewRoman', 18))
        label11.setAlignment(QtCore.Qt.AlignCenter)
        self.label12 = QLabel("0")
        self.label12.setFont(QFont('TimesNewRoman', 22))
        self.label12.setAlignment(QtCore.Qt.AlignCenter)
        self.countToday()

        pic_label10 = QLabel(self)
        self.pixmap10 = QPixmap("mtp.png")
        pic_label10.setPixmap(self.pixmap10)
        pic_label10.setFont(QFont('TimesNewRoman', 18))
        pic_label10.setMinimumSize(450, 10)
        pic_label10.setAlignment(QtCore.Qt.AlignCenter)
        pic_label10.setStyleSheet("border: 10px solid white;")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.label)
        self.vbox12 = QVBoxLayout()
        self.hbox.addLayout(self.vbox12)
        self.vbox12.addWidget(label11)
        self.vbox12.addWidget(self.label12)
        self.hbox11 = QHBoxLayout()
        self.hbox11.addWidget(pic_label10)
        self.vbox11 = QVBoxLayout()
        self.vbox11.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox11)


        self.label2 = QLabel("")
        self.label2.setStyleSheet("""font-style: oblique;
                                  border: 2px dotted white;""")
        self.label2.setFont(QFont('TimesNewRoman', 18))
        self.label2.setMinimumSize(450, 10)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setWordWrap(True)

        self.Advise()

        button20 = QPushButton("", self)
        button20.setMaximumSize(50, 50)
        self.pixmap20 = QPixmap("sett.png")
        self.pixmap20 = self.pixmap20.scaled(50, 50)
        button20.setIcon(QIcon(self.pixmap20))
        button20.clicked.connect(self.Refresh)

        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.label2)
        self.hbox2.addWidget(button20)

        self.hbox3 = QHBoxLayout()
        button31 = QPushButton("To Write", self)
        button31.setFont(QFont('TimesNewRoman', 18))
        button31.clicked.connect(self.ToWrite)

        button32 = QPushButton("Statistic", self)
        button32.setFont(QFont('TimesNewRoman', 18))
        button32.clicked.connect(self.Statistic)

        self.vbox31 = QVBoxLayout()
        self.vbox32 = QVBoxLayout()
        self.hbox3.addLayout(self.vbox31)
        self.hbox3.addLayout(self.vbox32)

        pic_label = QLabel(self)
        self.pixmap = QPixmap("write.bmp")
        pic_label.setPixmap(self.pixmap)
        pic_label.setFont(QFont('TimesNewRoman', 18))
        pic_label.setMinimumSize(450, 10)
        pic_label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox31.addWidget(pic_label)
        self.vbox31.addWidget(button31)

        pic_label2 = QLabel(self)
        self.pixmap2 = QPixmap("analize.bmp")
        pic_label2.setPixmap(self.pixmap2)
        pic_label2.setFont(QFont('TimesNewRoman', 18))
        pic_label2.setMinimumSize(450, 10)
        pic_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox32.addWidget(pic_label2)
        self.vbox32.addWidget(button32)

        self.hbox4 = QHBoxLayout()
        button41 = QPushButton("To Read", self)
        button41.setFont(QFont('TimesNewRoman', 18))
        button41.clicked.connect(self.toRead)

        button42 = QPushButton("Make Money", self)
        button42.setFont(QFont('TimesNewRoman', 18))
        button42.clicked.connect(self.MakeMoney)

        self.vbox41 = QVBoxLayout()
        self.vbox42 = QVBoxLayout()
        self.hbox4.addLayout(self.vbox41)
        self.hbox4.addLayout(self.vbox42)

        pic_label3 = QLabel(self)
        self.pixmap3 = QPixmap("read.bmp")
        pic_label3.setPixmap(self.pixmap3)
        pic_label3.setFont(QFont('TimesNewRoman', 18))
        pic_label3.setMinimumSize(450, 10)
        pic_label3.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox41.addWidget(pic_label3)
        self.vbox41.addWidget(button41)

        pic_label4 = QLabel(self)
        self.pixmap4 = QPixmap("coin.bmp")
        pic_label4.setPixmap(self.pixmap4)
        pic_label4.setFont(QFont('TimesNewRoman', 18))
        pic_label4.setMinimumSize(450, 10)
        pic_label4.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox42.addWidget(pic_label4)
        self.vbox42.addWidget(button42)

        self.vbox.addLayout(self.vbox11)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)

    def ToWrite (self):
        self.ToWrite = ToWrite(self.login)
        self.ToWrite.show()

    def Statistic (self):
        self.ToStat = ToStat(self.login)
        self.ToStat.show()

    def toRead (self):
        self.ToRead = ToRead(self.login)
        self.ToRead.show()

    def MakeMoney (self):
        self.ToMoney = ToMoney(self.login)
        self.ToMoney.show()

    def Refresh (self):
        self.countToday()
        self.TodayDay()
        self.Advise()
        self.update()

    def countToday (self):
        sql = self.cursor.execute("""select Date, NumWords from Activity
                                            where Login = '{}'""".format(self.login))
        wordsT = 0
        for i in sql.fetchall():
            if i[0][:10] == self.time[:10]:
                wordsT += i[1]
        self.label12.setText(str(wordsT))

    def TodayDay (self):
        self.time = str(datetime.datetime.now())
        self.year = self.time[:4]
        self.month = self.time[5:-19]
        self.day = self.time[8:-16]

        timeT = "Year: " + self.year + "\nMonth: " + self.month + "\nDay: " + self.day

        self.label.setText(timeT)

    def Advise (self):
        sql = self.cursor.execute("""select Advise from Advises""")
        n = 0
        for i in sql.fetchall():
            for j in i:
                n += 1
        nRandom = random.randint(1, n)
        sql = self.cursor.execute("""select Advise from Advises
                                    where Id = '{}' """.format(nRandom))
        for i in sql.fetchall():
            for j in i:
                self.label2.setText(j)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main("FlyingThinker")
    sys.exit(app.exec_())
