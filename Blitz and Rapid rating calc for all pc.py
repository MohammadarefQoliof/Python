import tkinter as tk
import os
from tkinter import simpledialog, messagebox, filedialog

root = tk.Tk()
root.geometry("300x230+550+300")
root.title("Rating Calculator")



def Blitz():

    root.withdraw()
    try:
        with open("C:/ProgramData/testfile.txt", "x") as f:
            print("Created")
    except FileExistsError:
        print("Already exists")

    def selectFilePath():
        path = filedialog.askdirectory(title="Select where to store rating list")
        with open("C:/ProgramData/testfile.txt", "w") as filePath:
            filePath.write(path)
        return path

    def checkFilePath():
        try:
            with open("C:/ProgramData/testfile.txt", "r") as file:
                saved_path = file.read()
            if saved_path == "":
                return selectFilePath()
            return saved_path
        except FileNotFoundError:
            return selectFilePath()
        
    location = checkFilePath()
    localStorage = "C:/ProgramData"

    myRatingList = location + "/Blitz Rating.txt"
    currentRatingStorage = localStorage + "/Current Rating Blitz.txt"
    dayNumStorage = localStorage + "/Number Of Day Blitz.txt"
    oneWeekResultLocation = localStorage + "/One Week Result Blitz.txt"

    weekNumStorage = localStorage + "/Number Of Week Blitz.txt"
    everyWeekRatingLocation = location + "/Blitz Weekly Rating.txt"
    if location != "":
        try:
            with open(myRatingList, "x") as f:
                print("Created")
        except FileExistsError:
            print("Already exists")
        
        try:
            with open(everyWeekRatingLocation, "x") as f:
                print("Created")
        except FileExistsError:
            print("Already exists")

        try:
            with open(currentRatingStorage, "x") as f:
                print("Created")
        except FileExistsError:
            print("Already exists")

        try:
            with open(dayNumStorage, "x") as f:
                print("Created")
        except FileExistsError:
            print("Already exists")

        try:
            with open(oneWeekResultLocation, "x") as f:
                print("Created")
        except FileExistsError:
            print("Already exists")

        try:
            with open(weekNumStorage, "x") as f:
                print("Created")
        except FileExistsError:
            print("Already exists")

        with open(dayNumStorage, "r+") as ratingListRead:
            myRatingListInfo = ratingListRead.read()
            if myRatingListInfo == "":
                ratingListRead.write("1")

        with open(oneWeekResultLocation, "r+") as ratingListRead:
            myRatingListInfo = ratingListRead.read()
            if myRatingListInfo == "":
                ratingListRead.write("0")

        with open(currentRatingStorage, "r+") as ratingListRead:
            myRatingListInfo = ratingListRead.read()
            if myRatingListInfo == "":
                curRating = simpledialog.askinteger("Current Rating", "What is your rating? It is first time I should know your rating")
                if curRating is not None:
                    ratingListRead.write(str(curRating))
                else:
                    messagebox.showwarning("Canceled", "Typing canceled")

        with open(weekNumStorage, "r+") as ratingListRead:
            myRatingListInfo = ratingListRead.read()
            if myRatingListInfo == "":
                ratingListRead.write("1")


        root.deiconify()

        inputRating = simpledialog.askinteger("Rating Calculate", "Enter your current rating")

        with open(oneWeekResultLocation, "r") as oneWeekResult:
            result = int(oneWeekResult.read())

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
                messagebox.showwarning("Cancel", "Typing canceled")

        if num > 7:
            messagebox.showinfo("1 Week Completed", f"The Blitz rating you gained in 1 week: {result}")
            messagebox.showinfo("Current Rating", f"Your current Blitz rating: {currentRating}")
            with open(myRatingList, "w") as ratingList:
                with open(currentRatingStorage, "r") as currentRatingFile:
                    myCurrentRating = int(currentRatingFile.read())
                ratingList.write(f"Previous Rating: {myCurrentRating}\n\n")
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
        messagebox.showwarning("Warning", "No location is selected")

