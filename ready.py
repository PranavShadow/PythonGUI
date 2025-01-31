import tkinter as tk

root = tk.Tk()
root.title("Ready Window")


ready_label = tk.Label(text="Ready", background="green", foreground="white", font="ariel 19 bold", padx=50, pady=20)
ready_label.pack(side="bottom")

root.mainloop()