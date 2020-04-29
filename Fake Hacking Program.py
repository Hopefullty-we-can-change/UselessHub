from tkinter import *
import time
import random
print("")

            
    






def hackthem():
    text.delete(0.0, END)
    text.insert(END, "Hacked")
    global email
    global inbox
    global searchhistory
    global files
    global applications
    global password
    email = entry.get()
    choice_1 = var1.get()
    if choice_1 == 1:
        inbox = ("yes")
    else:
        inbox = ("no")
    choice_2 = var2.get()
    if choice_2 == 1:
        searchhistory = ("yes")
    else:
        searchhistory = ("no")
    choice_3 = var3.get()
    if choice_3 == 1:
        files = ("yes")
    else:
        files = ("no")
    choice_4 = var4.get()
    if choice_4 == 1:
        applications = ("yes")
    else:
        applications = ("no")
    choice_5 = var5.get()
    if choice_5 == 1:
        password = ("yes")
    else:
        password = ("no")
    time.sleep(10)
    runresults()
        
        
        

    
      










def start():
    global text
    global var1
    global var2
    global var3
    global var4
    global var5
    global window
    window = Tk()
    window.title("Let's Hack!")
    label = Label(window, text="Enter Email address (of person you want to hack):    ")
    label.grid(row=0, column=0, sticky=W)
    global entry
    entry = Entry(window, width=41, bg="light green")
    entry.grid(row=1, column=0, sticky=W)
    entry.insert(END, "someone@somemail.com/co.uk/org")
    var1 = IntVar()
    global c1
    c1 = Checkbutton(window, text="Inbox", variable=var1)
    c1.grid(row=2, column=0, sticky=W)
    var2 = IntVar()
    global c2
    c2 = Checkbutton(window, text="Search History", variable=var2)
    c2.grid(row=3, column=0, sticky=W)
    var3 = IntVar()
    global c3
    c3 = Checkbutton(window, text="Files", variable=var3)
    c3.grid(row=4, column=0, sticky=W)
    var4 = IntVar()
    global c4
    c4 = Checkbutton(window, text="Applications", variable=var4)
    c4.grid(row=5, column=0, sticky=W)
    var5 = IntVar()
    global c5
    c5 = Checkbutton(window, text="Password", variable=var5)
    c5.grid(row=6, column=0, sticky=W)
    button = Button(window, width=7, text="HACK", command=hackthem)
    button.grid(row=7, column=0, sticky=W)
    text = Text(window, width=90, height=20, wrap=WORD, background="yellow")
    text.grid(row=8, column=0, columnspan=6, sticky=W)
    text.insert(END, "Do NOT exit (for any reason) after selecting HACK")
    
    
    













def runresults():
    inboxres = ("NA")
    text.delete(0.0, END)
    text.insert(END, "After hacking ")
    text.insert(END, email)
    text.insert(END, ":")
    if inbox == ("yes"):
        num = (random.randint(1,3))
        if num == 1:
            inboxres = ("Lots of emails from DonaldTrump@hotmail.com")
            text.insert(END, " ")
            text.insert(END, inboxres)
            text.insert(END, ".")
        elif num == 2:
            inboxres = (" Lots of emails from BuyMyNuke@bazinga.org")
            text.insert(END, inboxres)
            text.insert(END, ".")
        else:
            inboxres = ("Lots of emails from CountToTenTeachingVerification@stupidperson.com")
            text.insert(END, " ")
            text.insert(END, inboxres)
            text.insert(END, ".")
    else:
        print("")
    if searchhistory == ("yes"):
        num = (random.randint(1,3))
        if num == 1:
            SHres = (" Has searched for www.pen_island.com")
            text.insert(END, SHres)
            text.insert(END, ".")
        elif num == 2:
            SHres = (" Has searched for www.BuyNukes.com")
            text.insert(END, SHres)
            text.insert(END, ".")
        else:
            SHres = (" Has searched for www.Results-YouAreIdiot.com")
            text.insert(END, SHres)
            text.insert(END, ".")
    else:
        print("")
    if files == ("yes"):
        num = (random.randint(1,3))
        if num == 1:
            Fres = (" Has a suspicious folder named 'NotMyKidPics'")
            text.insert(END, Fres)
            text.insert(END, ".")
        elif num == 2:
            Fres = (" Has a document called 'MyJournal'.")
            text.insert(END, Fres)
        else:
            Fres = (" Has photos of crime scenes.")
            text.insert(END, Fres)
    else:
        print("")
    if applications == ("yes"):
        num = (random.randint(1,3))
        if num == 1:
            appres = (" Has an app called 'Fortnite'.")
            text.insert(END, appres)
        if num == 2:
            appres = (" Has an app called 'Minecraft'.")
            text.insert(END, appres)
        else:
            appres = (" Has an app called 'Plauge Inc.'.")
            text.insert(END, appres)
    else:
        print("")
    if password == ("yes"):
        num = (random.randint(1,3))
        if num == 1:
            passw = (" The email password is 'abcdyhvYGoops'.")
            text.insert(END, passw)
        elif num == 2:
            passw = (" The email password is 'ILovePeterRabbitMrMeForty'.")
            text.insert(END, passw)
        else:
            passw = (" The email password is 'WeBeGoingToNZBoisss!!!!'.")
            text.insert(END, passw)
        text.insert(END, " Please consider buying premium - it will decrease your 10 seacond wait time.")
        
        
        

































    










start()
