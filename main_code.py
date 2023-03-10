from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget('text')
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else :
            try:
                value = eval(screen.get())
            except Exception as e :
                print(e)
                value = "Error"   
        
        scvalue.set(value)
        screen.update()
    
    elif text == "c":
        scvalue.set("")
        screen.update()
    
    else :
        scvalue.set(scvalue.get()+text)
        screen.update()
        

root = Tk()

root.config(bg="black")
root.geometry('400x800')
root.title("calculator (shubham)")
p1 = PhotoImage(file = "calculator.png") #add icon
root.iconphoto(False,p1)

scvalue = StringVar()
scvalue.set('')
screen = Entry(root , textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill=X , ipadx=6,pady=8,padx=8)

f = Frame(root , bg="gray")
b = Button(f,text="9",padx=14,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="8",padx=15,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="7",padx=15,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root , bg="gray")
b = Button(f,text="6",padx=15,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="5",padx=15,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="4",padx=14,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root , bg="gray")
b = Button(f,text="3",padx=15,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="2",padx=15,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="1",padx=14,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root , bg="gray")
b = Button(f,text="0",padx=16,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="+",padx=15,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="-",padx=17,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root , bg="gray")
b = Button(f,text="*",padx=15,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="/",padx=15,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="%",padx=17,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root , bg="gray")
b = Button(f,text=".",padx=16,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="c",padx=16,pady=4,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="=",padx=17,pady=5,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

f.pack()
root.mainloop()