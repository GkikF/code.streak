import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Code.Streak")
root.configure(bg="white")
root.geometry("600x400")  # optional size

# -------- SCREEN 1 --------
scr1 = tk.Frame(root, bg="white")
scr1.pack(fill="both", expand=True)

label1 = tk.Label(scr1, text="Welcome to Code.Streak. You can learn Python in a fun and exciting way!", bg="white")
label1.pack(pady=20)

label2 = tk.Label(scr1, text="Python", bg="white")
label2.pack(pady=10)

# Button to go to Screen 2
def go_to_scr2():
    scr1.pack_forget()          # hide Screen 1
    scr2.pack(fill="both", expand=True)  # show Screen 2

button = tk.Button(scr1, text="Print and Values", command=go_to_scr2)
button.pack(pady=20)

# -------- SCREEN 2 --------
scr2 = tk.Frame(root, bg="white")

label_scr2 = tk.Label(scr2, text="Print and Values", bg="white")
label_scr2.pack(pady=20)

# Button to go back to Screen 1
def go_to_scr1():
    scr2.pack_forget()
    scr1.pack(fill="both", expand=True)

back_button = tk.Button(scr2, text="Back to main menu", command=go_to_scr1)
back_button.pack(pady=20)

# Start the app
root.mainloop()
