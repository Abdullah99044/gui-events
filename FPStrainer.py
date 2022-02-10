from asyncio import events
from calendar import c
from distutils import command
from multiprocessing.dummy import Event
from re import X
import tkinter as tk
import random
from tkinter.constants import CENTER, E, LEFT, N, NE, NW, RIGHT, S, SE, SW, TOP, W
from tkinter.messagebox import askyesno



window = tk.Tk()
window.title("FPS trainer v1")
window.geometry("700x500")
window.configure(bg="gray")

#functions

constant_time = 20
time = constant_time
points = 0


def time_function():
    global time , points
    for i in range(20):
        time = time - 1
        window.update()
        window.after(1000)
        bar.configure(text="Time remanning {}".format(str(time)) )  
    if time == 0:
        answer = askyesno(title='Confirm',
                message='Congratulations you have {} points , wanna play again?'.format(points))
        if answer == False:
            time = 20
            window.update()
            btn.pack_configure(
                expand=True
            )
            btn.configure(
                text="Press here",
                command=lambda : [ key_func(Event) , time_function() ]
            )
            points = 0
            bar1.configure(text=" 0 points")

        else:
            time = constant_time
            time_function()



def key_func(event):
    event
    global points
    window.update()
    keyboard = ["w" , "a" , "s" , "d" , "<Button-1>" , "<Double-Button-1>"]
    key = random.choice(keyboard)
    print(key)
    if key == "a": 
        bind_key("a" ,  "s" , "d" , "w" , "<Button-1>" , "<Double-Button-1>" ) 
    elif key == "w":
        bind_key("w" ,  "a" , "d" , "s" , "<Button-1>" , "<Double-Button-1>" ) 
    elif key == "s":
        bind_key("s" , "a" , "d" , "w" , "<Button-1>" , "<Double-Button-1>" ) 
    elif key == "d": 
        bind_key("d" ,  "a" , "s" , "w" , "<Button-1>" , "<Double-Button-1>" )
    elif key == "<Button-1>":
        bind_click("<Button-1>" , "d" ,  "a" , "s" , "w" , "<Double-Button-1>")
    elif key == "<Double-Button-1>":
        bind_click("<Double-Button-1>", "d" ,  "a" , "s" , "w" , "<Button-1>" )

    x = random.randint(40,400)
    y = random.randint(40,450)
    btn.place_configure(x=x , y=y  ) 
    btn.configure(font=("Arial" , 15) , text=key )
    
def points_func(event):
    event
    global points
    window.update()
    points+=2
    bar1.configure(text=" {} points".format(points))

def points_func1(event):
    global points
    window.update()
    points+=1
    bar1.configure(text=" {} points".format(points))
    
def bind_key(key , a ,s , d , e , f):
    window.unbind(str(a)) 
    window.unbind(str(s)) 
    window.unbind(str(d)) 
    window.unbind(str(e)) 
    window.unbind(str(f)) 
    bind_id = window.bind(str(key) , points_func1 ) 
    bind_id = window.bind(str(key) ,key_func, add="+") 

def bind_click(key , a ,s , d , e , f):
    window.unbind(str(a)) 
    window.unbind(str(s)) 
    window.unbind(str(d)) 
    window.unbind(str(e)) 
    window.unbind(str(f)) 
    bind_id = btn.bind(str(key) , points_func ) 
    bind_id = btn.bind(str(key) ,key_func, add="+") 
    


#labels

bar2 = tk.Label(
    bg="black"
)

bar2.pack(
    side= TOP,
    anchor=N
)

bar2.place(
    relwidth=4.1 ,
    height=30
)

bar = tk.Label(   #Time label
 
    bg="black" ,
    fg="White" , 
    text="Time remanning {}".format(str(time)),
    font=("Arial" , 15)
)

bar.pack( 
    side= LEFT ,
    anchor=N
)

     
bar1 = tk.Label(  #points label
    bg="black" ,
    fg="White" , 
    text=" {} points".format(points),
    font=("Arial" , 15)
)

bar1.pack(
    side = RIGHT, 
    anchor= N  ,
    padx=50
)

#button

btn = tk.Button(
    window , 
    bg="white",
    fg="black",
    text="Press here",
    font=("Arial" , 15),
    command=lambda : [ key_func(Event) , time_function() ]
)


btn.pack(
    ipadx=10,
    ipady=10,
    expand=True,
)




bind_id = window.bind("a",key_func )
bind_id = window.unbind("a")

window.mainloop()