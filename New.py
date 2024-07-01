import pyqtgraph.examples, sqlite3

#pyqtgraph.examples.run()

#conn = sqlite3.connect("geschloss.db")
#cursor = conn.cursor()

"""list1 = [
("FlyingThinker", "2023-01-01 15:02:33.035383", 771, 0),
("FlyingThinker", "2023-01-02 15:02:33.035383", 941, 0), 
("FlyingThinker", "2023-01-03 15:02:33.035383", 604, 0), 
("FlyingThinker", "2023-01-04 15:02:33.035383", 635, 0),
("FlyingThinker", "2023-01-05 15:02:33.035383", 1042, 1), 
("FlyingThinker", "2023-01-06 15:02:33.035383", 381, 0), 
("FlyingThinker", "2023-01-07 15:02:33.035383", 815, 0),
("FlyingThinker", "2023-01-08 15:02:33.035383", 580, 0), 
("FlyingThinker", "2023-01-09 15:02:33.035383", 1036, 1), 
("FlyingThinker", "2023-01-10 15:02:33.035383", 1025, 1), 
("FlyingThinker", "2023-01-11 15:02:33.035383", 1064, 1), 
("FlyingThinker", "2023-01-12 15:02:33.035383", 1282, 1), 
("FlyingThinker", "2023-01-13 15:02:33.035383", 591, 0),
("FlyingThinker", "2023-01-14 15:02:33.035383", 917, 0), 
("FlyingThinker", "2023-01-15 15:02:33.035383", 1711, 1), 
("FlyingThinker", "2023-01-16 15:02:33.035383", 1055, 1), 
("FlyingThinker", "2023-01-17 15:02:33.035383", 1471, 1), 
("FlyingThinker", "2023-01-18 15:02:33.035383", 0, 0),
("FlyingThinker", "2023-01-19 15:02:33.035383", 1510, 1), 
("FlyingThinker", "2023-01-20 15:02:33.035383", 2014, 1),
("FlyingThinker", "2023-01-21 15:02:33.035383", 1276, 1), 
("FlyingThinker", "2023-01-22 15:02:33.035383", 1608, 1), 
("FlyingThinker", "2023-01-23 15:02:33.035383", 1004, 1),
("FlyingThinker", "2023-01-24 15:02:33.035383", 1395, 1), 
("FlyingThinker", "2023-01-25 15:02:33.035383", 512, 0), 
("FlyingThinker", "2023-01-26 15:02:33.035383", 1963, 1),
("FlyingThinker", "2023-01-27 15:02:33.035383", 1240, 1), 
("FlyingThinker", "2023-01-28 15:02:33.035383", 1327, 1), 
("FlyingThinker", "2023-01-29 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-01-30 15:02:33.035383", 606, 0),
("FlyingThinker", "2023-01-31 15:02:33.035383", 1054, 1),
("FlyingThinker", "2023-02-01 15:02:33.035383", 526, 0),
("FlyingThinker", "2023-02-02 15:02:33.035383", 2054, 1), 
("FlyingThinker", "2023-02-03 15:02:33.035383", 1036, 1), 
("FlyingThinker", "2023-02-04 15:02:33.035383", 0, 0),
("FlyingThinker", "2023-02-05 15:02:33.035383", 1019, 1), 
("FlyingThinker", "2023-02-06 15:02:33.035383", 495, 0), 
("FlyingThinker", "2023-02-07 15:02:33.035383", 1025, 1),
("FlyingThinker", "2023-02-08 15:02:33.035383", 1052, 1), 
("FlyingThinker", "2023-02-09 15:02:33.035383", 1997, 1), 
("FlyingThinker", "2023-02-10 15:02:33.035383", 628, 0), 
("FlyingThinker", "2023-02-11 15:02:33.035383", 435, 0), 
("FlyingThinker", "2023-02-12 15:02:33.035383", 725, 0), 
("FlyingThinker", "2023-02-13 15:02:33.035383", 1811, 1),
("FlyingThinker", "2023-02-14 15:02:33.035383", 1889, 1), 
("FlyingThinker", "2023-02-15 15:02:33.035383", 2049, 1), 
("FlyingThinker", "2023-02-16 15:02:33.035383", 1466, 1), 
("FlyingThinker", "2023-02-17 15:02:33.035383", 1617, 1), 
("FlyingThinker", "2023-02-18 15:02:33.035383", 0, 0),
("FlyingThinker", "2023-02-19 15:02:33.035383", 1175, 1), 
("FlyingThinker", "2023-02-20 15:02:33.035383", 1840, 1),
("FlyingThinker", "2023-02-21 15:02:33.035383", 388, 0), 
("FlyingThinker", "2023-02-22 15:02:33.035383", 596, 0), 
("FlyingThinker", "2023-02-23 15:02:33.035383", 1222, 1),
("FlyingThinker", "2023-02-24 15:02:33.035383", 1102, 1), 
("FlyingThinker", "2023-02-25 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-02-26 15:02:33.035383", 1065, 1),
("FlyingThinker", "2023-02-27 15:02:33.035383", 480, 0), 
("FlyingThinker", "2023-02-28 15:02:33.035383", 0, 0),
("FlyingThinker", "2023-03-01 15:02:33.035383", 624, 0),
("FlyingThinker", "2023-03-02 15:02:33.035383", 1019, 1), 
("FlyingThinker", "2023-03-03 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-03-04 15:02:33.035383", 1039, 1),
("FlyingThinker", "2023-03-05 15:02:33.035383", 1300, 1), 
("FlyingThinker", "2023-03-06 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-03-07 15:02:33.035383", 1005, 1),
("FlyingThinker", "2023-03-08 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-03-09 15:02:33.035383", 1033, 1), 
("FlyingThinker", "2023-03-10 15:02:33.035383", 789, 0), 
("FlyingThinker", "2023-03-11 15:02:33.035383", 1006, 1), 
("FlyingThinker", "2023-03-12 15:02:33.035383", 712, 0), 
("FlyingThinker", "2023-03-13 15:02:33.035383", 831, 0),
("FlyingThinker", "2023-03-14 15:02:33.035383", 1007, 1), 
("FlyingThinker", "2023-03-15 15:02:33.035383", 599, 0), 
("FlyingThinker", "2023-03-16 15:02:33.035383", 607, 0),
("FlyingThinker", "2023-03-17 15:02:33.035383", 1347, 1), 
("FlyingThinker", "2023-03-18 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-03-19 15:02:33.035383", 455, 0), 
("FlyingThinker", "2023-03-20 15:02:33.035383", 1000, 1),
("FlyingThinker", "2023-03-21 15:02:33.035383", 340, 0), 
("FlyingThinker", "2023-03-22 15:02:33.035383", 1143, 1), 
("FlyingThinker", "2023-03-23 15:02:33.035383", 1003, 1),
("FlyingThinker", "2023-03-24 15:02:33.035383", 1135, 1), 
("FlyingThinker", "2023-03-25 15:02:33.035383", 1032, 1), 
("FlyingThinker", "2023-03-26 15:02:33.035383", 1039, 1),
("FlyingThinker", "2023-03-27 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-03-28 15:02:33.035383", 1040, 1), 
("FlyingThinker", "2023-03-29 15:02:33.035383", 1012, 1), 
("FlyingThinker", "2023-03-30 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-03-31 15:02:33.035383", 1028, 1),
("FlyingThinker", "2023-04-01 15:02:33.035383", 1018, 1),
("FlyingThinker", "2023-04-02 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-04-03 15:02:33.035383", 1042, 1), 
("FlyingThinker", "2023-04-04 15:02:33.035383", 1019, 1),
("FlyingThinker", "2023-04-05 15:02:33.035383", 1039, 1), 
("FlyingThinker", "2023-04-06 15:02:33.035383", 1034, 1), 
("FlyingThinker", "2023-04-07 15:02:33.035383", 1018, 1),
("FlyingThinker", "2023-04-08 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-04-09 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-04-10 15:02:33.035383", 785, 0), 
("FlyingThinker", "2023-04-11 15:02:33.035383", 1079, 1), 
("FlyingThinker", "2023-04-12 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-04-13 15:02:33.035383", 1031, 1),
("FlyingThinker", "2023-04-14 15:02:33.035383", 1006, 1), 
("FlyingThinker", "2023-04-15 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-04-16 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-04-17 15:02:33.035383", 0, 0), 
("FlyingThinker", "2023-04-18 15:02:33.035383", 1586, 1),
("FlyingThinker", "2023-04-19 15:02:33.035383", 1035, 1), 
("FlyingThinker", "2023-04-20 15:02:33.035383", 1030, 1),
("FlyingThinker", "2023-04-21 15:02:33.035383", 1118, 1), 
("FlyingThinker", "2023-04-22 15:02:33.035383", 1059, 1), 
("FlyingThinker", "2023-04-23 15:02:33.035383", 1109, 1),
("FlyingThinker", "2023-04-24 15:02:33.035383", 1062, 1), 
("FlyingThinker", "2023-04-25 15:02:33.035383", 1013, 1), 
("FlyingThinker", "2023-04-26 15:02:33.035383", 1060, 1),
("FlyingThinker", "2023-04-27 15:02:33.035383", 1046, 1), 
("FlyingThinker", "2023-04-28 15:02:33.035383", 1244, 1), 
("FlyingThinker", "2023-04-29 15:02:33.035383", 1110, 1), 
("FlyingThinker", "2023-04-30 15:02:33.035383", 0, 0),
("FlyingThinker", "2023-05-01 15:02:33.035383", 1050, 1),
("FlyingThinker", "2023-05-02 15:02:33.035383", 1066, 1), 
 ("FlyingThinker", "2023-05-03 15:02:33.035383", 1078, 1), 
("FlyingThinker", "2023-05-04 15:02:33.035383", 1349, 1),
("FlyingThinker", "2023-05-05 15:02:33.035383", 1155, 1), 
("FlyingThinker", "2023-05-06 15:02:33.035383", 1014, 1), 
("FlyingThinker", "2023-05-07 15:02:33.035383", 1029, 1),
("FlyingThinker", "2023-05-08 15:02:33.035383", 1313, 1), 
("FlyingThinker", "2023-05-09 15:02:33.035383", 1208, 1), 
("FlyingThinker", "2023-05-10 15:02:33.035383", 1073, 1), 
("FlyingThinker", "2023-05-11 15:02:33.035383", 1632, 1), 
("FlyingThinker", "2023-05-12 15:02:33.035383", 1331, 1), 
("FlyingThinker", "2023-05-13 15:02:33.035383", 460, 0),
("FlyingThinker", "2023-05-14 15:02:33.035383", 673, 0), 
("FlyingThinker", "2023-05-15 15:02:33.035383", 1053, 1), 
("FlyingThinker", "2023-05-16 15:02:33.035383", 1213, 1), 
("FlyingThinker", "2023-05-17 15:02:33.035383", 1149, 1), 
("FlyingThinker", "2023-05-18 15:02:33.035383", 1056, 1),
("FlyingThinker", "2023-05-19 15:02:33.035383", 702, 0), 
("FlyingThinker", "2023-05-20 15:02:33.035383", 1310, 1),
("FlyingThinker", "2023-05-21 15:02:33.035383", 930, 0), 
("FlyingThinker", "2023-05-22 15:02:33.035383", 1022, 1), 
("FlyingThinker", "2023-05-23 15:02:33.035383", 1050, 1),
("FlyingThinker", "2023-05-24 15:02:33.035383", 1093, 1)
]"""

