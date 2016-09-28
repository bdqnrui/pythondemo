from tkinter import *

root = Tk()

v = IntVar()

Radiobutton(root, text='One', variable=v, value=8).pack(anchor='w')
Radiobutton(root, text='T22wo', variable=v, value=2).pack(anchor='w')
Radiobutton(root, text='Three', variable=v, value=6).pack(anchor='w')

mainloop()
