import tkinter as tk
import random


H = 500 # กำหนดค่าตัวแปรความสูงหน้าต่างโปรแกรม
W = 800 # ตัวแปรความกว้าง

root = tk.Tk()

canvas = tk.Canvas(root, height=H, width=W)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='ตกลง', font=40, command=lambda: get_data(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg= '#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left')
label.place(relwidth=1, relheight=1)

y = random.randrange(1,10)
z = 0
op =[]


def get_data(x):
    global y
    global z
    if int(x) == y:
        op.append("!!!!!!!!!YOU WINNNN!!!!!!!!!!!")
        label['text'] = op
            
    elif int(x) > y:
        if z==2:
            op.append("GAME OVER"+" random = "+str(y))
            label['text'] =op
        else :
            op.append("too big\n")
            label['text'] =op
    elif int(x) < y:
        if z==2:
            op.append("GAME OVER"+" random = "+str(y))
            label['text'] = op
        else :
            op.append("too small\n")
            label['text'] =op
    if z==2:
        op.append("GAME OVER"+" random = "+str(y))
        label['text'] = op
    z += 1

root.mainloop()
