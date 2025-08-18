import tkinter as tk
from tkinter import messagebox
from datetime import date, datetime
# App
root = tk.Tk()
root.tk.call('tk', 'scaling', 2.0)
root.geometry("400x400+620+50")
root.title("Rating Counter")

# Creating files
try:
      with open("current rating.txt", "x") as f:
            print("Created")
except FileExistsError:
      print("Already exists")
try:
      with open("goal rating.txt", "x") as f:
            print("Created")
except FileExistsError:
      print("Already exists")
try:
      with open("day.txt", "x") as f:
            print("Created")
except FileExistsError:
      print("Already exists")
try:
      with open("month.txt", "x") as f:
            print("Created")
except FileExistsError:
      print("Already exists")
try:
      with open("stable current rating.txt", "x") as f:
            print("Created")
except FileExistsError:
      print("Already exists")

# Functions
def chooseDate():
      dateRoot = tk.Toplevel(root)
      dateRoot.protocol("WM_DELETE_WINDOW", root.destroy)
      root.withdraw()
      dateRoot.tk.call('tk', 'scaling', 2.0)
      dateRoot.geometry("400x400+620+50")
      dateRoot.title("Choose date")

      textDay = tk.Label(dateRoot, width=20, text="Enter day", font=("Arial", 12))
      choseDay = tk.Entry(dateRoot, width=3, font=("Arial", 12))

      textMonth = tk.Label(dateRoot, width=20, text="Enter month", font=("Arial", 12))
      choseMonth = tk.Entry(dateRoot, width=3, font=("Arial", 12))

      textCurrentRating = tk.Label(dateRoot, width=20, text="Enter your rating", font=("Arial", 12))
      choseCurrentRating = tk.Entry(dateRoot, width=5, font=("Arial", 12))

      textGoalRating = tk.Label(dateRoot, width=20, text="Enter your goal rating", font=("Arial", 12))
      choseGoalRating = tk.Entry(dateRoot, width=5, font=("Arial", 12))

      textDay.grid(row=0, column=0, padx=10, pady=10, sticky="w")
      choseDay.grid(row=0, column=1, padx=10, pady=10)

      textMonth.grid(row=1, column=0, padx=10, pady=10, sticky="w")
      choseMonth.grid(row=1, column=1, padx=10, pady=10)

      textCurrentRating.grid(row=2, column=0, padx=10, pady=20, sticky="w")
      choseCurrentRating.grid(row=2, column=1, padx=10, pady=20)

      textGoalRating.grid(row=3, column=0, padx=10, pady=10, sticky="w")
      choseGoalRating.grid(row=3, column=1, padx=10, pady=10)

      def get_date():
            day = choseDay.get()
            month = choseMonth.get()
            currentRating = choseCurrentRating.get()
            goalRating = choseGoalRating.get()
            try:
                  if int(day) > 31 or int(day) == 0 or int(day) < 0:
                        messagebox.showerror("ERROR", "Day should be 1-31")
                  elif int(month) > 12 or int(month) == 0 or int(month) < 0:
                        messagebox.showerror("ERROR", "Month should be 1-12")
                  elif int(currentRating) == 0 or int(currentRating) < 0:
                        messagebox.showerror("ERROR", "Rating should be more than 0")
                  elif int(goalRating) == 0 or int(goalRating) < 0:
                        messagebox.showerror("ERROR", "Goal rating should be more than 0")
                  else:
                        with open("day.txt", "w") as dayFile:
                              dayFile.write(day)
                        with open("month.txt", "w") as monthFile:
                              monthFile.write(month)
                        with open("current rating.txt", "w") as currentRatingFile:
                              currentRatingFile.write(currentRating)
                        with open("goal rating.txt", "w") as goalRatingFile:
                              goalRatingFile.write(goalRating)
                        with open("stable current rating.txt", "w") as stableCurrentRatingFile:
                              stableCurrentRatingFile.write(currentRating)
                        btnDate.pack_forget()
                        text.pack_forget()
                        dateRoot.destroy()
                        root.destroy()
            except ValueError:
                  messagebox.showerror("ERROR", "Only digit allowed")

      getDateBtn = tk.Button(dateRoot, text="NEXT", width=10, command=get_date, font=("Arial", 12))
      getDateBtn.grid(row=5, column=0, columnspan=2, pady=20)

# Convert datas to variables
with open("day.txt", "r") as dayRead:
      day = dayRead.read()
with open("month.txt", "r") as monthRead:
      month = monthRead.read()
with open("current rating.txt", "r") as currentRatingFile:
      currentRating = currentRatingFile.read()
with open("goal rating.txt", "r") as goalRatingFile:
      goalRating = goalRatingFile.read()
with open("stable current rating.txt", "r") as stableCurrentRatingFile:
      stableRating = stableCurrentRatingFile.read()


if not day or not month or not currentRating or not goalRating:
      text = tk.Label(root, text="No game plan yet? Start one", width=30, font=("Arial", 12))
      text.pack(pady=10)
      btnDate = tk.Button(root, text="Start a new plan", width=25, command=chooseDate, font=("Arial", 12), bg="lightblue")
      btnDate.pack(pady=20)
