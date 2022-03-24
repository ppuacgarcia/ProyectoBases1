from tkinter import *
from PIL import Image, ImageTk

def ColForm(pw):
    

    w = Frame(pw, bg='#707070')
    w.geometry('1200x675')
    w.place(x=0, y=0)
    fuenteG = font=('Comic Sans MS', 19,'bold')
    fuenteP = font=('Comic Sans MS', 15,'bold')
    bglabel = '#707070'
    fglabel = '#FFFFFF'
    posx = 80

    def Sav():
        None

    #Labels formulario
    def lab(text, font, bg, fg, x, y):
        labe = Label(text=text, font=font, bg=bg, foreground=fg)
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

    def Ent(textvar, width, x, y):
        Entr = Entry(textvariable=textvar, width=width)
        Entr.pack()
        Entr.place(x=x, y=y)
        

    Ent(name, 155, 175, 105)
    Ent(fechanac, 135, 295, 140)
    Ent(Sexo, 155, 175, 175)
    Ent(Rango, 155, 175, 210)
    Ent(Contacto, 155, 175, 300)
    Ent(Telefono, 155, 175, 335)
    Ent(TipoSangre, 144, 240, 370)
    Ent(Alergias, 155, 175, 405)


    def btn(f1, x, y, text, bcolor, fcolor, command, font, siz, tipe):
        #Botones para menu
        def on_enter(e):
            buttons['background'] = bcolor
            buttons['foreground'] = fcolor
            
        def on_leave(e):
            buttons['background'] = fcolor
            buttons['foreground'] = bcolor
            
            
        buttons = Button(w, width=18, height=2, text= text, fg  = bcolor, bg=fcolor, command=command, border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
        buttons.bind("<Enter>", on_enter)
        buttons.bind("<Leave>", on_leave)
        buttons.place(x=x, y=y)

    btn(w, 980, 600, 'guardar', '#000000', '#FF4e10', Sav,'Arial', 12,'bold',)