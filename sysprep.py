# Imports
from tkinter import *
import os
from tkinter.font import BOLD
import PIL
from PIL import Image,ImageTk

#MAIN GUI window
root = Tk()

#MAIN GUI window title
root.title('PWNC0D_sysprep')

#MAIN GUI icon
root.iconbitmap('img/PWNC0D.ico')

icon    =   "img/PWNCOD.ico"
zero    =   'run\\program0'
one     =   'run\\program1'
two     =   'run\\program2'
three   =   'run\\program3'
four    =   'run\\program4'
five    =   'run\\program5'
six     =   'run\\program6'
uac     =   ImageTk.PhotoImage(Image.open("img/please_click_yes.png"))
main    =   ImageTk.PhotoImage(Image.open("img/main.png"))
zero1   =   ImageTk.PhotoImage(Image.open("img/zero_1.png"))
zero2   =   ImageTk.PhotoImage(Image.open("img/zero_2.png"))
one1    =   ImageTk.PhotoImage(Image.open("img/one_1.png"))
one2    =   ImageTk.PhotoImage(Image.open("img/one_2.png"))
one3    =   ImageTk.PhotoImage(Image.open("img/one_3.png"))
one4    =   ImageTk.PhotoImage(Image.open("img/one_4.png"))
two1    =   ImageTk.PhotoImage(Image.open("img/two_1.png"))
two2    =   ImageTk.PhotoImage(Image.open("img/two_2.png"))
two3    =   ImageTk.PhotoImage(Image.open("img/two_3.png"))
two4    =   ImageTk.PhotoImage(Image.open("img/two_4.png"))
three1  =   ImageTk.PhotoImage(Image.open("img/three_1.png"))
four1   =   ImageTk.PhotoImage(Image.open("img/four_1.png"))
four2   =   ImageTk.PhotoImage(Image.open("img/four_2.png"))
four3   =   ImageTk.PhotoImage(Image.open("img/four_3.png"))
six1    =   ImageTk.PhotoImage(Image.open("img/six_1.png"))
six2    =   ImageTk.PhotoImage(Image.open("img/six_2.png"))
txt1    =   "Click 'Disable Windows Defender' outlined in the picture.\nThen click the BLUE 'NEXT'>>>"
txt2    =   "Close Windows Defender Controll as oulined in the picture.\nThen click the BLUE 'NEXT>>>"
txt3    =   "Click the blue button outlined in the picture above. Then click the BLUE  'NEXT'>>>"
txt4    =   "Welcome to sysprep v0.1 \nPlease click INSTALL to get started!"
txt5    =   "Please click 'YES' on the next popup"
txt6    =   "We are all done here\nHAPPY HACKING"
button1 =   "INSTALL"
button2 =   "NEXT"
button3 =   "DONE"

#UAC POPUP INSTRUCTIOS
def uac_pic(task):
    picture_label.config(image=uac)
    txt_label.config(text=txt5)
    button_install.config(text=button2, command=lambda: prog_num(task))

#INSTRUCTIOS
def prog_num(arg):
    global img, text, command, button
    if arg == "zero1":
        install(zero)
        button = button2
        img = zero1
        text = txt1
        command = lambda: prog_num("zero2")
    if arg == "zero2":
        button = button2
        img = zero2
        text = txt2
        command = lambda: uac_pic("one1")
    if arg == "one1":
        install(one)
        button = button2
        img = one1
        text = txt3
        command = lambda: prog_num("one2")
    if arg == "one2":
        button = button2
        img = one2
        text = txt3
        command = lambda: prog_num("one3")
    if arg == "one3":
        button = button2
        img = one3
        text = txt3
        command = lambda: prog_num("one4")
    if arg == "one4":
        button = button2
        img = one4
        text = txt3
        command = lambda: uac_pic("two1")
    if arg == "two1":
        install(two)
        button = button2
        img = two1
        text = txt3
        command = lambda: prog_num("two2")
    if arg == "two2":
        button = button2
        img = two2
        text = txt3
        command = lambda: prog_num("two3")
    if arg == "two3":
        button = button2
        img = two3
        text = txt3
        command = lambda: prog_num("two4")
    if arg == "two4":
        button = button2
        img = two4
        text = txt3
        command = lambda: uac_pic("three1")
    if arg == "three1":
        install(three)
        button = button2
        img = three1
        text = txt3
        command = lambda: uac_pic("four1")
    if arg == "four1":
        install(four)
        button = button2
        img = four1
        text = txt3
        command = lambda: prog_num("four2")
    if arg == "four2":
        button = button2
        img = four2
        text = txt3
        command = lambda: prog_num("four3")
    if arg == "four3":
        button = button2
        img = four3
        text = txt3
        command = lambda: uac_pic("six1")
    if arg == "six1":
        install(six)
        button = button2
        img = six1
        text = txt3
        command = lambda: prog_num("six2")
    if arg == "six2":
        button = button3
        img = six2
        text = txt6
        command = root.quit
    picture_label.config(image=img)
    txt_label.config(text=text)
    button_install.config(text=button, command=command)

#INSTALL
def install(prog):
    os.startfile(prog)

#window frame
window_frame = Frame(root)
window_frame.grid()

#MAIN GUI picture
picture = main
picture_label = Label(root, image=picture)
picture_label.grid(row=0, column=0, columnspan=3)

#MAIN GUI txt
txt_label = Label(root, text=txt4, font=("Helvetica", 18, BOLD))
txt_label.grid(row=1, column=1)

### MAIN GUI buttons ###
### INSTALL ###
button_install_border = Frame(root, highlightbackground = "blue", highlightthickness = 2.5, bd=0)
button_install = Button(button_install_border, text=button1, fg = 'black', bg = 'white',
font = (("Helvetica"),15, BOLD), command=lambda: uac_pic("zero1"))
button_install.grid(row=1, column=2)
button_install_border.grid(row=1, column=2)

### QUIT ###
button_quit_border = Frame(root, highlightbackground = "red", highlightthickness = 2.5, bd=0)
button_quit = Button(button_quit_border, text="QUIT",  fg = 'black', bg = 'white',
font = (("Helvetica"),15, BOLD), command=root.quit)
button_quit.grid(row=1, column=0)
button_quit_border.grid(row=1,column=0)

# call sysprep
root.mainloop()