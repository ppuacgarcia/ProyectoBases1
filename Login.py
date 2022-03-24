import tkinter as tk
from turtle import bgcolor, width
from tkinter import *
from PIL import Image, ImageTk
from MenuPrincipal import *

pw = Tk()
pw.geometry('1200x675')
pw.configure(bg='#707070')
pw.resizable(0,0)
pw.title('Base de Datos')
pw.iconbitmap('Images/Teen.ico')

fonttxt = 'Arial'
posx=430
posy=100
colorbg="#ABB2B9"

flog = Frame(pw,width=1200,height=675,bg='#707070')
flog.place(x=0, y=0)


def Correcto():
    if(Username.get()=="admin" and Password.get()=="1234"):
        MenP(pw)
        flog.destroy()
        print("entro")
    else:
        
        print("no entro")
        
        

#Labels
#imagenes
global logoH
lgimg=Image.open('Images/Teen.ico')
lgimg.resize((100,100),Image.ANTIALIAS)
logoH = ImageTk.PhotoImage(lgimg)
bglabel=Label(flog,image=logoH, border=0,bg=colorbg).place(x=posx, y = posy)
#labels
#user label
UserLabel=Label(flog,text='Usuario')
UserLabel.place(x=posx,y=posy+260)
UserLabel.config(bg=colorbg,font=(fonttxt,15,'bold'))
#password label
PasswordLabel=Label(flog,text='Clave')      
PasswordLabel.place(x=posx,y=posy+315)
PasswordLabel.config(bg=colorbg,font=(fonttxt,15,'bold'))
#login label
LoginLablel=Label(flog, text='Inicio')
LoginLablel.place(x=posx+80,y=0)
LoginLablel.config(bg=colorbg,font=(fonttxt,40,'bold'))

#username enrty
Username=StringVar()
Username_entry = Entry(flog,textvariable=Username)
Username_entry.config(width=30,font=(fonttxt,12))
Username_entry.place(x=posx,y=posy+290)
#password entry
Password=StringVar()
EntryPassword=Entry(flog,textvariable=Username)
EntryPassword.config(width=30,font=(fonttxt,12),textvariable=Password,show='■')
EntryPassword.place(x=posx,y=posy+340)
#button
Enter=Button(flog, text="Entrar",font=(fonttxt,13,'bold'),width=10,command=Correcto)
Enter.place(x=posx,y=posy+370)
pw.mainloop()


        
