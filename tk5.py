from tkinter import *

root = Tk()

Label(root, text='帐号：').grid(row=0, column=0)
Label(root, text='密码：').grid(row=1, column=0)

v1 = StringVar()
v2 = StringVar()

e1 = Entry(root, textvariable=v1)
e2 = Entry(root, textvariable=v2, show='*')
e1.grid(row=0, column=1, padx=10, pady=10)
e2.grid(row=1, column=1, padx=10, pady=10)

def show():
    print('帐号：《%s》' % e1.get())
    print('密码：%s' % e2.get())

Button(root, text='获取信息', width=10, command=show)\
             .grid(row=3, column=0, sticky='w', padx=10, pady=5)
Button(root, text='退出', width=10, command=root.quit)\
             .grid(row=3, column=1, sticky='e', padx=10, pady=5)

mainloop()