else:
      def calculatePercentage(goalRating, stableRating, currentRating):
            finalGoalRating = int(goalRating) - int(stableRating)
            finalCurrentRating = int(currentRating) - int(stableRating)
            percent = round((finalCurrentRating * 100) / finalGoalRating, 2)
            if percent > 100:
                  percent = 100
            elif percent < 0:
                  percent = 0
            return percent
      
      def updateGreenBar(percentage):
            canvas.delete("green_bar")
            fill_width = (percentage / 100) * 300
            canvas.create_rectangle(0, 0, fill_width, 30, fill="green", tags="green_bar")

      percentage = calculatePercentage(goalRating, stableRating, currentRating)
      canvas = tk.Canvas(root, width=300, height=30)
      canvas.grid(row=3, column=0, columnspan=2, pady=10, padx=50, sticky="w")
      canvas.create_rectangle(0,0,300,30, fill="lightgrey")
      updateGreenBar(percentage)

      def calculateNewRating():
            realNewRating = newRatingInput.get()
            try:
                  if not realNewRating:
                        messagebox.showerror("ERROR", "Input cannot be empty")
                        return
                  with open("current rating.txt", "w") as newRatingFile:
                        newRatingFile.write(realNewRating)
                  with open("goal rating.txt", "r") as goalRatingFile:
                        goalRating = goalRatingFile.read()
                  with open("stable current rating.txt", "r") as stableCurrentRatingFile:
                        stableRating = stableCurrentRatingFile.read()
                  percentage = calculatePercentage(goalRating, stableRating, realNewRating)
                  updateGreenBar(percentage)
                  percentageText = tk.Label(root, text=f"{percentage}%",width=10, font=("Arial", 12))
                  percentageText.grid(row=4, column=0,columnspan=2, padx=10, pady=10)
            except ValueError:
                  messagebox.showerror("ERROR", "Only digit allowed")


      def restart(ask):
            if ask:
                  askYesNo = messagebox.askyesno("Yes or No", "Do you want to restart your plan?")
                  if askYesNo:
                        with open("current rating.txt", "w") as currentTxtFile:
                              currentTxtFile.write("")
                        with open("goal rating.txt", "w") as goalTxtFile:
                              goalTxtFile.write("")
                        with open("stable current rating.txt", "w") as StablecurrentTxtFile:
                              StablecurrentTxtFile.write("")
                        with open("month.txt", "w") as monthTxtFile:
                              monthTxtFile.write("")
                        with open("day.txt", "w") as dayTxtFile:
                              dayTxtFile.write("")
                        root.destroy()
            else:
                  with open("current rating.txt", "w") as currentTxtFile:
                        currentTxtFile.write("")
                  with open("goal rating.txt", "w") as goalTxtFile:
                        goalTxtFile.write("")
                  with open("stable current rating.txt", "w") as StablecurrentTxtFile:
                        StablecurrentTxtFile.write("")
                  with open("month.txt", "w") as monthTxtFile:
                        monthTxtFile.write("")
                  with open("day.txt", "w") as dayTxtFile:
                        dayTxtFile.write("")
                  root.destroy()

      newRatingInput = tk.Entry(root, width=5, font=("Arial", 12))
      text1 = tk.Label(root, text="Finished playing today?", font=("Arial", 12))
      text2 = tk.Label(root, text="Enter your new rating:", font=("Arial", 12))
      calculateBtn = tk.Button(root, text="Calculate", width=10, command=calculateNewRating, font=("Arial", 12), bg="green")
      restartBtn = tk.Button(root, text="Restart", width=7, command=lambda: restart(True), font=("Arial", 10), bg="green")
      percentageText = tk.Label(root, text=f"{percentage}%", font=("Arial", 12))
      
      text1.grid(row=0, column=0, pady=10, padx=10, sticky="w")
      text2.grid(row=1, column=0, pady=10, padx=10, sticky="w")
      newRatingInput.grid(row=1, column=1, padx=10, pady=10)
      calculateBtn.grid(row=2, column=0, pady=10, padx=10, sticky="w")
      restartBtn.grid(row=2, column=1, pady=10, padx=10, sticky="w")
      percentageText.grid(row=4, column=0,columnspan=2, padx=10, pady=10)

      #date
      with open("day.txt", "r") as dayFile:
            day = int(dayFile.read())
      with open("month.txt", "r") as monthFile:
            month = int(monthFile.read())

      now = datetime.now()
      today = date(2025, now.month, now.day)
      targetDate = date(2025, month, day)

      leftDays = (targetDate - today).days

      if leftDays <= 0:
            # Delete widgets
            text1.grid_forget()
            text2.grid_forget()
            newRatingInput.grid_forget()
            canvas.grid_forget()
            calculateBtn.grid_forget()
            percentageText.grid_forget()

            timeUpText = tk.Label(root, text="Your time is up", font=("Arial", 12))
            percentageInfoText = tk.Label(root, text=f"You reached {percentage}% to your goal", font=("Arial", 12))
            nextBtn = tk.Button(root, text="Next", width=15,command=lambda: restart(False), font=("Arial", 12), bg="green")

            timeUpText.grid(row=0, column=0, padx=30, pady=10)
            percentageInfoText.grid(row=1, column=0, padx=30, pady=10)
            nextBtn.grid(row=3, column=0, padx=30, pady=10)
      else:
            leftDaysText = tk.Label(root, text=f"Left time: {leftDays} days", font=("Arial", 12))
            leftDaysText.grid(row=5, column=0, padx=10, pady=10, sticky="w")

root.mainloop()