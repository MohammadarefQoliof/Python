import time
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

location = "C:/Users/HOME/OneDrive/Desktop/Chess.com Ratings with py"
localStorage = "C:/Users/HOME/OneDrive/Desktop/Məhəmmədarif/Python LocalSotrage/Blitz Rating"

myRatingList = location + "/Blitz Rating.txt"
currentRatingStorage = localStorage + "/Current Rating Blitz.txt"
dayNumStorage = localStorage + "/Number Of Day Blitz.txt"
oneWeekResultLocation = localStorage + "/One Week Result Blitz.txt"

weekNumStorage = localStorage + "/Number Of Week Blitz.txt"
everyWeekRatingLocation = location + "/Weekly rating/Blitz Weekly Rating.txt"

myPassword = "1006"
password = simpledialog.askinteger("Password", "Enter the Password")

if str(password) == myPassword:
    messagebox.showinfo("Alright", "Password Is Correct")

    with open(myRatingList, "r") as ratingListRead:
            myRatingListInfo = ratingListRead.read()

    if myRatingListInfo == "":
        with open(myRatingList, "w") as emptyRatingList:
            with open(currentRatingStorage, "r") as currentRatingFile:
                myCurrentRating = int(currentRatingFile.read())
            emptyRatingList.write(f"Previous Rating: {myCurrentRating}\n\n")

    inputRating = simpledialog.askinteger("Rating Calculate", "Enter your current rating")

    with open(oneWeekResultLocation, "r") as oneMonthResult:
        result = int(oneMonthResult.read())

    with open(dayNumStorage, "r") as dayNum:
        num = int(dayNum.read())

    with open(currentRatingStorage, "r") as myRating:
        currentRating = myRating.read()

    with open(myRatingList, "a") as file:
        if inputRating is not None:
            file.write(f"Day {num}: {inputRating}\n")
            onlyRating = int(inputRating) - int(currentRating)
            result += onlyRating
            messagebox.showinfo("Today's Gained Rating", f"Today you gained {onlyRating} Rating")
            file.write(f"Gained rating: {onlyRating}\n\n")
            currentRating = inputRating
            num += 1
            with open(currentRatingStorage, "w") as myNewRating:
                myNewRating.write(str(currentRating))
            with open(dayNumStorage, "w") as newDayNum:
                newDayNum.write(str(num))
            with open(oneWeekResultLocation, "w") as newOneWeekResult:
                newOneWeekResult.write(str(result))
            print("Done")
        else:
            print("Typing the rating canceled!")
            time.sleep(2)

    if num > 7:
        messagebox.showinfo("1 Week Completed", f"The Blitz rating you gained in 1 week: {result}")
        messagebox.showinfo("Current Rating", f"Your current Blitz rating: {currentRating}")
        with open(myRatingList, "w") as ratingList:
            ratingList.write("")
        with open(weekNumStorage, "r") as weekNum:
            numOfWeek = int(weekNum.read())
        with open(oneWeekResultLocation, "r") as theResult:
            result = int(theResult.read())
        with open(everyWeekRatingLocation, "a") as everyWeekRating:
            everyWeekRating.write(f"Week {numOfWeek}: {result}\n\n")
        result = 0
        with open(oneWeekResultLocation, "w") as newOneWeekResult:
            newOneWeekResult.write(str(result))
        numOfWeek += 1
        with open(weekNumStorage, "w") as newWeekNum:
            newWeekNum.write(str(numOfWeek))
        with open(dayNumStorage, "r") as dayNum:
            numOfDay = int(dayNum.read())
        numOfDay = 1
        with open(dayNumStorage, "w") as newDayNum:
            newDayNum.write(str(numOfDay))
else:
    if password is None:
        print("Canceled")
        time.sleep(2)
    else:
        messagebox.showinfo("Failed", "Password Is Wrong")