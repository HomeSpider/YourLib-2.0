import sys, os, datetime, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QApplication, QHBoxLayout, QVBoxLayout, \
    QTextEdit, QLabel, QPushButton, QPlainTextEdit, QLineEdit, QFrame, QScrollArea, QGridLayout, QComboBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QSignalMapper
from PyQt5.QtGui import QIcon, QFont, QColor, QMouseEvent
import sqlite3

class ToChange(QWidget):
    def __init__(self, login, open=0):
        super().__init__()
        self.resize(800, 600)
        self.move(300, 100)
        self.name = 'Changing Corner'
        self.setWindowTitle(self.name)
        self.setWindowIcon(QIcon('towpen.png'))

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#9EFDFF"))
        self.pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor("#7FFFD4"))
        self.setPalette(self.pal)

        self.login = login

        vbox = QVBoxLayout(self)

        hbox1 = QHBoxLayout(self)
        self.namelbl = QLabel("Choose File Name:")
        self.namelbl.setFont(QFont('TimesNewRoman', 12))
        self.namelbl.setAlignment(Qt.AlignCenter)
        hbox1.addWidget(self.namelbl)
        self.name = QComboBox(self)
        self.name.setFont(QFont('TimesNewRoman', 12))
        self.namecom = QPushButton("Open File", self)
        self.namecom.setFont(QFont('TimesNewRoman', 12))
        self.namecom.clicked.connect(self.com)

        hbox2 = QHBoxLayout(self)
        self.namelbl2 = QLabel("Change File Name:")
        self.namelbl2.setFont(QFont('TimesNewRoman', 12))
        self.namelbl2.setAlignment(Qt.AlignCenter)
        hbox2.addWidget(self.namelbl2)
        self.namet = QLineEdit(self)
        self.namet.setFont(QFont('TimesNewRoman', 12))
        hbox2.addWidget(self.namet)

        self.conn = sqlite3.connect("geschloss.db")
        self.cursor = self.conn.cursor()

        sql = self.cursor.execute("""select Name from Texts 
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
            self.name.addItem(i)

        hbox1.addWidget(self.name)
        hbox1.addWidget(self.namecom)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.note = QTextEdit(self)
        self.note.resize(775, 600)
        self.note.setAlignment(Qt.AlignLeft)
        self.note.setCurrentFont(QFont('TimesNewRoman', 12))
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.note)
        vbox.addWidget(self.scroll)

        self.tegslbl = QLabel("Enter Tags:")
        self.tegslbl.resize(5, 600)
        self.tegslbl.setFont(QFont('TimesNewRoman', 12))
        self.tegslbl.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.tegslbl)

        hbox = QHBoxLayout(self)
        self.tegs = QLineEdit(self)
        self.tegs.setFont(QFont('TimesNewRoman', 12))
        hbox.addWidget(self.tegs)

        self.tegs1 = QLineEdit(self)
        self.tegs1.setFont(QFont('TimesNewRoman', 12))
        hbox.addWidget(self.tegs1)

        self.tegs2 = QLineEdit(self)
        self.tegs2.setFont(QFont('TimesNewRoman', 12))
        hbox.addWidget(self.tegs2)

        self.tegs3 = QLineEdit(self)
        self.tegs3.setFont(QFont('TimesNewRoman', 12))
        hbox.addWidget(self.tegs3)

        self.tegs4 = QLineEdit(self)
        self.tegs4.setFont(QFont('TimesNewRoman', 12))
        hbox.addWidget(self.tegs4)

        self.tegs5 = QLineEdit(self)
        self.tegs5.setFont(QFont('TimesNewRoman', 12))
        hbox.addWidget(self.tegs5)
        vbox.addLayout(hbox)

        hbox3 = QHBoxLayout(self)
        self.button2 = QPushButton("Count Words", self)
        self.button2.setFont(QFont('TimesNewRoman', 12))
        self.button2.clicked.connect(self.WCount)
        hbox3.addWidget(self.button2)
        self.label23 = QLabel("Click to count")
        self.label23.setFont(QFont('TimesNewRoman', 14))
        hbox3.addWidget(self.label23)
        hbox3.addStretch(1)
        self.button1 = QPushButton("Save", self)
        self.button1.setFont(QFont('TimesNewRoman', 12))
        self.button1.clicked.connect(self.Save)
        hbox3.addWidget(self.button1)
        vbox.addLayout(hbox3)

        if open != 0:
            self.name.setCurrentText(open)
            self.com()

    def com(self):
        search = self.name.currentText()
        sql = self.cursor.execute("""select * from Texts 
                                    where Name = "{}"
                                    and Login = "{}" """.format(search, self.login))
        list2 = []
        for i in sql.fetchall():
            for j in i:
                list2.append(j)
        self.namet.setText(list2[1])
        self.note.setText(list2[2])
        self.tegs.setText(list2[5])
        self.tegs1.setText(list2[6])
        self.tegs2.setText(list2[7])
        self.tegs3.setText(list2[8])
        self.tegs4.setText(list2[9])
        self.tegs5.setText(list2[10])

        self.update()

    def coopfile(self, nname, ttext):

        time.sleep(15)

        self.name.setText(nname)
        self.note.setText(ttext)
        self.update()

    def Save(self):

        self.nametext = self.namet.text()
        self.text = self.note.toPlainText()
        self.teg = self.tegs.text()
        self.teg1 = self.tegs1.text()
        self.teg2 = self.tegs2.text()
        self.teg3 = self.tegs3.text()
        self.teg4 = self.tegs4.text()
        self.teg5 = self.tegs5.text()
        self.namew = self.name.currentText()

        time = datetime.datetime.now()

        self.activity()

        sql = self.cursor.execute(""" UPDATE Texts 
                                    SET Name = "{}", Text = "{}", 
                                    Tegs = "{}", Tegs1 = "{}", 
                                    Tegs2 = "{}", Tegs3 = "{}", 
                                    Tegs4 = "{}", Tegs5 = "{}" 
                                    WHERE Name = "{}"
                                    and Login = "{}" """.format(self.nametext, self.text, self.teg, self.teg1,
                                                                 self.teg2, self.teg3, self.teg4, self.teg5,
                                                                 self.namew, self.login))
        self.conn.commit()

        self.SaveW = SaveW()
        self.SaveW.show()
        self.notext()

    def activity (self):
        time = datetime.datetime.now()
        count = len(self.text.split())
        self.WCount()
        self.make_goal()
        sql = self.cursor.execute("""select Text from Texts
                                           where Name = "{}"
                                           and Login = "{}" """.format(self.namew, self.login))
        self.conn.commit()
        words = str
        for i in sql.fetchall():
            for j in i:
                words = j
        count2 = len(words.split())
        if count > count2:
            sql = self.cursor.execute(""" INSERT INTO Activity (Login, Date, NumWords, GoalComplete)
                                            VALUES('{}', '{}', {}, {}) """.format(self.login, time, count - count2, self.goal))
            self.conn.commit()

    def make_goal(self):
        sql = self.cursor.execute("""SELECT WordsGoal from Goals
                                    where Login = '{}'""".format(self.login))
        self.conn.commit()

        for i in sql.fetchall():
            for j in i:
                goal = j

        self.goal = 0
        if self.WordsNum >= self.goal:
            self.goal = 1

    def notext(self):
        self.name.clear()
        self.note.clear()
        self.tegs.clear()
        self.tegs1.clear()
        self.tegs2.clear()
        self.tegs3.clear()
        self.tegs4.clear()
        self.tegs5.clear()
        self.update()
        self.close()

    def WCount (self):
        self.words = self.note.toPlainText()
        words = self.words.split()
        count = len(words)
        self.WordsNum = count
        self.label23.setText(str(count))
        self.update()


class SaveW(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(QtCore.Qt.Popup)
        self.resize(180, 50)
        self.move(600, 400)

        self.label = QLabel("File is saved.", self)

        self.label.setFont(QFont('TimesNewRoman', 18))
        self.label.setAlignment(Qt.AlignCenter)

        self.pal = self.palette()
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#FFFFFF"))
        self.setPalette(self.pal)

        vbox = QVBoxLayout()
        button = QPushButton("OK", self)
        button.clicked.connect(self.close)
        vbox.addWidget(self.label)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(button)
        vbox.addLayout(hbox)
        self.setLayout(vbox)