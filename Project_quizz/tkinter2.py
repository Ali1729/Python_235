from tkinter import *
import random
import csv


#This section of code also sets up the GUI
window=Tk()
window.configure(bg="#6e17bf")
window.resizable(False, False)
window.geometry("1001x601")
window.title("Flashcard-App")
window2=Tk()
window2.configure(bg="#6e17bf")
window2.resizable(False, False)
window2.geometry("1001x601")
window2.title("Flashcard-App")


the_canvas = Canvas(window,width=1000,height=600, highlightthickness=0)
the_canvas.place(x=0,y=0)
the_canvas.create_rectangle(0,0,1000,600,fill="#1A17BF",outline="")
the_canvas.create_rectangle(10,10,990,590,fill="#BF17BC",outline="")
the_canvas.create_rectangle(20,20,980,580,fill="#1A17BF",outline="")
the_canvas.create_rectangle(30,30,970,570,fill="#6e17bf",outline="")
the_canvas.create_rectangle(40,40,80,560,fill="#BF17BC",outline="")
the_canvas.create_rectangle(100,40,140,560,fill="#BF17BC",outline="")
the_canvas.create_rectangle(160,40,200,560,fill="#BF17BC",outline="")
the_canvas.create_rectangle(920,40,960,560,fill="#BF17BC",outline="")
the_canvas.create_rectangle(860,40,900,560,fill="#BF17BC",outline="")
the_canvas.create_rectangle(800,40,840,560,fill="#BF17BC",outline="")


the_canvas2 = Canvas(window2,width=1000,height=600, highlightthickness=0)
the_canvas2.place(x=0,y=0)
the_canvas2.create_rectangle(0,0,1000,600,fill="#1A17BF",outline="")
the_canvas2.create_rectangle(10,10,990,590,fill="#BF17BC",outline="")
the_canvas2.create_rectangle(20,20,980,580,fill="#1A17BF",outline="")
the_canvas2.create_rectangle(30,30,970,570,fill="#6e17bf",outline="")
the_canvas2.create_rectangle(40,40,80,560,fill="#BF17BC",outline="")
the_canvas2.create_rectangle(100,40,140,560,fill="#BF17BC",outline="")
the_canvas2.create_rectangle(160,40,200,560,fill="#BF17BC",outline="")
the_canvas2.create_rectangle(920,40,960,560,fill="#BF17BC",outline="")
the_canvas2.create_rectangle(860,40,900,560,fill="#BF17BC",outline="")
the_canvas2.create_rectangle(800,40,840,560,fill="#BF17BC",outline="")
start_label=Label(the_canvas2,text="FLASHCARDS",font=("fixedsys",155),bg="#6e17bf",fg="white",pady=90)
start_label.place(x=245,y=100)
start_button=Button(text="START STUDYING",font=("fixedsys",30),command=None,bg="#2a19e3",fg="white",anchor=CENTER,padx=99)
start_button.place(x=246,y=450)
window.mainloop()
window2.mainloop()