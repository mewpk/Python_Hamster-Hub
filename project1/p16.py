import tkinter as tk

root = tk.Tk()

tk.Button(root,text='0', bg = "yellow").grid(row=0, column=0, sticky='NSEW')
tk.Button(root,text='1', bg = "yellow").grid(row=0, column=1, sticky='NSEW')
tk.Button(root,text='2', bg = "yellow").grid(row=0, column=2, sticky='NSEW')
tk.Button(root,text='3', bg = "yellow").grid(row=0, column=3, sticky='NSEW')
tk.Button(root,text='4', bg = "yellow").grid(row=0, column=4, sticky='NSEW')
tk.Button(root,text='5', bg = "yellow").grid(row=1, column=0, sticky='NSEW')
tk.Button(root,text='6', bg = "yellow").grid(row=1, column=1, sticky='NSEW')
tk.Button(root,text='7', bg = "yellow").grid(row=1, column=2, sticky='NSEW')
tk.Button(root,text='8', bg = "yellow").grid(row=1, column=3, sticky='NSEW')
tk.Button(root,text='9', bg = "yellow").grid(row=1, column=4, sticky='NSEW')
tk.Button(root,text='+', bg = "yellow").grid(row=2, column=0, sticky='NSEW')
tk.Button(root,text='-', bg = "yellow").grid(row=2, column=1, sticky='NSEW')
tk.Button(root,text='*', bg = "yellow").grid(row=2, column=2, sticky='NSEW')
tk.Button(root,text='/', bg = "yellow").grid(row=2, column=3, sticky='NSEW')
tk.Button(root,text='Enter', bg = "yellow").grid(row=2, column=4, sticky='NSEW')

root.mainloop()
