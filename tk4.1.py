from tkinter import *

root = Tk()


GIELS = ['西施', '貂蝉', '王昭君', '杨玉环']

v = []

for girl in GIELS:
    v.append(IntVar())
    b = Checkbutton(root, text=girl, variable=v[-1])
    b.pack(anchor='w')

mainloop()
