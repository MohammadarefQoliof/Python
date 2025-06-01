import time
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

localStorage = "C:/Users/HOME/OneDrive/Desktop/Məhəmmədarif/Python LocalSotrage/Rapid Winning number"
winNumLocation = localStorage + "/Win Number For Rapid.txt"
setWinNumber = localStorage + "/Set Win Number.txt"

with open(setWinNumber, "r") as setWinNum:
    theSetWinNum = int(setWinNum.read())

if theSetWinNum <= 0:
    askSetNum = simpledialog.askinteger("Setting Number", "Set your targeted point number")
    if askSetNum is not None:
        with open(setWinNumber, "w") as newSetNum:
            newSetNum.write(str(askSetNum))
    else:
        print("Canceled")
        time.sleep(2)
else:
    with open(winNumLocation, "r") as winningNum:
        winNum = int(winningNum.read())

    winOrLoseQuestion = messagebox.askquestion("win or lose", "Did you win?")
    if winOrLoseQuestion == "yes":
        winNum += 1
        with open(winNumLocation, "w") as newWinningNum:
            newWinningNum.write(str(winNum))
        messagebox.showinfo("YOU WON", f"You have {winNum} points")
    elif winOrLoseQuestion == "no":
        winNum -= 1
        with open(winNumLocation, "w") as newWinningNum:
            newWinningNum.write(str(winNum))
        messagebox.showinfo("YOU LOSE", f"You have {winNum} points")
    else:
        print("Invalid input")

    with open(winNumLocation, "r") as winNum:
        winNum = winNum.read()

    with open(setWinNumber, "r") as setWinNum:
        theSetWinNum = setWinNum.read()

    if winNum >= theSetWinNum:
        messagebox.showinfo("WELL DONE", f"You reached to your goal. You have {winNum} points")
        winNum = 0
        theSetWinNum = 0
        with open(winNumLocation, "w") as restartedWinNum:
            restartedWinNum.write(str(winNum))
        with open(setWinNumber, "w") as theNewWinNumber:
            theNewWinNumber.write(str(theSetWinNum))