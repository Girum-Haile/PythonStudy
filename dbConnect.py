import sqlite3


class DBConnect:
    def __init__(self):
        self.db = sqlite3.connect("personalInformation.db")
        self.db.row_factory = sqlite3.Row
        self.db.execute("create table if not exists Info(Name text, Sex text, Age int)")
        self.db.commit()


def saverecord(self, name, sex, age):
    self.db.execute("insert into Info(Name, Sex, Age) values(?,?,?)", (name, sex, age))
    self.db.commit()
    print("Info added successfully")


def showdetail(self):
    show = self.db.execute("select * from Info")
    for row in show:
        print("Name:{},\tSex:{},\tAge: {}".format(row[0], row[1], row[2]))


def deleterecord(self, name):

        try:
            cursor = self.db.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from Info where name = ?"""
            cursor.execute(sql_update_query, (name,))
            self.db.commit()
            print("Record deleted successfully")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete record from a sqlite table", error)


def updaterecord(self, age, name):
    try:
        cursor = self.db.cursor()
        print("Connected to SQLite")

        sql_update_query = """update Info set age=? where name = ?"""
        data = (age, name)
        cursor.execute(sql_update_query, data)
        self.db.commit()
        print("Record updated successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update record from a sqlite table", error)


def main():
    dbc = DBConnect()
    print("------------main menu-------------")
    index = int(input("\n1/ to add info\n2/ to see detail\n3/ delete info\n4/update info\n>>"))
    if index == 1:
        name = input("enter your name: ")
        sex = input("enter your sex: ")
        age = int(input("enter your age: "))
        dbc.saverecord(name, sex, age)
        again = int(input("choose: press 4 to add another info or 5 to exit:  "))
        if again == 4:
            main()
        else:
            print("done")

    elif index == 2:
        dbc.showdetail()
        again = int(input("choose: press 4 to move to main menu or 5 to exit:  "))
        if again == 4:
            main()
        else:
            print("done")

    elif index == 3:
        name = input("enter name to delete")
        dbc.deleterecord(name)

        again = int(input("choose: press 4 to add another info or 5 to exit:  "))
        if again == 4:
            main()
        else:
            print("done")
    elif index == 4:
        name = input("enter name to update")
        age = int(input("enter the new age"))
        dbc.updaterecord(age,name)

        again = int(input("choose: press 4 to add another info or 5 to exit:  "))
        if again == 4:
            main()
        else:
            print("done")
    else:
        print("wrong input")


if __name__ == '__main__':main()