def Rapid():

    root.withdraw()
    try:
        with open("C:/ProgramData/testfile.txt", "x") as f:
            print("Created")
    except FileExistsError:
        print("Already exists")

    def selectFilePath():
        path = filedialog.askdirectory(title="Select where to store rating list")
        with open("C:/ProgramData/testfile.txt", "w") as filePath:
            filePath.write(path)
        return path

    def checkFilePath():
        try:
            with open("C:/ProgramData/testfile.txt", "r") as file:
                saved_path = file.read()
            if saved_path == "":
                return selectFilePath()
            return saved_path
        except FileNotFoundError:
            return selectFilePath()
        
    location = checkFilePath()
    localStorage = "C:/ProgramData"

    myRatingList = location + "/Rapid Rating.txt"
    currentRatingStorage = localStorage + "/Current Rating Rapid.txt"
    dayNumStorage = localStorage + "/Number Of Day Rapid.txt"
    oneWeekResultLocation = localStorage + "/One Week Result Rapid.txt"

    weekNumStorage = localStorage + "/Number Of Week Rapid.txt"
    everyWeekRatingLocation = location + "/Rapid Weekly Rating.txt"

    if location != "":
        try:
            with open(myRatingList, "x") as f:
                print("Created")
        except FileExistsError:
            print("Already exists")
        
        try:
            with open(everyWeekRatingLocation, "x") as f:
                print("Created")
        except FileExistsError:
            print("Already exists")

        try:
            with open(currentRatingStorage, "x") as f:
                print("Created")
        except FileExistsError:
            print("Already exists")

        try:
            with open(dayNumStorage, "x") as f:
                print("Created")
        except FileExistsError:
            print("Already exists")

        try:
            with open(oneWeekResultLocation, "x") as f:
                print("Created")
        except FileExistsError:
            print("Already exists")

        try:
            with open(weekNumStorage, "x") as f:
                print("Created")
        except FileExistsError:
            print("Already exists")

        with open(dayNumStorage, "r+") as ratingListRead:
            myRatingListInfo = ratingListRead.read()
            if myRatingListInfo == "":
                ratingListRead.write("1")

        with open(oneWeekResultLocation, "r+") as ratingListRead:
            myRatingListInfo = ratingListRead.read()
            if myRatingListInfo == "":
                ratingListRead.write("0")

        with open(currentRatingStorage, "r+") as ratingListRead:
            myRatingListInfo = ratingListRead.read()
            if myRatingListInfo == "":
                curRating = simpledialog.askinteger("Current Rating", "What is your rating? It is first time I should know your rating")
                if curRating is not None:
                    ratingListRead.write(str(curRating))
                else:
                    messagebox.showwarning("Canceled", "Typing canceled")

        with open(weekNumStorage, "r+") as ratingListRead:
            myRatingListInfo = ratingListRead.read()
            if myRatingListInfo == "":
                ratingListRead.write("1")


        root.deiconify()

        inputRating = simpledialog.askinteger("Rating Calculate", "Enter your current rating")

        with open(oneWeekResultLocation, "r") as oneWeekResult:
            result = int(oneWeekResult.read())

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
                messagebox.showwarning("Cancel", "Typing canceled")

        if num > 7:
            messagebox.showinfo("1 Week Completed", f"The Rapid rating you gained in 1 week: {result}")
            messagebox.showinfo("Current Rating", f"Your current Rapid rating: {currentRating}")
            with open(myRatingList, "w") as ratingList:
                with open(currentRatingStorage, "r") as currentRatingFile:
                    myCurrentRating = int(currentRatingFile.read())
                ratingList.write(f"Previous Rating: {myCurrentRating}\n\n")
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
        messagebox.showwarning("Warning", "No location is selected")

def resetHistory():
    acceptFunc = messagebox.askyesno("Remove All Data", "Are you sure to reset the files?")

    if acceptFunc:
        localStorage = "C:/ProgramData"
        currentRatingStorage = localStorage + "/Current Rating Blitz.txt"
        dayNumStorage = localStorage + "/Number Of Day Blitz.txt"
        oneWeekResultLocation = localStorage + "/One Week Result Blitz.txt"
        weekNumStorage = localStorage + "/Number Of Week Blitz.txt"

        currentRatingStorageRapid = localStorage + "/Current Rating Rapid.txt"
        dayNumStorageRapid = localStorage + "/Number Of Day Rapid.txt"
        oneWeekResultLocationRapid = localStorage + "/One Week Result Rapid.txt"
        weekNumStorageRapid = localStorage + "/Number Of Week Rapid.txt"

        if os.path.exists("C:/ProgramData/testfile.txt"):

            with open("C:/ProgramData/testfile.txt", "r") as RatingListsLocation:
                location = RatingListsLocation.read()

            myRatingList = location + "/Blitz Rating.txt"
            everyWeekRatingLocation = location + "/Blitz Weekly Rating.txt"
            myRatingListRapid = location + "/Rapid Rating.txt"
            everyWeekRatingLocationRapid = location + "/Rapid Weekly Rating.txt"

            if os.path.exists(currentRatingStorage):
                os.remove(currentRatingStorage)
                print("Removed")
            else:
                print("File not created yet")

            if os.path.exists(dayNumStorage):
                os.remove(dayNumStorage)
                print("Removed")
            else:
                print("File not created yet")

            if os.path.exists(oneWeekResultLocation):
                os.remove(oneWeekResultLocation)
                print("Removed")
            else:
                print("File not created yet")
            
            if os.path.exists(weekNumStorage):
                os.remove(weekNumStorage)
                print("Removed")
            else:
                print("File not created yet")
            
            if os.path.exists(currentRatingStorageRapid):
                os.remove(currentRatingStorageRapid)
                print("Removed")
            else:
                print("File not created yet")

            if os.path.exists(dayNumStorageRapid):
                os.remove(dayNumStorageRapid)
                print("Removed")
            else:
                print("File not created yet")

            if os.path.exists(oneWeekResultLocationRapid):
                os.remove(oneWeekResultLocationRapid)
                print("Removed")
            else:
                print("File not created yet")
            
            if os.path.exists(weekNumStorageRapid):
                os.remove(weekNumStorageRapid)
                print("Removed")
            else:
                print("File not created yet")
            
            if os.path.exists("C:/ProgramData/testfile.txt"):
                os.remove("C:/ProgramData/testfile.txt")
                print("Removed")
            else:
                print("File not created yet")
            
            if os.path.exists(myRatingList):
                os.remove(myRatingList)
                print("Removed")
            else:
                print("File not created yet")
            
            if os.path.exists(everyWeekRatingLocation):
                os.remove(everyWeekRatingLocation)
                print("Removed")
            else:
                print("File not created yet")
            
            if os.path.exists(myRatingListRapid):
                os.remove(myRatingListRapid)
                print("Removed")
            else:
                print("File not created yet")
            
            if os.path.exists(everyWeekRatingLocationRapid):
                os.remove(everyWeekRatingLocationRapid)
                print("Removed")
            else:
                print("File not created yet")
        else:
            messagebox.showerror("Error", "Files not created yet")

    else:
        messagebox.showinfo("Cancel", "Reseting the files canceled")

