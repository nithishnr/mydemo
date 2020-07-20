from tkinter import *

root = Tk()
root.title("Percentage Calculator")
root.configure(background="#f4511e", padx=20, pady=30)
root.geometry("400x250")

def click():
    ans = (int(i.get()) / 100) * int(e.get())
    flt = int(ans)
    global myClick
    myClick = Label(root, text=flt, font="inter 20 normal",bg="#f4511e")
    myClick.place(x=250,y=150)


def des():
    myClick.destroy()


title=Label(root,text="Percentage Calculator",font="benzo 20 bold", bg="#f4511e")
title.place(x=30,y=0)
enterNumber = Label(root, text="Enter a number", bg="#f4511e",  font="benzo 15 normal",pady=20,fg="#FFFFFF")
enterNumber.place(x=5,y=40)
e = Entry(root, width=15,borderwidth=0)

e.place(x=220,y=65)

enterPercent = Label(root, text="Enter a percentage", bg="#f4511e", font="benzo 15 normal",pady=10,fg="#FFFFFF")
enterPercent.place(x=5,y=95)
i = Entry(root, width=15,borderwidth=0)

i.place(x=220,y=110)

myButton = Button(root, text="Okay!", command=click,fg="#d32f2f",bg="#FFFFFF",borderwidth=0)
myButton.place(x=7,y=150)
rem = Button(root, text="Clear",command=des,  fg="#d32f2f",bg="#FFFFFF",borderwidth=0)
rem.place(x=100,y=150)


root.mainloop()
