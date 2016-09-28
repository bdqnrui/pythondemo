from tkinter import *

master = Tk()

theLB = Listbox(master)
theLB.pack()

for item in ['鸡蛋', '鸭蛋', '厄蛋', '李狗蛋']:
    theLB.insert(END, item)

def dele():
    theLB.delete(ACTIVE)
    
theButton = Button(master, text='删除它', command=dele)
theButton.pack()
mainloop()
