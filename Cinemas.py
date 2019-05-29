from tkinter import *

class Cinemas():

    schedule = []

    def __init__(self, cinema_name, movie_id, choice ):
        self.cinema_name=cinema_name
        self.movie_id=movie_id
        self.choice=choice

    def __init__(self,sql1, sql2,sql3):
        self.sql1=("SELECT * FROM Kinopark ")
        self.sql2=("SELECT * FROM Bekmambetov")
        self.sql3= ('SELECT * FROM Chaplin ')

    def Cinema1Func(self):
        return self.sql1

    def Cinema2Func(self):
        return self.sql2


    def Cinema3Func(self):
        return self.sql3

    def showCinemaList(self):
        pass

    # def getSeats(self, seats=[]):
    #     seats.append([0, 0, 1, 1, 0, 1, 1, 1])
    #     seats.append([0, 1, 1, 0, 0, 1, 0, 1])
    #     seats.append([1, 0, 0, 1, 0, 1, 1, 0])
    #     seats.append([0, 1, 1, 1, 0, 0, 0, 1])
    #     return seats

#
# kinopark=Cinemas("Kinopark8", ["17:30", "13:10", "15:00", "00:00"])
# bekmambetov=Cinemas("Bekmambetov Cinema", ["14:00", "18:30", "22:10", "23:00"])
# chaplin = Cinemas("Chaplin cinema", ["12:40", "20:00", "16:30", "21:00"])

