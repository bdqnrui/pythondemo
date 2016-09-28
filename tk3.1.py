from tkinter import *

root = Tk()

photo = PhotoImage(file='bg.gif')
theLabel = Label(root,
                 text='学python\n到Fishc',
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=('迷你简硬笔楷书',20),
                 fg='#fff')
theLabel.pack()

mainloop()
