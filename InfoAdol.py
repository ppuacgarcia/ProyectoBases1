from optparse import Values
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from Menu import *
from tkinter import ttk
from tkcalendar import *
import mariadb

def adolinfo(pw):
    
    w = Frame(pw,width=1200,height=675,bg='#707070')
    w.place(x=0, y=0)
    fuenteG = font=('Comic Sans MS', 19,'bold')
    fuenteP = font=('Comic Sans MS', 15,'bold')
    bglabel = '#707070'
    fglabel = '#FFFFFF'
    posx = 80
    posx2 = 790

    def Sav():
        None
        
    def cmd():
        w.destroy()
        
    def borrarRegistro():
        None
    
    def editarRegistro():
        None   
        
    def NomSearch():
        None 
        
    def FechaSearch():
        None
        
    def GenSearch():
        None
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open('Images/HM.png')) 
    Button(w, command = cmd, image=img1, border=0,activebackground='#000000', bg='#707070').place(x=5, y = 10)

    #Labels formulario
    def lab(text, font, bg, fg, x, y):
        labe = Label(w,text=text, font=font, bg=bg, foreground=fg)
        labe.pack()
        labe.place(x=x, y=y)


    lab('Informacion Adolescentes', fuenteG, bglabel, fglabel, 490, 10)
    lab('Busquedas:', fuenteG, bglabel, fglabel, posx, 55)
    lab('Nombre:', fuenteP, bglabel, fglabel, posx2, 170)
    lab('Genero:', fuenteP, bglabel, fglabel, posx2, 230)
    lab('Edad:', fuenteP, bglabel, fglabel, posx2, 290)
    lab('Tipo Sangre:', fuenteP, bglabel, fglabel, posx2, 348)
    lab('Contacto Enmergencia:', fuenteP, bglabel, fglabel, posx2, 408)

    busc = StringVar()
    Nombre = StringVar()
    Genero = StringVar()
    Edad = StringVar()
    TSangre = StringVar()
    CEnmerg = StringVar()
    #Cuadros de Texto
    def Ent(textvar, width, x, y):
        Entr = Entry(w,textvariable=textvar, width=width)
        Entr.pack()
        Entr.place(x=x, y=y)
        

    Ent(busc, 55, 220, 72)
    Ent(Nombre, 57, 800, 200)
    Ent(Genero, 57, 800, 260)
    Ent(Edad, 57, 800, 320)
    Ent(TSangre, 57, 800, 380)
    Ent(CEnmerg, 57, 800, 440)

    
    valS = ['Masculino', 'Femenino']
    comboS = ttk.Combobox(w, value=valS, width=25)
    comboS.place(x=805, y=72)
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
    
    btn(w, 570, 72, 'Nombre', '#000000', '#FF4e10', NomSearch,'Arial', 12,'bold',10,1)
    btn(w, 680, 72, 'Fecha', '#000000', '#FF4e10', FechaSearch,'Arial', 12,'bold',10,1)
    btn(w, 1010, 72, 'Genero', '#000000', '#FF4e10', GenSearch,'Arial', 12,'bold',10,1)
    
    
    #Tabla
    tabladata = ttk.Treeview(w)
    tabladata=ttk.Treeview(w,columns=("col1","col2","col3", "col4", "col5"), height=18)
    tabladata.column("#0", width=80)
    tabladata.column("col1",width=200, anchor=CENTER)
    tabladata.column("col2",width=100, anchor=CENTER)
    tabladata.column("col3",width=80, anchor=CENTER)
    tabladata.column("col4",width=80, anchor=CENTER)
    tabladata.column("col5",width=120, anchor=CENTER)
    tabladata.heading("#0",text="Id",anchor=CENTER)
    tabladata.heading("col1",text="Nombre",anchor=CENTER)
    tabladata.heading("col2",text="Genero",anchor=CENTER)
    tabladata.heading("col3",text="Edad",anchor=CENTER)
    tabladata.heading("col4",text="Tipo Sangre",anchor=CENTER)
    tabladata.heading("col5",text="Contacto Enmerg",anchor=CENTER)
    tabladata.place(x=80,y=120)
    
    #TablaTElefonos
    tablatel = ttk.Treeview(w)
    tablatel=ttk.Treeview(w,columns=("col1"), height=3)
    tablatel.column("#0", width=80)
    tablatel.column("col1",width=200, anchor=CENTER)
    tablatel.heading("#0",text="Id",anchor=CENTER)
    tablatel.heading("col1",text="Telefono",anchor=CENTER)
    tablatel.place(x=80,y=520)
    
    #TablaAlergias
    tablaAl = ttk.Treeview(w)
    tablaAl=ttk.Treeview(w,columns=("col1"), height=3)
    tablaAl.column("#0", width=80)
    tablaAl.column("col1",width=272, anchor=CENTER)
    tablaAl.heading("#0",text="Id",anchor=CENTER)
    tablaAl.heading("col1",text="Alergia",anchor=CENTER)
    tablaAl.place(x=385,y=520)