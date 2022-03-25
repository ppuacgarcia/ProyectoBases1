from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from Menu import *
from tkinter import ttk
from tkcalendar import *

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
        

    Ent(name, 155, 175, 105)
    cal=DateEntry(w,width=30)
    cal.place(x=295,y=140)
    Ent(Contacto, 155, 175, 300)
    Ent(Telefono, 25, 175, 335)
    Ent(TipoSangre, 144, 240, 370)
    Ent(Alergias, 25, 175, 405)

    valrang = ['Ministro','Lider','Teacher']
    comboRan = ttk.Combobox(w, value=valrang, width=152)
    comboRan.place(x=175, y=210)
    comboRan["state"]="readonly"
    comboRan.current(2)
    
    valS = ['Masculino', 'Femenino']
    comboS = ttk.Combobox(w, value=valS, width=152)
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
    btn(w,posx+375,335,'guardar telefono','#000000','#FF4e10',Sav,'Arial',12,'bold',13,1)
    btn(w,posx+375,405,'guardar alergia','#000000','#FF4e10',Sav,'Arial',12,'bold',13,1)
    
    def tb(w,x,y):
        tabla=Listbox(w)
        tabla.place(x=x,y=y)
        tabla.config(height=2)
    tb(w,707,335)
    tb(w,707,405)
    

    
     
    
  