def notPlayed():
    def blitzNotPlayed():
        localStorage = "C:/ProgramData"
        dayNumStorage = localStorage + "/Number Of Day Blitz.txt"
        myRatingList = location + "/Blitz Rating.txt"
        try:
            with open(dayNumStorage, "r") as dayNum:
                num = int(dayNum.read())
            with open(myRatingList, "a") as file:
                file.write(f"Day {num}: Not Played\n")
                file.write("Gained rating: 0\n\n")
            num += 1
            with open(dayNumStorage, "w") as newDay:
                newDay.write(str(num))
            messagebox.showinfo("Not Played", "Marked Blitz as not played today.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Files are not created yet")
        window.destroy()

    def rapidNotPlayed():
        localStorage = "C:/ProgramData"
        dayNumStorage = localStorage + "/Number Of Day Rapid.txt"
        myRatingList = location + "/Rapid Rating.txt"
        try:
            with open(dayNumStorage, "r") as dayNum:
                num = int(dayNum.read())
            with open(myRatingList, "a") as file:
                file.write(f"Day {num}: Not Played\n")
                file.write("Gained rating: 0\n\n")
            num += 1
            with open(dayNumStorage, "w") as newDay:
                newDay.write(str(num))
            messagebox.showinfo("Not Played", "Marked Rapid as not played today.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Files are not created yet")
        window.destroy()
    
    def cancel():
        window.destroy()

    if os.path.exists("C:/ProgramData/testfile.txt"):
        with open("C:/ProgramData/testfile.txt", "r") as RatingListsLocation:
            location = RatingListsLocation.read()

        window = tk.Toplevel(root)
        window.title("Choose Time Control")
        window.geometry("300x150")

        label = tk.Label(window, text="Which rating did you not play today?")
        label.pack(pady=10)

        blitzBtn = tk.Button(window, text="Blitz", width=20, command=blitzNotPlayed)
        blitzBtn.pack(pady=5)

        rapidBtn = tk.Button(window, text="Rapid", width=20, command=rapidNotPlayed)
        rapidBtn.pack(pady=5)
        
        rapidBtn = tk.Button(window, text="Cancel", width=20, command=cancel)
        rapidBtn.pack(pady=5)
    else:
        messagebox.showerror("Error", "Files not created yet")

def exit():
    root.destroy()

#------------------MAIN BUTTONS
buttonBlitz = tk.Button(root, text="Blitz", width=20, command=Blitz)
buttonBlitz.pack(pady=10)

buttonRapid = tk.Button(root, text="Rapid", width=20, command=Rapid)
buttonRapid.pack(pady=10)

buttonReset = tk.Button(root, text="Reset All Data", width=20, command=resetHistory)
buttonReset.pack(pady=10)

buttonNotPlayed = tk.Button(root, text="Not Played Today", width=20, command=notPlayed)
buttonNotPlayed.pack(pady=10)

buttonExit = tk.Button(root, text="Exit", width=20, command=exit)
buttonExit.pack(pady=10)

root.mainloop()