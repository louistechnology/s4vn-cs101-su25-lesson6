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
    ],
    "score": 0
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

def update_score():
    # thay đổi số điểm
    data["score"] = data["score"] + 1
    score_label.configure(text="Số bước: "+str(data["score"]))

def up_handler(event):
    canvas.move(player, 0, -10)
    update_score()

def down_handler(event):
    canvas.move(player, 0, 10)
    update_score()

def left_handler(event):
    canvas.move(player, -10, 0)
    update_score()

def right_handler(event):
    canvas.move(player, 10, 0)
    update_score()

root.bind("<Up>", up_handler)
root.bind("<Down>", down_handler)
root.bind("<Left>", left_handler)
root.bind("<Right>", right_handler)

root.bind("w", up_handler)
root.bind("s", down_handler)
root.bind("a", left_handler)
root.bind("d", right_handler)

root.mainloop()
