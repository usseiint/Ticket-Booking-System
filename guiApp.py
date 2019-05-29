from tkinter import *
import sqlite3
import tkinter.messagebox
from Cinemas import *
from tkinter import Toplevel

conn = sqlite3.connect('newDBusers.db')
c = conn.cursor()


class guiApp():
    def __init__(self, master):
        self.master = master
        self.frames = Frame(master, width=800, height=500, bg='pink')
        self.frames.pack()
        self.heading = Label(self.frames, text="CINEMA TICKETS BOOKING SYSTEM", font='arial 30 bold', fg='black',
                             bg='pink')
        self.heading.place(x=30, y=0)

        # REGISTRATION
        self.text = Label(self.frames, text="Registration", font=('arial 20 bold'), bg='pink')
        self.text.place(x=30, y=100)

        self.text2 = Label(self.frames, text="Введите логин", font=('arial 10 bold'), bg='pink')
        self.text2.place(x=30, y=160)

        self.reg_login = Entry(self.frames)
        self.reg_login.place(x=200, y=160)

        self.text3 = Label(self.frames, text="Введите пароль", font=('arial 10 bold'), bg='pink')
        self.text3.place(x=30, y=200)

        self.reg_pass = Entry(self.frames)
        self.reg_pass.place(x=200, y=200)

        self.button_registrat = Button(self.frames, text="Зарегистрироваться", font=('arial 10 bold'),
                                       command=self.saveLogPass)
        self.button_registrat.place(x=120, y=300)

        # ЛОГИН
        self.text4 = Label(self.frames, text="Login", font=('arial 20 bold'), bg='pink')
        self.text4.place(x=500, y=100)

        self.text5 = Label(self.frames, text="Введите логин", font=('arial 10 bold'), bg='pink')
        self.text5.place(x=450, y=160)

        self.login_entry = Entry(self.frames)
        self.login_entry.place(x=600, y=160)

        self.text6 = Label(self.frames, text="Введите пароль", font=('arial 10 bold'), bg='pink')
        self.text6.place(x=450, y=200)

        self.pass_entry = Entry(self.frames)
        self.pass_entry.place(x=600, y=200)

        self.button_log = Button(self.frames, text="LOGIN", font=('arial 10 bold'), command=self.Logging)
        self.button_log.place(x=500, y=300)

    def saveLogPass(self):
        self.val1 = self.reg_login.get()
        self.val2 = self.reg_pass.get()

        if self.val1 == '' or self.val2 == '':
            tkinter.messagebox.showinfo("Warning", "Please, fill up all fields!")
        else:
            # I'm adding to my database
            # Делаем INSERT запрос к базе данных
            mysql = "insert into users (login, password) values (?,?)"
            c.execute(mysql, (self.val1, self.val2))
            conn.commit()
            tkinter.messagebox.showinfo("Successful registration!", self.val1)

    def Logging(self):
        self.log = self.login_entry.get()
        self.passw = self.pass_entry.get()
        c.execute("SELECT login, password FROM users")
        # self.sql3= c.execute('SELECT password FROM users')

        # for row in c.execute('SELECT login,password FROM users'): #  print(row[0]), output : togzhan Sara Togzhan
        #         #     # print(row[1]), output: all passwords in sequence
        #         #     for i in row:
        #         #         print(i[0])

        res = []
        res = c.fetchall()
        # print(res[0]), out:  ('togzhan', '123dds')
        if self.log == '' and self.passw == '':
            tkinter.messagebox.showinfo("Fill in all fields")
        else:
            for row in res:
                if self.log in row[0] and self.passw in row[1]:
                    print("registered")
                    self.Okno()

            if self.log not in row[0] and self.passw not in row[1]:  # ????
                tkinter.messagebox.showinfo("You are not registered")

    # def ext(self):
    #     self.exit()
    #

    def Okno(self):
        self.newF = Tk()
        self.newF.geometry("1000x800")
        self.newF.title("Movies")

        # self.btn =Button(self.newF, text="EXIT", command=self.ext)
        # self.btn.pack()
        lbl = Label(self.newF, text="Which cinema would you like to choose", font=('arial 20 bold'))
        lbl.pack()

        self.cinema1 = Button(self.newF, text="Kinopark cinema", font=('arial 15 bold'), bg="pink", command=self.func1)
        self.cinema1.place(x=100, y=100)

        self.cinema2 = Button(self.newF, text="Bekmambetov cinema", font=('arial 15 bold'), bg="pink",
                              command=self.func2)
        self.cinema2.place(x=380, y=100)

        self.cinema3 = Button(self.newF, text="Chaplin cinema", font=('arial 15 bold'), bg="pink", command=self.func3)
        self.cinema3.place(x=700, y=100)

        self.lbl1 = Label(self.newF, text="Enter cinema and movie ", font=('arial 15 bold'))
        self.lbl1.place(x=400, y=450)

        self.cinemaName = Label(self.newF, text="Cinema name", font=('arial 15 bold'))
        self.cinemaName.place(x=150, y=500)
        self.cinEntry = Entry(self.newF, bg='pink')
        self.cinEntry.place(x=300, y=520)

        self.movieID = Label(self.newF, text="Movie ID", font=('arial 15 bold'))
        self.movieID.place(x=600, y=500)
        self.movieEntry = Entry(self.newF)
        self.movieEntry.place(x=700, y=520)

        self.submit = Button(self.newF, text="Submit", font=('arial 15 bold'), bg='pink', command=self.chooseFilm)
        self.submit.place(x=460, y=600)

        self.newF.mainloop()

    def func1(self):
        r = []
        c.execute("SELECT * FROM Kinopark")
        data = c.fetchall()
        numrows = int(c.rowcount)

        listbox = Listbox(self.newF, width=40, height=10, bg='pink', font='Times 16 bold italic')
        listbox.place(x=300, y=180)
        listbox.insert(END, "   MOVIE   |hall| time|price\n")
        for item in data:
            listbox.insert(END, "\n", item)

    def func2(self):
        c.execute("SELECT * FROM Bekmambetov")
        data = c.fetchall()
        listbox = Listbox(self.newF, width=40, height=10, bg='pink', font='Times 16 bold italic')
        listbox.place(x=300, y=180)
        listbox.insert(END, "  MOVIE |hall| time|price\n")
        for item in data:
            listbox.insert(END, "\n", item)

    def func3(self):
        c.execute("SELECT * FROM Chaplin")
        data = c.fetchall()
        listbox = Listbox(self.newF, width=40, height=10, bg='pink', font='Times 16 bold italic')
        listbox.place(x=300, y=180)
        listbox.insert(END, " MOVIE |hall| time|price\n")
        for item in data:
            listbox.insert(END, "\n", item)

    def chooseFilm(self):
        self.seatsPage = Tk()
        self.seatsPage.geometry("600x400")
        self.seatsPage.title("Seats")

        MODES = [
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5","5")
        ]

        v = StringVar()
        v.set("L")  # initialize
        for text, mode in MODES:
            radibtn = Radiobutton(self.seatsPage, text=text,
                                  variable=v, value=mode, indicatoron=0)
            radibtn.place(x=300,y=200)

        req = ""
        cinema_name = self.cinEntry.get()
        movie_id = self.movieEntry.get()
        seats = [] = {cinema_name, movie_id}
        if cinema_name == "Kinopark":

            req = ""
        elif cinema_name == "Bekmambetov":
            req = ""
        elif cinema_name == "Chaplin":
            req = ""

        self.seatsPage.mainloop()


root = Tk()
b = guiApp(root)
root.geometry("800x500+0+0")
root.mainloop()
