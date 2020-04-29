from tkinter import *


def end_accountB():
     activityfile = UN + "" +  PS
     activity = open(activityfile, "a")
     add = addentry.get()
     activity.write(add)
     activity.close()
     window3.destroy()
     run_program()
     window3.mainloop()
def signout2():
    window2.destroy()
    global window3
    global addentry
    window3 = Tk()
    window3.title("ADD")
    addwhat = Label(window3, text="Before you go, type what you want to add to your activity file:     ")
    addwhat.grid(row=0, column=0, sticky=W)
    addentry = Entry(window3, width=40, bg="light green")
    addentry.grid(row=1, column=0, sticky=W)
    end_accountA = Button(window3, width=11, text="SIGN OUT", command = end_accountB)
    end_accountA.grid(row=2, column=0, sticky=W)
    window2.mainloop()
    window3.mainloop()
def SI():
    global passtext
    global activity
    global exist
    global UN
    global PS
    UN = entry1.get()
    PS = entry2.get()
    try:
        exist = open(UN, "r")
        text.delete(0.0, END)
        doesexist = ("yes")
    except:
        text.delete(0.0, END)
        text.insert(END, "Your account doesn't exist. Try creating an account. Go to Create Account under the OPTIONS menu.")
        doesexist = ("no")
    if doesexist == ("yes"):
        try:
            passtext = open(PS, "r")
            text.delete(0.0, END)
            text.insert(END, "LOGGED IN")
            window.destroy()
            global window2
            window2 = Tk()
            window2.title("SIGN OUT")
            signout = Button(window2, width=55, text="SIGN OUT", command=signout2)
            signout.grid(row=0, column=0, sticky=N)
            passtext.close()
            exist.close()
            
        except:
            text.delete(0.0, END)
            text.insert(END, "Password incorrect")
            
        
        
            
    else:
        for iiugfityfgutuyfkjfyfjf in range (0, 23):
            print("ERROR")
    window.mainloop()
    window2.mainloop()
def checknewaccount():
    NUN = entry3.get()
    NPS = entry4.get()
    try:
        already = (NUN, "r")
        already.close()
        text2.delete(0.0, END)
        text2.insert(END, "Username already exists")
    except:
        text2.delete(0.0, END)
        text2.insert(END, "All Good!")
        new_file = open(NUN, "w")
        new_file.close()
        new_file = open(NPS, "w")
        new_file.close()
        newactivityfile = NUN + "" + NPS
        new_file = open(newactivityfile, "w")
        new_file.close()
        root.destroy()
        run_program()
        root.mainloop()
def createaccount():
    window.destroy()
    global root
    global entry3
    global entry4
    global text2
    root = Tk()
    root.title("CAsim")
    label3 = Label(root, text="Enter Username:     ")
    label3.grid(row=0, column=0, sticky=W)
    entry3 = Entry(root, width=32, bg="light green")
    entry3.grid(row=1, column=0, sticky=W)
    label4 = Label(root, text="Enter Password:     ")
    label4.grid(row=2, column=0, sticky=W)
    entry4 = Entry(root, width=32, bg="light green")
    entry4.grid(row=3, column=0, sticky=W)
    button2 = Button(root, width=8, text="CREATE", command=checknewaccount)
    button2.grid(row=6, column=0, sticky=W)
    text2  = Text(root, height=10, width=30, wrap=WORD, background="yellow")
    text2.grid(row=5, column=0, columnspan=2, sticky=W)
    window.mainloop()
    root.mainloop()
def run_program():
    global entry1
    global entry2
    global window
    global text
    window= Tk()
    window.title("SIsim")
    label1 = Label(window, text="Enter Username:     ")
    label1.grid(row=0, column=0, sticky=W)
    entry1 = Entry(window, width=32, bg="light green")
    entry1.grid(row=1, column=0, sticky=W)
    label2 = Label(window, text="Enter Password:     ")
    label2.grid(row=2, column=0, sticky=W)
    entry2 = Entry(window, width=32, bg="light green")
    entry2.grid(row=3, column=0, sticky=W)
    button = Button(window, width=5, text="LOGIN", command=SI)
    button.grid(row=6, column=0, sticky=W)
    text  = Text(window, height=10, width=30, wrap=WORD, background="yellow")
    text.grid(row=5, column=0, columnspan=2, sticky=W)
    menubar = Menu(window)
    firstmenu = Menu(menubar, tearoff=0)
    firstmenu.add_command(label="Create Account", command=createaccount)
    firstmenu.add_command(label="Quit", command=window.destroy)
    menubar.add_cascade(label="OPTIONS", menu=firstmenu)
    window.config(menu=menubar)
    window.mainloop()
run_program()
