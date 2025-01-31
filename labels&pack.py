import tkinter as tk

root = tk.Tk()
root.title("Labels & Pack GUI")

#Important Label Options
# text - adds the text
# bd - background
# fg -  foreground
# font - sets the font
# padx - x padding
# pady - y padding
# relief - border styling (SUNKEN, RAISED, GROOVE, RIDGE)

#Important Label pack options
# side - top, bottom, left, right
# anchor = n, s, e, w, ne, se and so...ff

title_label = tk.Label(text = "My Name is Pranav Gupta, I am pursuing my BTECH from ABES Engineering College. I am cool as fuck, and my college is shit as fuck!", bg="darkblue", fg="white", padx=23, pady= 54, font="comicsansms 19 bold italic", borderwidth=3, relief="groove")
title_label.pack(side="top", anchor="se")

root.mainloop()