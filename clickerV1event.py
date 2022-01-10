import tkinter
from tkinter import Event, Label, font
from tkinter.constants import E, N
from typing import Text

window = tkinter.Tk()
window.title("Clicket v1")
window.configure(bg="gray")
window.geometry("700x500")

number = 0
n = str(number)


def up_func(event):
    print(str(event))
    global number
    global n
    number = number + 1
    n = str(number)
    crusorOut_func(Event)

def down_func(event):
    print(str(event))
    global number
    global n
    number = number - 1
    n = str(number)
    crusorOut_func(Event)

    

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

def click_Up(event):
    global number
    print(str(event))
    if number > 0:
        number = number + 3
        n = str(number)
    elif number < 0:
        number = number - 3
        n = str(number)
    window.update()
    label.configure(text=n)

 
     

btn1 = tkinter.Button(window , text="Up" , font=("Arial" , 15) , width = 20, bg="white" , fg="black" , command= lambda :  up_func(Event)    )
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


btn2 = tkinter.Button(window , text="Down" , font=("Arial" , 15) , width = 20 , bg="white" , fg="black" , command= lambda : down_func(Event)    )
btn2.pack(
    pady=40,
    padx=40,
    expand=True
)

label.bind("<Enter>" , crusorIn_func )
label.bind("<Leave>" , crusorOut_func)
label.bind("<Double-Button>",  click_Up  )

window.bind("<Up>",up_func)
window.bind("<+>",up_func)

window.bind("<Down>",down_func)
window.bind("-",down_func)

window.bind("<space>",click_Up )
 


window.mainloop()