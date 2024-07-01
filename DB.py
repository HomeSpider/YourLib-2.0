import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("geschloss.db")
        self.cursor = self.conn.cursor()

        sql = self.cursor.execute(
            """ create table if not exists Users (
                    ID integer primary key autoincrement, Login Text, Password Text)""")
        self.conn.commit()

        sql = self.cursor.execute(
            """ create table if not exists Texts (
                    ID integer primary key autoincrement, Name Text, Text Text, Date Text, Login Text, Tegs Text, Tegs1 Text, Tegs2 Text, Tegs3 Text, Tegs4 Text, Tegs5 Text)""")
        self.conn.commit()

        sql = self.cursor.execute(
            """ create table if not exists Activity (
                    ID integer primary key autoincrement, Login Text,  Date Text, NumWords Integer, GoalComplete Integer)""")
        self.conn.commit()

        sql = self.cursor.execute(
            """ create table if not exists Activity (
                    ID integer primary key autoincrement, Login Text,  Date Text, NumWords Integer)""")
        self.conn.commit()

        sql = self.cursor.execute(
            """ create table if not exists Goals (
                    ID integer primary key autoincrement, Login Text,  WordsGoal Integer, DayGoal Integer,
                    WordsPay Integer, SumPay Integer)""")
        self.conn.commit()

        sql = self.cursor.execute(
            """ create table if not exists Advises (
                    ID integer primary key autoincrement, Login Text, Advise Text  )""")
        self.conn.commit()

        sql = self.cursor.execute("""select * from Advises""")
        if len(sql.fetchall()) == 0:
            self.adlist()

    def adlist (self):
        adlist = ["We cannot solve problems with the kind of thinking we employed when we came up with them.",
                  "Learn as if you will live forever, live like you will die tomorrow.",
                  "Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.",
                  "Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.",
                  "When you change your thoughts, remember to also change your world.",
                  "It is only when we take chances, when our lives improve. The initial and the most difficult risk that we need to take is to become honest.",
                  "It is only when we take chances, when our lives improve. The initial and the most difficult risk that we need to take is to become honest.",
                  "Success is not final; failure is not fatal: It is the courage to continue that counts.",
                  "It is better to fail in originality than to succeed in imitation.",
                  "The road to success and the road to failure are almost exactly the same.",
                  "Success usually comes to those who are too busy looking for it.",
                  "Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.",
                  "There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind.",
                  "Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.",
                  "I never dreamed about success. I worked for it.",
                  "Success is getting what you want, happiness is wanting what you get.",
                  "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.",
                  "Don’t let yesterday take up too much of today.",
                  "You learn more from failure than from success. Don’t let it stop you. Failure builds character.",
                  "If you are working on something that you really care about, you don’t have to be pushed. The vision pulls you.",
                  "Experience is a hard teacher because she gives the test first, the lesson afterwards.",
                  "To know how much there is to know is the beginning of learning to live.",
                  "Goal setting is the secret to a compelling future.",
                  "Concentrate all your thoughts upon the work in hand. The sun’s rays do not burn until brought to a focus.",
                  "Either you run the day or the day runs you.",
                  "I’m a greater believer in luck, and I find the harder I work the more I have of it.",
                  "When we strive to become better than we are, everything around us becomes better too.",
                  "Opportunity is missed by most people because it is dressed in overalls and looks like work.",
                  "Setting goals is the first step in turning the invisible into the visible.",
                  "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle. As with all matters of the heart, you’ll know when you find it.",
                  "It’s not about better time management. It’s about better life management.",
                  "You’ve got to get up every morning with determination if you’re going to go to bed with satisfaction.",
                  "Education is the most powerful weapon which you can use to change the world.",
                  "The most difficult thing is the decision to act, the rest is merely tenacity.",
                  "You’ll find that education is just about the only thing lying around loose in this world, and it’s about the only thing a fellow can have as much of as he’s willing to haul away.",
                  "Take the attitude of a student, never be too big to ask questions, never know too much to learn something new.",
                  "The elevator to success is out of order. You’ll have to use the stairs, one step at a time.",
                  "People often say that motivation doesn’t last. Well, neither does bathing – that’s why we recommend it daily.",
                  "Work until your bank account looks like a phone number.",
                  "I am so clever that sometimes I don’t understand a single word of what I am saying.",
                  "People say nothing is impossible, but I do nothing every day.",
                  "Life is like a sewer… what you get out of it depends on what you put into it.",
                  "I always wanted to be somebody, but now I realise I should have been more specific.",
                  "Just one small positive thought in the morning can change your whole day.",
                  "Opportunities don’t happen, you create them.",
                  "Love your family, work super hard, live your passion.",
                  "It is never too late to be what you might have been.",
                  "Don’t let someone else’s opinion of you become your reality",
                  "If you’re not positive energy, you’re negative energy.",
                  "I am not a product of my circumstances. I am a product of my decisions.",
                  "Do the best you can. No one can do more than that.",
                  "If you can dream it, you can do it.",
                  "Do what you can, with what you have, where you are.",
                  "Don’t look at your feet to see if you are doing it right. Just dance",
                  "Someone’s sitting in the shade today because someone planted a tree a long time ago.",
                  "True freedom is impossible without a mind made free by discipline.",
                  "Rivers know this: there is no hurry. We shall get there some day.",
                  "There is a vitality, a life force, an energy, a quickening that is translated through you into action, and because there is only one of you in all time, this expression is unique. And if you block it, it will never exist through any other medium and will be lost.",
                  "Small is not just a stepping-stone. Small is a great destination itself.",
                  "He that can have patience can have what he will.",
                  "The only one who can tell you «you can’t win» is you and you don’t have to listen.",
                  "Set your goals high, and don’t stop till you get there.",
                  "Take your victories, whatever they may be, cherish them, use them, but don’t settle for them.",
                  "If you don’t risk anything, you risk even more."]

        login = "admin"
        for i in adlist:
            sql = self.cursor.execute(""" INSERT INTO Advises (Login, Advise)
                             VALUES('{}', '{}') """.format(login, i))
            self.conn.commit()


