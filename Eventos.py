from calendar import calendar
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from Menu import *
from tkcalendar import *
from tkinter import ttk
from Asistencia import AsisForm

class EvtForm:
    
    def __init__(self,pw):
        self.principal = pw
        self.w = Frame(pw,width=1200,height=675,bg='#707070')
        self.w.place(x=0, y=0)
        self.fuenteG = font=('Comic Sans MS', 19,'bold')
        self.fuenteP = font=('Comic Sans MS', 15,'bold')
        self.bglabel = '#707070'
        self.fglabel = '#FFFFFF'
        self.posx = 80
        self.img1 = ImageTk.PhotoImage(Image.open('Images/HM.png')) 
        Button(self.w, command = self.cmd, image=self.img1, border=0,activebackground='#000000', bg='#707070').place(x=5, y = 10)

        self.lab('Eventos', self.fuenteG, self.bglabel, self.fglabel, 490, 10)
        self.lab('Datos Evento', self.fuenteG, self.bglabel, self.fglabel, self.posx, 55)
        self.lab('Nombre.', self.fuenteP, self.bglabel, self.fglabel, self.posx, 95)
        self.lab('Fecha', self.fuenteP, self.bglabel, self.fglabel, self.posx, 130)
        self.lab('Hora (HH:MM)', self.fuenteP, self.bglabel, self.fglabel, self.posx, 165)
        self.lab('Lugar', self.fuenteP, self.bglabel, self.fglabel, self.posx, 200)
        self.lab('Eventos: ', self.fuenteG, self.bglabel, self.fglabel, 100, 300 )
        
        self.name = StringVar()
        self.LugarE = StringVar()
        self.HoraE= StringVar()
        self.nombre = self.Ent(self.name, 156, 175, 105)
        self.hora = self.Ent(self.HoraE, 143, 250, 175)
        self.lugar = self.Ent(self.LugarE, 155, 175, 210)
        self.cal=DateEntry(self.w,width=30)
        self.cal.place(x=175,y=140)

        self.guardar = self.btn(self.w, 980, 275, 'guardar', '#000000', '#FF4e10', self.Sav,'Arial', 12,'bold')
        self.editar = self.btn(self.w, 980, 600, 'editar', '#000000', '#FF4e10', self.edit,'Arial', 12,'bold')
        self.borrar = self.btn(self.w, 750, 600, 'borrar', '#000000', '#FF4e10', self.delete,'Arial', 12,'bold')
        self.asistencia = self.btn(self.w, 100, 600, 'Asistencia', '#000000', '#FF4e10', self.Asistencia,'Arial', 12,'bold')

        #Agenda en tabla
        self.tabladata = ttk.Treeview(self.w)
        self.tabladata=ttk.Treeview(self.w,columns=("col1","col2","col3","col4"))
        self.tabladata.column("#0", width=80)
        self.tabladata.column("col1",width=360, anchor=CENTER)
        self.tabladata.column("col2",width=100, anchor=CENTER)
        self.tabladata.column("col3",width=100, anchor=CENTER)
        self.tabladata.column("col4",width=100, anchor=CENTER)
        self.tabladata.heading("#0",text="Id",anchor=CENTER)
        self.tabladata.heading("col1",text="Evento",anchor=CENTER)
        self.tabladata.heading("col2",text="Fecha",anchor=CENTER)
        self.tabladata.heading("col3",text="Hora",anchor=CENTER)
        self.tabladata.heading("col4",text="Lugar",anchor=CENTER)
        self.tabladata.place(x=230,y=340)

    def Sav(self):
        None
        
    def cmd(self):
        self.w.destroy()
        
    def edit(self):
        None
        
    def delete(self):
        None
        
    def Asistencia(self):
        AsisForm(self.principal, 1)
    

    #Labels formulario
    def lab(self, text, font, bg, fg, x, y):
        labe = Label(self.w,text=text, font=font, bg=bg, foreground=fg)
        labe.pack()
        labe.place(x=x, y=y)


    

    def Ent(self, textvar, width, x, y):
        Entr = Entry(self.w,textvariable=textvar, width=width)
        Entr.pack()
        Entr.place(x=x, y=y)
        

    
    
   

    def btn(self, f1, x, y, text, bcolor, fcolor, command, font, siz, tipe):
        #Botones para menu
        def on_enter(e):
            buttons['background'] = bcolor
            buttons['foreground'] = fcolor
            
        def on_leave(e):
            buttons['background'] = fcolor
            buttons['foreground'] = bcolor
            
            
        buttons = Button(self.w, width=18, height=2, text= text, fg  = bcolor, bg=fcolor, command=command, border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
        buttons.bind("<Enter>", on_enter)
        buttons.bind("<Leave>", on_leave)
        buttons.place(x=x, y=y)
    
    
    
    
    