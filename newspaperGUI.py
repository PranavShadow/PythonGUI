import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Newspaper")

image_paths = [
    r"D:\Semester - III\Python\Python GUI\Images\1.jpg",
    r"D:\Semester - III\Python\Python GUI\Images\2.png",
    r"D:\Semester - III\Python\Python GUI\Images\3.png"
]

text_paths = [
    r"D:\Semester - III\Python\Python GUI\Texts\1.txt.txt",
    r"D:\Semester - III\Python\Python GUI\Texts\2.txt.txt",
    r"D:\Semester - III\Python\Python GUI\Texts\3.txt.txt"
]

photos = []
image_labels = []
text_labels = []

for path in image_paths:
    img = Image.open(path)
    resized_image = img.resize((300, 300)) 
    photos.append(ImageTk.PhotoImage(resized_image))

for path in text_paths:
    with open(path, "r") as file:
        content = file.read()
        text_labels.append(content)

for i in range(len(photos)):
    frame = tk.Frame(root)
    frame.pack(side="top", fill="x", pady=10)  

    image_label = tk.Label(frame, image=photos[i])
    image_label.pack(side="left", padx=10)  

    text_label = tk.Label(frame, text=text_labels[i], justify="left", width=40, padx=10, pady=10, anchor="w", background="black", foreground="white")
    text_label.pack(side="left", padx=10)  

root.mainloop()
