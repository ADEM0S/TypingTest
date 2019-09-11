#coding: utf-8

from tkinter import *
from tkinter import font
import random
import time
# from itertools import *



# little program to increase the typing speed

def listToStr(lol):
    starf = ""
    a = 0
    for i in lol:
        if len(starf) == 0:
            starf += str(i)
        else:
            starf += f" ,{str(i)}"
            if a % 5 == 0:
                starf += "\n"

        a += 1
    return starf

# deletes word from dico if already done
def wordsTo():
    if dictionary != []:
        for i in dictionary:

            if i in wordsDone:
                dictionary.remove(i)
                if dictionary == []:
                    global stop
                    stop = time.time()

    return dictionary

# returns a new word
def wordChanger():

    wordsTo()

    if dictionary != []:
        n = random.choice(dictionary)
        return n
    
# tries the word
def tryWord(event):

    if dictionary != []:
        entered = entrytxt.get()
        toEnter = t.get()

        if toEnter=="press enter":
            if entered == "":
                global start
                start = time.time()
        else: 
            if entered == toEnter:
                good.append(toEnter)
                # print("g", good)
            else:
                bad.append(toEnter)
                # print("b", bad)

        entrytxt.set("")

        wordsDone.append(toEnter)

        # gen a new word from dico
        wd = wordChanger()
        t.set(wd)

        # print(entered)
        # print(wordsDone)
        # print(dictionary)

        """END !!!"""
    else:
        entrytxt.set("")
        t.set("FINISH")
        global delta
        delta = stop - start
        # print(delta)


# sets the entry field to nothing
def deleteWord(event):
    entrytxt.set("")


def resultShow():
    if dictionary == []:

        #hide result button
        resButton.pack_forget()

        # time
        resTxt = StringVar() 
        resTxt.set(f"{round(delta, 2)} sec.\nYou wrote good {len(good)} words but also {len(bad)} incorrect word(s):\n {listToStr(bad)} \nWich make you {round((delta*len(good)*len(bad))/50, 2)} points.")
        results = Label(resFrame, bg="#663366", fg="white", font=("Helvetica", 20), textvariable = resTxt, justify= CENTER)
        results.pack()

        #retry
        retry = Button(resFrame, bg= '#663366', fg='white', font=('Arial', 25, 'bold'), text= 'Retry ?', command= play)
        retry.pack()


def play():
    d = root.slaves()
    for l in d:
        l.destroy()

    #variables
    global dictionary
    dictionary = ["espadrille", "pâtes", "pays", "cheveux", "téléphone", "codage", "ordinateur", "coin",\
                "de", "arc-en-ciel", "haut", "eau", "Jhon", "est", "nice", "spaghettis", "bolognaise", \
                "rutabaga", "chinchilla", "rosé", "espelette", "couteau", "fourchette", "crépusculaire",\
                "nocturne", "dioxyde", "carbone", "sirop", "bouteille", "feu", "camp", "pringles", "cuisiner",\
                "brasser"]

    global wordsDone
    wordsDone= []
    global good
    good = []
    global bad
    bad = []
    global start
    start, stop = 0, 0



    # global frame
    Gframe= Frame(root, bg='#663366')
    Gframe.pack()

    # general frame
    frame = Frame(Gframe, bg='#663366')
    frame.pack()



    # LAB 1
    label1 = Label(Gframe, text='TYPING Increaser', bg='#663366', fg="#ff8c7a", font=("Helvetica", 30, 'italic'))
    f = font.Font(label1, label1.cget("font"))
    f.configure(underline=True)
    label1.configure(font=f)

    label1.pack(pady= (50, 45))

    # LAB 2
    label2= Label(Gframe, text="**Type the following words without any fault**", bg='#663366', fg="white", font=("Helvetica", 23, 'italic'))
    label2.pack(pady= (0, 45))


    # form frame/grid
    frameGrid1 = Frame(Gframe)
    frameGrid1.pack()


    # words to type's grid
    frameGrid2 = Frame(frameGrid1)
    frameGrid2.grid(row=0)

    #LAB 'word to type in'
    label3= Label(frameGrid2, bg='#663366', text="Word to type in:", fg="white", font=("Helvetica", 25), width= 15)
    label3.grid(row=0, column=1)

    # 'word' label
    global t
    t = StringVar()
    t.set("press enter")
    labelRTR = Label(frameGrid2, bg='#663366', textvariable=t, fg="#00D8FF", font=("Helvetica", 25), width= 12)
    labelRTR.grid(row=0, column=2)

    # Entry frame
    entryFrame = Frame(frameGrid1, bg= '#663366')
    entryFrame.grid(row=1)
    # Entry 1
    global entrytxt
    entrytxt = StringVar()
    entry1 = Entry(entryFrame, font=("Helvetica", 23), width= 30, justify=CENTER, textvariable= entrytxt)
    entry1.pack()
    #assigning functions
    entry1.bind("<Return>", tryWord)
    entry1.bind("<Control-BackSpace>", deleteWord)


    # 'RESULT' frame
    global resFrame
    resFrame = Frame(Gframe, bg= '#663366')
    resFrame.pack()

    # label "RESULT"
    resLabel = Label(resFrame, bg='#663366', fg="red", font=("Helvetica", 27, "bold"), text="RESULTS")
    resLabel.pack(pady= (60, 0))


    # result activator
    global resButton
    resButton = Button(resFrame, bg = "white", width=20, height=3, text = "Click to see your results !", command= resultShow, shadow = None)
    resButton.pack()
        

    # print loop
    root.mainloop()


# root
root = Tk()
root.geometry("1800x1080")
root.config(bg='#663366')
root.title("Typing Increaser")
root.iconbitmap("rocket.ico")

play()
