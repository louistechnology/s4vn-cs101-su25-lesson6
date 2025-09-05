from tkinter import *

WIDTH = 500   # Chiều ngang (W: Width)
HEIGHT = 500  # Chiều dọc   (H: Height)

root = Tk()
root.title("CS101")

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

score_label = Label(root, text="Số bước: 0")
canvas.create_window(50, 15, window=score_label)

canvas.create_line(0, 30, WIDTH, 30)

root.mainloop()
