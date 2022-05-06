from optparse import Values
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from Menu import *
from tkinter import ttk
from tkcalendar import *
import mariadb

def ColForm(pw):
    
    #
    w = Frame(pw,width=1200,height=675,bg='#707070')
    w.place(x=0, y=0)
    fuenteG = font=('Comic Sans MS', 19,'bold')
    fuenteP = font=('Comic Sans MS', 15,'bold')
    bglabel = '#707070'
    fglabel = '#FFFFFF'
    posx = 80

    def Sav():
        None
        
    def cmd():
        w.destroy()
        
    global img1
    img1 = ImageTk.PhotoImage(Image.open('Images/HM.png')) 
    Button(w, command = cmd, image=img1, border=0,activebackground='#000000', bg='#707070').place(x=5, y = 10)

    #Labels formulario
    def lab(text, font, bg, fg, x, y):
        labe = Label(w,text=text, font=font, bg=bg, foreground=fg)
        labe.pack()
        labe.place(x=x, y=y)


    lab('Registro Colaboradores', fuenteG, bglabel, fglabel, 490, 10)
    lab('Datos Generales', fuenteG, bglabel, fglabel, posx, 55)
    lab('Nombre', fuenteP, bglabel, fglabel, posx, 95)
    lab('Fecha de Nacimiento', fuenteP, bglabel, fglabel, posx, 130)
    lab('Sexo', fuenteP, bglabel, fglabel, posx, 165)
    lab('Rango', fuenteP, bglabel, fglabel, posx, 200)
    lab('Informacion de Enmergencia', fuenteG, bglabel, fglabel, posx, 240)
    lab('Contacto', fuenteP, bglabel, fglabel, posx, 290)
    lab('Telefono', fuenteP, bglabel, fglabel, posx, 325)
    lab('Tipo de Sangre', fuenteP, bglabel, fglabel, posx, 360)
    lab('Alergias', fuenteP, bglabel, fglabel, posx, 395)


    name = StringVar()
    fechanac = StringVar()
    Sexo = StringVar()
    Rango = StringVar()
    Contacto = StringVar()
    Telefono = int()
    TipoSangre = StringVar()
    Alergias = StringVar()

    #Cuadros de Texto
    def Ent(textvar, width, x, y):
        Entr = Entry(w,textvariable=textvar, width=width)
        Entr.pack()
        Entr.place(x=x, y=y)
        

    Ent(name, 65, 175, 105)
    cal=DateEntry(w,width=30)
    cal.place(x=295,y=140)
    Ent(Contacto, 65, 175, 300)
    Ent(Telefono, 20, 175, 335)
    Ent(TipoSangre, 54, 240, 370)
    Ent(Alergias, 20, 175, 405)

    valrang = ['Ministro','Lider','Teacher']
    comboRan = ttk.Combobox(w, value=valrang, width=62)
    comboRan.place(x=175, y=210)
    comboRan["state"]="readonly"
    comboRan.current(2)
    
    valS = ['Masculino', 'Femenino']
    comboS = ttk.Combobox(w, value=valS, width=62)
    comboS.place(x=175, y=175)
    comboS["state"]="readonly"
    comboS.current(0)
    
    
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
    
    btn(w, 980, 600, 'guardar', '#000000', '#FF4e10', Sav,'Arial', 12,'bold',18,2)
    btn(w,posx+230,331,'guardar telefono','#000000','#FF4e10',Sav,'Arial',12,'bold',13,1)
    btn(w,posx+230,401,'guardar alergia','#000000','#FF4e10',Sav,'Arial',12,'bold',13,1)
    
    def tb(w,x,y):
        tabla=Listbox(w)
        tabla.place(x=x,y=y)
        tabla.config(height=1)
    tb(w,450,335)
    tb(w,450,405)
    
    #Tabla
    tabladata = ttk.Treeview(w)
    tabladata=ttk.Treeview(w,columns=("col1","col2","col3"))
    tabladata.column("#0", width=80)
    tabladata.column("col1",width=240, anchor=CENTER)
    tabladata.column("col2",width=100, anchor=CENTER)
    tabladata.column("col3",width=80, anchor=CENTER)
    tabladata.heading("#0",text="Id",anchor=CENTER)
    tabladata.heading("col1",text="Nombre",anchor=CENTER)
    tabladata.heading("col2",text="Genero",anchor=CENTER)
    tabladata.heading("col3",text="Edad",anchor=CENTER)
    tabladata.place(x=620,y=100)