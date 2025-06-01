import tkinter as tk
from tkinter import simpledialog, messagebox
import keyboard

password = "09192531793"
def checkPassword():
    if keyboard.is_pressed('ctrl+q'):
        root.quit()
    else:
        root.attributes("-fullscreen", True)
        root.attributes("-topmost", True)
        root.update()

        askpassword = simpledialog.askstring("Password", "Çıxmaq üçün kodu daxil edin", parent=root)

        if askpassword == password:
            messagebox.showinfo("Doğru", "Kod doğrudur. Çıxış edildi", parent=root)
            root.destroy()
        else:
            messagebox.showerror("Yanlış", "Kod yanlışdır. Çıxa bilməzsiniz", parent=root)
            root.after(1000, checkPassword)

def block_close():
    pass  # Disable close (X)

def block_alt_f4(event):
    return "break"  # Block Alt+F4

root = tk.Tk()
root.title("Fullscreen Black")
root.configure(bg="black")
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.protocol("WM_DELETE_WINDOW", block_close)
root.bind_all("<Alt-F4>", block_alt_f4)

root.after(100, checkPassword)

# Start mainloop
root.mainloop()
