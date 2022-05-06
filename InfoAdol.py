from optparse import Values
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from Menu import *
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
import mariadb

class adolinfo:
    
    def __init__(self,pw):
        self.w = Frame(pw,width=1200,height=675,bg='#707070')
        self.w.place(x=0, y=0)
        self.fuenteG = font=('Comic Sans MS', 19,'bold')
        self.fuenteP = font=('Comic Sans MS', 15,'bold')
        self.bglabel = '#707070'
        self.fglabel = '#FFFFFF'
        self.posx = 80
        self.posx2 = 790
        self.img1 = ImageTk.PhotoImage(Image.open('Images/HM.png')) 
        Button(self.w, command = self.cmd, image=self.img1, border=0,activebackground='#000000', bg='#707070').place(x=5, y = 10)

        self.lab('Informacion Adolescentes', self.fuenteG, self.bglabel, self.fglabel, 490, 10)
        self.lab('Busquedas:', self.fuenteG, self.bglabel, self.fglabel, self.posx, 55)
        self.lab('Nombre:', self.fuenteP, self.bglabel, self.fglabel, self.posx2, 170)
        self.lab('Genero:', self.fuenteP, self.bglabel, self.fglabel, self.posx2, 230)
        self.lab('Edad:', self.fuenteP, self.bglabel, self.fglabel, self.posx2, 290)
        self.lab('Tipo Sangre:', self.fuenteP, self.bglabel, self.fglabel, self.posx2, 348)
        self.lab('Contacto Enmergencia:', self.fuenteP, self.bglabel, self.fglabel, self.posx2, 408)

        self.busc = StringVar()
        self.NombreS = StringVar()
        self.GeneroS = StringVar()
        self.EdadS = StringVar()
        self.TSangre = StringVar()
        self.CEnmerg = StringVar()
        self.buscar = self.Ent(self.busc, 55, 220, 72)
        self.nombre = self.Ent(self.NombreS, 57, 800, 200)
        self.genero = self.Ent(self.GeneroS, 57, 800, 260)
        self.fecha = self.Ent(self.EdadS, 57, 800, 320)
        self.tipoSangre = self.Ent(self.TSangre, 57, 800, 380)
        self.contacto = self.Ent(self.CEnmerg, 57, 800, 440)

        valS = ['MASCULINO', 'FEMENINO']
        self.comboS = ttk.Combobox(self.w, value=valS, width=25)
        self.comboS.place(x=805, y=72)
        self.comboS["state"]="readonly"
        self.comboS.current(0)

        self.buscarNombre = self.btn(self.w, 570, 72, 'Nombre', '#000000', '#FF4e10', self.NomSearch,'Arial', 12,'bold',10,1)
        self.buscarFecha = self.btn(self.w, 680, 72, 'Edad', '#000000', '#FF4e10', self.FechaSearch,'Arial', 12,'bold',10,1)
        self.buscarGenero = self.btn(self.w, 1010, 72, 'Genero', '#000000', '#FF4e10', self.GenSearch,'Arial', 12,'bold',10,1)

        #Tabla
        self.tabladata = ttk.Treeview(self.w)
        self.tabladata=ttk.Treeview(self.w,columns=("col1","col2","col3", "col4", "col5"), height=18)
        self.tabladata.column("#0", width=80)
        self.tabladata.column("col1",width=200, anchor=CENTER)
        self.tabladata.column("col2",width=100, anchor=CENTER)
        self.tabladata.column("col3",width=80, anchor=CENTER)
        self.tabladata.column("col4",width=80, anchor=CENTER)
        self.tabladata.column("col5",width=120, anchor=CENTER)
        self.tabladata.heading("#0",text="Id",anchor=CENTER)
        self.tabladata.heading("col1",text="Nombre",anchor=CENTER)
        self.tabladata.heading("col2",text="Genero",anchor=CENTER)
        self.tabladata.heading("col3",text="Fecha Nacimiento",anchor=CENTER)
        self.tabladata.heading("col4",text="Tipo Sangre",anchor=CENTER)
        self.tabladata.heading("col5",text="Contacto Enmerg",anchor=CENTER)
        self.tabladata.place(x=80,y=120)
        self.tabladata.bind("<Double-Button-1>",self.doubleClickTabla)
        
        #TablaTElefonos
        self.tablatel = ttk.Treeview(self.w)
        self.tablatel=ttk.Treeview(self.w,columns=("col1"), height=3)
        self.tablatel.column("#0", width=80)
        self.tablatel.column("col1",width=200, anchor=CENTER)
        self.tablatel.heading("#0",text="Id",anchor=CENTER)
        self.tablatel.heading("col1",text="Telefono",anchor=CENTER)
        self.tablatel.place(x=80,y=520)
        
        #TablaAlergias
        self.tablaAl = ttk.Treeview(self.w)
        self.tablaAl=ttk.Treeview(self.w,columns=("col1"), height=3)
        self.tablaAl.column("#0", width=80)
        self.tablaAl.column("col1",width=272, anchor=CENTER)
        self.tablaAl.heading("#0",text="Id",anchor=CENTER)
        self.tablaAl.heading("col1",text="Alergia",anchor=CENTER)
        self.tablaAl.place(x=385,y=520)

    def Sav():
        None
        
    def cmd(self):
        self.w.destroy()
        
    def borrarRegistro():
        None
    
    def editarRegistro():
        None   
        
    
        
    

    #Labels formulario
    def lab(self,text, font, bg, fg, x, y):
        labe = Label(self.w,text=text, font=font, bg=bg, foreground=fg)
        labe.pack()
        labe.place(x=x, y=y)

    #Cuadros de Texto
    def Ent(self,textvar, width, x, y):
        Entr = Entry(self.w,textvariable=textvar, width=width)
        Entr.pack()
        Entr.place(x=x, y=y)
        return Entr

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

    #Metodos para ingresar a la base de datos
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
            cur=self.consultaBD("SELECT adolescente.id,adolescente.nombre, adolescente.genero, adolescente.fechanacimiento, infoemergencia.tiposangre, infoemergencia.encargado FROM iglesia.adolescente JOIN iglesia.infoemergencia ON adolescente.id = infoemergencia.adolescente_id " + where)
        else:
            cur=self.consultaBD("SELECT adolescente.id,adolescente.nombre, adolescente.genero, adolescente.fechanacimiento, infoemergencia.tiposangre, infoemergencia.encargado FROM iglesia.adolescente JOIN iglesia.infoemergencia ON adolescente.id = infoemergencia.adolescente_id;")
        for (id,nombre,genero,fechanacimiento,tiposangre,encargado) in cur:
            self.tabladata.insert('',0,text=id,values=[nombre,genero,fechanacimiento,tiposangre,encargado])

    def doubleClickTabla(self,event):
        self.idViejo=str(self.tabladata.item(self.tabladata.selection())["text"])
        self.nombre.delete(0,END)
        self.genero.delete(0,END)
        self.tipoSangre.delete(0,END)
        self.contacto.delete(0,END)
        self.fecha.delete(0,END)
        for i in self.tablatel.get_children():
            self.tablatel.delete(i)
        for i in self.tablaAl.get_children():
            self.tablaAl.delete(i)
        #self.mostrarDatos()
        
        cur=self.consultaBD("SELECT adolescente.nombre, adolescente.genero, adolescente.fechanacimiento, infoemergencia.tiposangre, infoemergencia.encargado FROM iglesia.adolescente JOIN iglesia.infoemergencia ON adolescente.id = infoemergencia.adolescente_id WHERE adolescente.id = '" + self.idViejo + "';")
        for (nombre,genero,fechanacimiento,tiposangre,encargado) in cur:
            self.nombre.insert(0,nombre)
            self.genero.insert(0,genero)
            self.fecha.insert(0,fechanacimiento.strftime('%m/%d/%Y'))
            self.tipoSangre.insert(0,tiposangre)
            self.contacto.insert(0,encargado)

        cur=self.consultaBD("SELECT telefono.id, telefono.telefono FROM iglesia.telefono JOIN iglesia.infoemergencia ON telefono.infoemergencia_id = infoemergencia.id JOIN iglesia.adolescente ON infoemergencia.adolescente_id = adolescente.id WHERE adolescente.id = '" + self.idViejo + "';")
        for (id, telefono) in cur:
            self.tablatel.insert('',0,text=id,values=telefono)

        cur=self.consultaBD("SELECT alergia.id, alergia.detalle FROM iglesia.alergia JOIN iglesia.infoemergencia ON alergia.infoemergencia_id = infoemergencia.id JOIN iglesia.adolescente ON infoemergencia.adolescente_id = adolescente.id WHERE adolescente.id = '" + self.idViejo + "';")
        for (id, detalle) in cur:
            self.tablaAl.insert('',0,text=id,values=detalle)
        self.buscar.delete(0,END)

    def NomSearch(self):
        where=" where 1=1 "
        if len(self.buscar.get())>0:
            where = where + "and adolescente.nombre='" + self.buscar.get() + "' "
        self.mostrarDatos(where)
        

    def GenSearch(self):
        where=" where 1=1 "
        if len(self.comboS.get())>0:
            where = where + "and adolescente.genero='" + self.comboS.get() + "' "
        self.mostrarDatos(where)
        

    def FechaSearch(self):
        where=" where 1=1 "
        if len(self.buscar.get())>0:
            where = where + "and (YEAR(NOW()) - YEAR(adolescente.fechanacimiento)) = '" + self.buscar.get() + "' "
        self.mostrarDatos(where)
        