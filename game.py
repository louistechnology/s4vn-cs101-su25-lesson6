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

data = {
    "player": [20, 40],
    "items": [
        [100, 100],
        [120, 100],
        [150, 100],
        [200, 250],
        [300, 350],
        [250, 400],
        [250, 50]
    ]
}

px, py = data["player"]
player = canvas.create_rectangle(
    px, py,
    px+20, py+20,
    fill='red', outline='red')

items = []
for x,y in data["items"]:
    item = canvas.create_oval(x, y, x+5, y+5, fill='white')
    items.append(item)

root.mainloop()
