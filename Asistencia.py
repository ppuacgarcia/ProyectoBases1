from optparse import Values
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from Menu import *
from tkinter import ttk
from tkcalendar import *
import mariadb

def AsisForm(pw, idEvent):
    
    w = Frame(pw,width=1200,height=675,bg='#707070')
    w.place(x=0, y=0)
    fuenteG = font=('Comic Sans MS', 19,'bold')
    fuenteP = font=('Comic Sans MS', 15,'bold')
    bglabel = '#707070'
    fglabel = '#FFFFFF'
    posx = 80

    def confirmarAsistencia():
        None
        
    def cmd():
        w.destroy()
        
    def buscarAdolescente():
        None
    
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open('Images/HM.png')) 
    Button(w, command = cmd, image=img1, border=0,activebackground='#000000', bg='#707070').place(x=5, y = 10)

    #Labels formulario
    def lab(text, font, bg, fg, x, y):
        labe = Label(w,text=text, font=font, bg=bg, foreground=fg)
        labe.pack()
        labe.place(x=x, y=y)


    lab('Asistencia', fuenteG, bglabel, fglabel, 500, 10)


    
    #Funcion para crear botones
    def btn(f1, x, y, text, bcolor, fcolor, command, font, siz, tipe,wdt,ht):
        #Botones para menu
        def on_enter(e):
            buttons['background'] = bcolor
            buttons['foreground'] = fcolor
            
        def on_leave(e):
            buttons['background'] = fcolor
            buttons['foreground'] = bcolor
            
            
        buttons = Button(w, width=wdt, height=ht, text= text, fg  = bcolor, bg=fcolor, command=command, border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
        buttons.bind("<Enter>", on_enter)
        buttons.bind("<Leave>", on_leave)
        buttons.place(x=x, y=y)
    
    btn(w, 975, 600, 'confirmar asistencia', '#000000', '#FF4e10', confirmarAsistencia,'Arial', 12,'bold',18,2)
    btn(w, 60, 115, 'buscar', '#000000', '#FF4e10', buscarAdolescente,'Arial', 12,'bold',10,1)
    
    def Ent(textvar, width, x, y):
        Entr = Entry(w,textvariable=textvar, width=width)
        Entr.pack()
        Entr.place(x=x, y=y)
     
    busqueda = StringVar()  

    Ent(busqueda, 64, 175, 115)
    
    #Tabla Adolescentes
    tabladata = ttk.Treeview(w)
    tabladata=ttk.Treeview(w,columns=("col1","col2","col3"), height=19)
    tabladata.column("#0", width=80)
    tabladata.column("col1",width=240, anchor=CENTER)
    tabladata.column("col2",width=100, anchor=CENTER)
    tabladata.column("col3",width=80, anchor=CENTER)
    tabladata.heading("#0",text="Id",anchor=CENTER)
    tabladata.heading("col1",text="Nombre",anchor=CENTER)
    tabladata.heading("col2",text="Genero",anchor=CENTER)
    tabladata.heading("col3",text="Edad",anchor=CENTER)
    tabladata.place(x=60,y=150)
    
    
    #Tabla Asistencia
    tabla = ttk.Treeview(w)
    tabla=ttk.Treeview(w,columns=("col1","col2","col3"), height=21)
    tabla.column("#0", width=80)
    tabla.column("col1",width=240, anchor=CENTER)
    tabla.column("col2",width=100, anchor=CENTER)
    tabla.column("col3",width=80, anchor=CENTER)
    tabla.heading("#0",text="Id",anchor=CENTER)
    tabla.heading("col1",text="Nombre",anchor=CENTER)
    tabla.heading("col2",text="Genero",anchor=CENTER)
    tabla.heading("col3",text="Edad",anchor=CENTER)
    tabla.place(x=620,y=110)
    