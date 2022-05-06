from calendar import calendar
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from Menu import *
from tkcalendar import *
from tkinter import ttk
from Asistencia import AsisForm

def EvtForm(pw):
    

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
        
    def edit():
        None
        
    def delete():
        None
        
    def Asistencia():
        AsisForm(pw, 1)
        
    global img1
    img1 = ImageTk.PhotoImage(Image.open('Images/HM.png')) 
    Button(w, command = cmd, image=img1, border=0,activebackground='#000000', bg='#707070').place(x=5, y = 10)

    #Labels formulario
    def lab(text, font, bg, fg, x, y):
        labe = Label(w,text=text, font=font, bg=bg, foreground=fg)
        labe.pack()
        labe.place(x=x, y=y)


    lab('Eventos', fuenteG, bglabel, fglabel, 490, 10)
    lab('Datos Evento', fuenteG, bglabel, fglabel, posx, 55)
    lab('Nombre.', fuenteP, bglabel, fglabel, posx, 95)
    lab('Fecha', fuenteP, bglabel, fglabel, posx, 130)
    lab('Hora (HH:MM)', fuenteP, bglabel, fglabel, posx, 165)
    lab('Lugar', fuenteP, bglabel, fglabel, posx, 200)
    lab('Eventos: ', fuenteG, bglabel, fglabel, 100, 300 )
    name = StringVar()
    Lugar = StringVar()
    Hora= StringVar()

    def Ent(textvar, width, x, y):
        Entr = Entry(w,textvariable=textvar, width=width)
        Entr.pack()
        Entr.place(x=x, y=y)
        

    Ent(name, 156, 175, 105)
    Ent(Hora, 143, 250, 175)
    Ent(Lugar, 155, 175, 210)
    cal=DateEntry(w,width=30)
    cal.place(x=175,y=140)
    
   

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
    
    btn(w, 980, 275, 'guardar', '#000000', '#FF4e10', Sav,'Arial', 12,'bold')
    btn(w, 980, 600, 'editar', '#000000', '#FF4e10', edit,'Arial', 12,'bold')
    btn(w, 750, 600, 'borrar', '#000000', '#FF4e10', delete,'Arial', 12,'bold')
    btn(w, 100, 600, 'Asistencia', '#000000', '#FF4e10', Asistencia,'Arial', 12,'bold')
    
    
    #Agenda en tabla
    tabladata = ttk.Treeview(w)
    tabladata=ttk.Treeview(w,columns=("col1","col2","col3","col4"))
    tabladata.column("#0", width=80)
    tabladata.column("col1",width=360, anchor=CENTER)
    tabladata.column("col2",width=100, anchor=CENTER)
    tabladata.column("col3",width=100, anchor=CENTER)
    tabladata.column("col4",width=100, anchor=CENTER)
    tabladata.heading("#0",text="Id",anchor=CENTER)
    tabladata.heading("col1",text="Evento",anchor=CENTER)
    tabladata.heading("col2",text="Fecha",anchor=CENTER)
    tabladata.heading("col3",text="Hora",anchor=CENTER)
    tabladata.heading("col4",text="Lugar",anchor=CENTER)
    tabladata.place(x=230,y=340)