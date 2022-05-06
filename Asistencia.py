from optparse import Values
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from Menu import *
from tkinter import ttk
from tkcalendar import *
import mariadb

class AsisForm:
    
    def __init__(self,pw, idEvento):
        self.w = Frame(pw,width=1200,height=675,bg='#707070')
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

    def confirmarAsistencia():
        None
        
    def cmd(self):
        self.w.destroy()
        
    def buscarAdolescente():
        None
    

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
     


    def consultaBD(self,query):
        try:
            conn=mariadb.connect(
                host="localhost",
                user="root",
                #password="123456789",
                password="Kamado_Tanjiro_12",
                database="iglesia",
                autocommit=True
            )
        except mariadb.Error as e:
            print("Error al conectarse a la bd",e)
        cur = conn.cursor()
        id2=cur.execute(query)
        print("PRIMERO   "+str(id2))
        return cur
    
    def mostrarDatos(self,where=""):
        registro=self.tabladata.get_children()
        for registro in registro:
            self.tabladata.delete(registro)
        if len(where)>0:
            cur=self.consultaBD("SELECT id, Nombre, Genero, FechaNacimiento FROM iglesia.adolescente " + where + " ORDER BY nombre DESC")
        else:
            cur=self.consultaBD("SELECT id, nombre, genero, fechanacimiento FROM iglesia.adolescente ORDER BY nombre DESC")
        for (id,nombre,genero,fechanacimiento) in cur:
            self.tabladata.insert('',0,text=id,values=[nombre,genero,fechanacimiento])
    
    
    