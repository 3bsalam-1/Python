from datetime import datetime
from tkinter import ttk

import customtkinter
from tkcalendar import DateEntry

# initialize the gui window and add some styles on it.
root = customtkinter.CTk()
style = ttk.Style(root)
root.geometry("600x200")
root.resizable(True, True)
root.title('Age Calculator')
root.iconbitmap('D:\\Python\\Age_calculator\\Age.ico')
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")


# define a function to calculate the age using the birthdate
def age():
    now = str(datetime.now())
    split = datetime.strptime(now, '%Y-%m-%d  %H:%M:%S.%f')  # get the current date
    date = datetime.strptime(cal.get(), '%d/%m/%Y')  # get the birthdate from user by date entry
    month = 0
    day = split.day
    year = 0
    if int(date.month) > int(split.month):
        month = (int(date.month) - int(split.month)) - 12
        year = (int(split.year) - int(date.year)) - 1

    elif int(date.month) <= int(split.month):
        month = int(split.month) - int(date.month)
        year = (int(split.year) - int(date.year))
        if day > int(date.day):
            day = int(split.day) - int(date.day)

    # print the full age in label
    l1.after(1000, age)  # make a label dynamic
    l1.configure(
        text=f"Your age now is: {year} years, {month} months, {day} days, {split.hour} hours, {split.minute} minutes, {split.second} seconds.")


# initialize and configure the date entry and label

style.theme_use('alt')
style.configure("age.DateEntry", foreground="#aaaaaa", fieldbackground='#242424', background="#242424",
                arrowcolor='#aaaaaa', borderwidth=0, bordercolor="#242424")
cal = DateEntry(root, selectmode='day', font='calibri 11 bold',
                cursor="hand2", style="age.DateEntry", locale='en_US', date_pattern='dd/mm/yyyy',
                borderwidth=0, disabledbackground="#242424", bordercolor="#242424",
                headersbackground="#242424", normalbackground="#242424", foreground='#aaaaaa',
                normalforeground='#aaaaaa', headersforeground='#aaaaaa', weekendbackground="#242424",
                othermonthbackground="#242424", othermonthwebackground="#242424")
cal.grid(row=1, column=1, padx=250, pady=25)
b1 = customtkinter.CTkButton(root, text="Age", command=lambda: age())
b1.grid(row=2, column=1)
l1 = customtkinter.CTkLabel(root, font=('calibri', 12, 'bold'), text=" ", fg_color="transparent")
l1.grid(row=3, column=1, pady=20)

root.mainloop()
