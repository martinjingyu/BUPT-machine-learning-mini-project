import os
import tkinter as tk
from PIL import Image, ImageTk
import sys  # 导入sys模块
sys.setrecursionlimit(3000)  # 将默认的递归深度修改为3000

IMAGE_DIR = "./genki4k/files"
LABEL_DIR = ".\\genki4k\\newlabel"
LABEL_FILE = os.path.join(LABEL_DIR, "labels.txt")

if not os.path.exists(LABEL_DIR):
    os.makedirs(LABEL_DIR)

window = tk.Tk()
window.title("Image Labeling")

canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

button0 = tk.Button(window, text="男", width=10, command=lambda: save_label(0))
button0.pack(side=tk.LEFT, padx=10, pady=10)
button1 = tk.Button(window, text="女", width=10, command=lambda: save_label(1))
button1.pack(side=tk.LEFT, padx=10, pady=10)
# button2 = tk.Button(window, text="2", width=10, command=lambda: save_label(2))
# button2.pack(side=tk.LEFT, padx=10, pady=10)

images = os.listdir(IMAGE_DIR)

labels = {}
if os.path.exists(LABEL_FILE):
    with open(LABEL_FILE, "r") as f:
        for line in f:
            image_name, label = line.strip().split()
            labels[image_name] = label

index = 0

def show_next_image():
    global index
    if index >= len(images):
        window.destroy()
        return
    image_name = images[index]
    if image_name in labels:
        index += 1
        show_next_image()
        return
    image_data = Image.open(os.path.join(IMAGE_DIR, image_name))
    image_data = image_data.resize((600, 400))
    image_data = ImageTk.PhotoImage(image_data)
    canvas.create_image(0, 0, anchor=tk.NW, image=image_data)
    window.title(f"Image Labeling - {image_name}")
    canvas.image = image_data

def save_label(label):
    global index
    image_name = images[index]
    with open(LABEL_FILE, "a") as f:
        f.write(f"{image_name} {label}\n")
    index += 1
    show_next_image()

show_next_image()
window.mainloop()
