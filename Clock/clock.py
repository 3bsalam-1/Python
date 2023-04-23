from tkinter import __all__
from time import strftime
import customtkinter
root = customtkinter.CTk()
root.geometry("400x80")
root.resizable(True,True)
root.title('Clock')
root.iconbitmap("D:\\Python\\Clock\\clock.ico")
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")
def time():
    string = strftime('%I:%M:%S %p')
    mark.configure(text = string)
    mark.after(1000, time)
mark = customtkinter.CTkLabel(root, font = ('calibri', 40, 'bold'),pady=35,text=" ",fg_color="transparent")
mark.grid(row=3,column=1)
mark.pack(anchor = 'center')
time()
 
root.mainloop()