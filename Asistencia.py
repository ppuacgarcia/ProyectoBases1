from optparse import Values
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from Menu import *
from tkinter import ttk
from tkcalendar import *
from Conexion import conexion
import mariadb

class AsisForm:
    
    def __init__(self,pw, idEvento):
        self.idEvento = idEvento
        self.w = Frame(pw,width=1200,height=675,bg='#707070')
        self.conn = conexion()
        self.w.place(x=0, y=0)
        self.fuenteG = font=('Comic Sans MS', 19,'bold')
        self.fuenteP = font=('Comic Sans MS', 15,'bold')
        self.bglabel = '#707070'
        self.fglabel = '#FFFFFF'
        self.posx = 80
        self.img1 = ImageTk.PhotoImage(Image.open('Images/HM.png')) 
        Button(self.w, command = self.cmd, image=self.img1, border=0,activebackground='#000000', bg='#707070').place(x=5, y = 10)
        self.lab('Asistencia', self.fuenteG, self.bglabel, self.fglabel, 500, 10)

        self.confirmar = self.btn(self.w, 975, 600, 'confirmar asistencia', '#000000', '#FF4e10', self.confirmarAsistencia,'Arial', 12,'bold',18,2)
        self.buscar = self.btn(self.w, 60, 115, 'buscar', '#000000', '#FF4e10', self.buscarAdolescente,'Arial', 12,'bold',10,1)

        self.busqueda = StringVar()  

        self.referencia = self.Ent(self.busqueda, 64, 175, 115)

        #Tabla Adolescentes
        self.tabladata = ttk.Treeview(self.w)
        self.tabladata=ttk.Treeview(self.w,columns=("col1","col2","col3"), height=19)
        self.tabladata.column("#0", width=80)
        self.tabladata.column("col1",width=240, anchor=CENTER)
        self.tabladata.column("col2",width=100, anchor=CENTER)
        self.tabladata.column("col3",width=80, anchor=CENTER)
        self.tabladata.heading("#0",text="Id",anchor=CENTER)
        self.tabladata.heading("col1",text="Nombre",anchor=CENTER)
        self.tabladata.heading("col2",text="Genero",anchor=CENTER)
        self.tabladata.heading("col3",text="Fecha nacimiento",anchor=CENTER)
        self.tabladata.place(x=60,y=150)
        self.tabladata.bind("<Double-Button-1>",self.doubleClickTabla)
        
        
        #Tabla Asistencia
        self.tabla = ttk.Treeview(self.w)
        self.tabla=ttk.Treeview(self.w,columns=("col1","col2","col3"), height=21)
        self.tabla.column("#0", width=80)
        self.tabla.column("col1",width=240, anchor=CENTER)
        self.tabla.column("col2",width=100, anchor=CENTER)
        self.tabla.column("col3",width=80, anchor=CENTER)
        self.tabla.heading("#0",text="Id",anchor=CENTER)
        self.tabla.heading("col1",text="Nombre",anchor=CENTER)
        self.tabla.heading("col2",text="Genero",anchor=CENTER)
        self.tabla.heading("col3",text="Fecha nacimiento",anchor=CENTER)
        self.tabla.place(x=620,y=110)

    
        
    def cmd(self):
        self.w.destroy()
    

    #Labels formulario
    def lab(self,text, font, bg, fg, x, y):
        labe = Label(self.w,text=text, font=font, bg=bg, foreground=fg)
        labe.pack()
        labe.place(x=x, y=y)
    
    #Funcion para crear botones
    def btn(self,f1, x, y, text, bcolor, fcolor, command, font, siz, tipe,wdt,ht):
        #Botones para menu
        def on_enter(e):
            buttons['background'] = bcolor
            buttons['foreground'] = fcolor
            
        def on_leave(e):
            buttons['background'] = fcolor
            buttons['foreground'] = bcolor
            
            
        buttons = Button(self.w, width=wdt, height=ht, text= text, fg  = bcolor, bg=fcolor, command=command, border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
        buttons.bind("<Enter>", on_enter)
        buttons.bind("<Leave>", on_leave)
        buttons.place(x=x, y=y)
        return buttons
    
    
    def Ent(self,textvar, width, x, y):
        Entr = Entry(self.w,textvariable=textvar, width=width)
        Entr.pack()
        Entr.place(x=x, y=y)
        return Entr

    def mayus(self,nombreB):
        result=""
        for i in range ( len (nombreB) ):
            if(ord(nombreB[i])>96 and ord(nombreB[i])<122):
               result+=chr(ord(nombreB[i])-32)
            else:
                result+=nombreB[i]
        return result

    def doubleClickTabla(self,event):
        self.idViejo=str(self.tabladata.item(self.tabladata.selection())["text"])
        print(self.idViejo)
        print(self.idEvento)

    def confirmarAsistencia(self):
        self.conn.consultaBD("INSERT INTO AsistenciaAdolescente(Evento_id, Adolescente_id) VALUES(" + self.idEvento + ", " + self.idViejo + ")")
        self.mostrarDatos()
    
    def mostrarDatos(self,where=""):
        registro=self.tabladata.get_children()
        for registro in registro:
            self.tabladata.delete(registro)
        registro=self.tabla.get_children()
        for registro in registro:
            self.tabla.delete(registro)
        if len(where)>0:
            cur=self.conn.consultaBD("SELECT id, Nombre, Genero, FechaNacimiento FROM iglesia.adolescente " + where + " ORDER BY nombre DESC")
        else:
            cur=self.conn.consultaBD("SELECT id, nombre, genero, fechanacimiento FROM iglesia.adolescente ORDER BY nombre DESC")
        for (id,nombre,genero,fechanacimiento) in cur:
            self.tabladata.insert('',0,text=id,values=[nombre,genero,fechanacimiento])
        cur=self.conn.consultaBD("SELECT adolescente.id, adolescente.nombre, adolescente.genero, adolescente.fechanacimiento FROM iglesia.evento INNER JOIN iglesia.asistenciaadolescente ON evento.id = asistenciaadolescente.evento_id INNER JOIN iglesia.adolescente ON asistenciaadolescente.adolescente_id = adolescente.id WHERE evento.id = " + self.idEvento)
        for (id,nombre,genero,fechanacimiento) in cur:
            self.tabla.insert('',0,text=id,values=[nombre,genero,fechanacimiento])

    def buscarAdolescente(self):
        if (len(self.referencia.get())>0):
            self.mostrarDatos("WHERE Nombre = '" + self.mayus(self.referencia.get()) + "'")
    
    