import tkinter as tk
from tkinter import messagebox

def send_manual_distress():
    messagebox.showinfo("Distress Activated", "Manual distress signal sent!")
    with open("manual_trigger.log", "a") as f:
        f.write("Manual distress triggered.\n")

window = tk.Tk()
window.title("Maritime Safety System")

label = tk.Label(window, text="System Status: NORMAL", font=("Arial", 14))
label.pack(pady=10)

btn = tk.Button(window, text="Trigger Manual Distress", command=send_manual_distress, bg="red", fg="white")
btn.pack(pady=20)

window.mainloop()
