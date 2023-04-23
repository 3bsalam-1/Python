from tkinter import *
from time import strftime
root = Tk()
root.geometry("500x500")
root.resizable(True,True)
root.title('Clock')
root.config(bg="#121212")
root.iconbitmap("D:\Python\Clock\clock.ico")
def time():
    string = strftime('%I:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)
mark = Label(root, 
            font = ('calibri', 40, 'bold'),
            pady=150,
            foreground = '#b0b0b0',
            bg='#121212')
mark.pack(anchor = 'center')
time()
 
mainloop()