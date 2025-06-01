import time
import subprocess
import tkinter as tk
from tkinter import messagebox

while True:
    root = tk.Tk()
    root.withdraw()
    result = subprocess.run(['WMIC', 'Path', 'Win32_Battery', 'Get', 'EstimatedChargeRemaining'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    percent_line = next((line for line in lines if line.strip().isdigit()), None)
    if int(percent_line) <= 30:
        messagebox.showwarning("Battery warning", "Your battery is under 30")
        break
    time.sleep(30)