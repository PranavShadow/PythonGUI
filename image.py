import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image GUI")
root.geometry("1920x500")

# Define image paths
image_paths = [
    r"D:\Semester - III\Python\Python GUI\Images\1.jpg",
    r"D:\Semester - III\Python\Python GUI\Images\2.png",
    r"D:\Semester - III\Python\Python GUI\Images\3.png",
    r"D:\Semester - III\Python\Python GUI\Images\4.jpg",
    r"D:\Semester - III\Python\Python GUI\Images\5.jpg",
    r"D:\Semester - III\Python\Python GUI\Images\6.jpg",
    r"D:\Semester - III\Python\Python GUI\Images\7.jpg",
    r"D:\Semester - III\Python\Python GUI\Images\8.jpg"
]

# Create a list to store resized images and labels
photos = []
labels = []

# Resize images and store them in the list
for path in image_paths:
    img = Image.open(path)
    img_resized = img.resize((200, 200))  # Resize to 200x200
    photos.append(ImageTk.PhotoImage(img_resized))

# Create labels with resized images
for photo in photos:
    labels.append(tk.Label(image=photo))

# Pack the labels
for label in labels:
    label.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
