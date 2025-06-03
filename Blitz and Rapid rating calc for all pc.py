import time
import tkinter as tk
import os
from tkinter import simpledialog, messagebox, filedialog

root = tk.Tk()
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
            ratingListRead.write(str(curRating))

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
            print("Typing the rating canceled!")
            time.sleep(2)

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
    root.destroy()

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
            ratingListRead.write(str(curRating))

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
            print("Typing the rating canceled!")
            time.sleep(2)

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
    root.destroy()

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
        messagebox.showinfo("Cancel", "Reseting the files canceled")
    root.destroy()

buttonBlitz = tk.Button(root, text="Blitz", command=Blitz)
buttonBlitz.pack(pady=10)

buttonRapid = tk.Button(root, text="Rapid", command=Rapid)
buttonRapid.pack(pady=10)

buttonReset = tk.Button(root, text="Reset All Data", command=resetHistory)
buttonReset.pack(pady=10)

root.mainloop()