import tkinter as tk

class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.RIGHT,padx=10,pady=10)

        self.hi_there = tk.Button(frame, text='打招呼', fg='#f60', bg='#000', command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print('互联网的广大朋友大家好，我是无忧')

root = tk.Tk()
app = APP(root)

root.mainloop()
