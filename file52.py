from tkinter import *
def add():
    a = int(txtA.get())
    b = int(txtB.get())
    lblResult = Label(root,text=a+b)
    lblResult.place(relx=0.1,rely=0.5)

def form():
    global root,txtA,txtB,btnSubmit
    root = Tk()
    root.geometry("600x600")
    root.option_add("*Font", "aerial 12 bold")
    txtA = Entry(root)
    txtA.place(relx=0.1,rely=0.2)
    txtB = Entry(root)
    txtB.place(relx=0.1,rely=0.3)
    btnSubmit=Button(root,text="Add",command=add)
    btnSubmit.place(relx=0.1,rely=0.4)
    root.mainloop()


form()
    