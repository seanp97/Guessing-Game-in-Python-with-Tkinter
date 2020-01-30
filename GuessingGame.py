from tkinter import *
import sys
import tkinter
import random

def GetVal():
    try:
        global GuessNum
        GuessVal = Entry.get(GuessEnt)
        GuessVal = int(GuessVal)
        GuessMax.configure(text="Highest value of random number is " + str(GuessVal))
        GuessNum = random.randrange(1, (GuessVal + 1))
    except:
        if GuessVal == "" or type(GuessVal) == str:
            ErrorLabel.configure(text="Please add in a number")
        else:
            ErrorLabel.configure(text="An error occured")
            
def UserGuess():  
    try:
        UserGuess = Entry.get(UserEnt)
        UserGuess = int(UserGuess)  
        if UserGuess > GuessNum:
            EndLabel.configure(text="Guess a bit lower")
        elif UserGuess < GuessNum:
            EndLabel.configure(text="Guess a bit higher")
        else:
            EndLabel.configure(text="Correct! The answer was " + str(GuessNum))
            GuessEnt.delete(first=0, last=100)
            UserEnt.delete(first=0, last=100) 
    except:
        if UserGuess == "" or type(UserGuess) == str:
            ErrorLabel.configure(text="Please add in a number")
        else:
            ErrorLabel.configure(text="An error occured")
        
               
app = Tk()
app.configure(bg="#ccffff")
app.geometry("800x400")
app.title("Guessing Game")

LabelOne = Label(app, text="Random Guessing Game", pady=20, padx=20, font=("Times New Roman", 12, "bold"), bg="#ccffff")
LabelOne.grid(column=0, row=0)

LabelTwo = Label(app, text="How high do you want to guess?", pady=20, padx=20, font=("Times New Roman", 12, "bold"), bg="#ccffff")
LabelTwo.grid(column=0, row=1)
GuessEnt = Entry(app, bd=5)
GuessEnt.grid(column=1, row=1)
GuessBtn = Button(app, bd=5, text="Submit", command=GetVal)
GuessBtn.grid(column=2, row=1)
GuessMax = Label(app, text="Highest value of random number is undefined", pady=20, padx=20, font=("Times New Roman", 12, "bold"), bg="#ccffff")
GuessMax.grid(column=3, row=1)

UserLabel = Label(app, text="Your Guess", font=("Times New Roman", 12, "bold"), pady=20, padx=20, bg="#ccffff")
UserLabel.grid(column=0, row=2)
UserEnt = Entry(app, bd=5)
UserEnt.grid(column=1, row=2)
UserBtn = Button(app, bd=5, text="Guess", command=UserGuess)
UserBtn.grid(column=2, row=2)

EndLabel = Label(app, text="Guessing Game", font=("Times New Roman", 12, "bold"), pady=20, padx=20, bg="#ccffff")
EndLabel.grid(column=0, row=3, pady=20, padx=20)

ErrorLabel = Label(app, text="", font=("Times New Roman", 12, "bold"), pady=20, padx=20, bg="#ccffff")
ErrorLabel.grid(column=0, row=4)

app.mainloop()