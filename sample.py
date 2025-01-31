import tkinter as tk

root = tk.Tk()
root.title("Basic Tkinter Application")

#Minimum & Maximum Geometry
root.geometry("800x800")
root.minsize(400,400)
root.maxsize(1200,1200)

label = tk.Label(text="Sample Label for GUI")
label.pack()



root.mainloop()