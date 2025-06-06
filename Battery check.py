import time
import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog

percentage = simpledialog.askinteger("Percentage", "When do you want to get warning?")
while True:
    root = tk.Tk()
    root.withdraw()
    result = subprocess.run(['WMIC', 'Path', 'Win32_Battery', 'Get', 'EstimatedChargeRemaining'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    percent_line = next((line for line in lines if line.strip().isdigit()), None)
    if percentage is not None:
        if int(percent_line) <= int(percentage):
            messagebox.showwarning("Battery warning", f"Your battery is under {percentage}")
            break
        time.sleep(30)