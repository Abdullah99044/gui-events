import tkinter
from tkinter import Event, Label, font
from tkinter.constants import E, N
from typing import Text

window = tkinter.Tk()
window.title("Clicket v1")
window.configure(bg="gray")
window.geometry("700x500")

number = 0


def up_func():
    global number
    number = number + 1

def lable_func():
    global number
    n = str(number)
    if number > 0:
        window.update()
        label.configure(text=n)
        window.configure(bg="green")
    elif number == 0:
        window.update()
        label.configure(text=n)
        window.configure(bg="gray")
    elif number < 0:
        window.update()
        label.configure(text=n)
        window.configure(bg="Red")

def down_func():
    global number
    number = number - 1

def crusorIn_func(event):
    print(str(event))
    window.update()
    window.configure(bg="yellow")   

def crusorOut_func(event):
    global number
    print(str(event))
    n = str(number)
    if number > 0:
        window.update()
        label.configure(text=n)
        window.configure(bg="green")
    elif number == 0:
        window.update()
        label.configure(text=n)
        window.configure(bg="gray")
    elif number < 0:
        window.update()
        label.configure(text=n)
        window.configure(bg="Red")



     

btn1 = tkinter.Button(window , text="Up" , font=("Arial" , 15) , width = 20, bg="white" , fg="black" , command=lambda : [up_func() , lable_func()] )
btn1.pack(
    pady=50,
    padx=40,
    expand=True
)

label = tkinter.Label( window , text="0" , font=("Arial" , 15) , bg="white" , width = 20 , fg="black" )
label.pack(
    pady=40,
    padx=40,
    expand=True
)

label.bind("<Enter>" , crusorIn_func )
label.bind("<Leave>" , crusorOut_func)

btn2 = tkinter.Button(window , text="Down" , font=("Arial" , 15) , width = 20 , bg="white" , fg="black" , command=lambda : [down_func() , lable_func()]  )
btn2.pack(
    pady=40,
    padx=40,
    expand=True
)


window.mainloop()