#sql = cursor.execute(""" INSERT INTO Goals (Login, WordsGoal, DayGoal, WordsPay, SumPay)
#                                     VALUES('{}', {}, {}, {}, {})""".format("FlyingThinker", 1000, 0, 0, 0))
#conn.commit()

#UPDATE SQLITE_SEQUENCE SET seq = <n> WHERE name = '<table>'

#for i in list1:
#    sql = cursor.execute(""" INSERT INTO Activity (Login, Date, NumWords, GoalComplete)
#                                            VALUES('{}', '{}', {}, {}) """.format(i[0], i[1], i[2], i[3]))
#    conn.commit()
#sql = cursor.execute(""" select Date, NumWords from Activity
#                                                                where Login = '{}'""".format("Spectra"))

"""
k = 1
day = "25"
year = "2023"
month = "04"
counter = int(day)
words = []
nums = []
today = 0
worklist = sql.fetchall()
worklist.reverse()

"""

"""for i in worklist:
    print(i)
    counter = str(counter)
    print(i[0][8:-16], counter)
    while i[0][:4] == year and i[0][5:-19] == month and i[0][8:-16] == counter:
            today += i[1]
            print(today, counter)
    words.append(today)
    today = 0
    counter = int(counter)
    nums.append(counter)
    counter = counter - 1
    k += 1
    if k == 8:
        break
print(words, nums)"""

"""n = 0

for i in range(1,8):
    nums.append(counter)
    counter -= 1
for i in worklist:
    print(i)
    if i[0][:4] == year and i[0][5:-19] == month and i[0][8:-16] == str(nums[n]):
        today += i[1]
    print(today)
    n += 1
print(nums)"""

#sql = cursor.execute("""select Date, NumWords from Activity where Login = '{}'""".format("Spectra"))
"""conn.commit()

worklist = sql.fetchall()
list = worklist[-1]
print(list)

if list[1][:4] == year and list[0][5:-19] == month and list[0][8:-16] == day:
    pass
else:
    day = int(day) - 1
    """

