import string
from tkinter import *
import random
import pyperclip

# setting the window
window = Tk()
window.geometry('400x250')
window.resizable(0, 0)
window.title("GDJ Password Generator")

# Heading
heading = Label(window,text= 'Password Generator',font='arial 15 bold').pack()

# select password length
password_label = Label(window,text='Password Length',font= 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(window, from_=8, to=25,textvariable=pass_len, width= 15).pack()     # spinbox is used to have a box with arrows to change the value

# function to generate pwd

pass_str = StringVar()
def generator():
    password = ""
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

    pass_str.set(password)


Button(window,text='generate password',font= 'arial 10 bold',bg='cyan', command=generator).pack(pady=5)
Entry(window,textvariable= pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(window, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)



window.mainloop()


