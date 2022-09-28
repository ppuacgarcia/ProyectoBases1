from optparse import Values
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from Menu import *
from tkinter import ttk
from tkcalendar import *
import mariadb
from Conexion import conexion

class ColForm:
    
    def __init__(self,ventanaPrincipal):
        self.w = Frame(ventanaPrincipal,width=1200,height=675,bg='#707070')
        self.conn = conexion()
        self.conn.autocommit = FALSE
        try:
            with open('Query.txt', 'a') as f:
                f.write("START TRANSACTION \n")
        except FileNotFoundError:
            print("The 'docs' directory does not exist")
        self.conn.consultaBD("SAVEPOINT identifier")
        self.w.place(x=0, y=0)
        self.fuenteG = font=('Comic Sans MS', 19,'bold')
        self.fuenteP = font=('Comic Sans MS', 15,'bold')
        self.bglabel = '#707070'
        self.fglabel = '#FFFFFF'
        self.posx = 80
        self.img1 = ImageTk.PhotoImage(Image.open('Images/HM.png')) 
        Button(self.w, command = self.cmd, image=self.img1, border=0,activebackground='#000000', bg='#707070').place(x=5, y = 10)

        #Etiquetas
        self.lab('Registro Colaboradores', self.fuenteG, self.bglabel, self.fglabel, 490, 10)
        self.lab('Datos Generales', self.fuenteG, self.bglabel, self.fglabel, self.posx, 55)
        self.lab('Nombre', self.fuenteP, self.bglabel, self.fglabel, self.posx, 95)
        self.lab('Fecha de Nacimiento', self.fuenteP, self.bglabel, self.fglabel, self.posx, 130)
        self.lab('Sexo', self.fuenteP, self.bglabel, self.fglabel, self.posx, 165)
        self.lab('Rango', self.fuenteP, self.bglabel, self.fglabel, self.posx, 200)
        self.lab('Informacion de Enmergencia', self.fuenteG, self.bglabel, self.fglabel, self.posx, 270)
        self.lab('Contacto', self.fuenteP, self.bglabel, self.fglabel, self.posx, 320)
        self.lab('Telefono', self.fuenteP, self.bglabel, self.fglabel, self.posx, 355)
        self.lab('Tipo de Sangre', self.fuenteP, self.bglabel, self.fglabel, self.posx, 390)
        self.lab('Alergias', self.fuenteP, self.bglabel, self.fglabel, self.posx, 425)
        self.lab('Telefono', self.fuenteP, self.bglabel, self.fglabel, self.posx, 230)

        #Cuadros de texto
        self.nombre=self.Ent(65, 175, 105)
        self.contacto=self.Ent(65, 175, 330)
        self.Telefono1=self.Ent(20, 175, 365)
        self.tipoSangre=self.Ent(54, 240, 400)
        self.alergia=self.Ent(20, 175, 435)
        self.telefonoColab=self.Ent(20, 175, 240)

        #comboBox
        self.valrang = ['Ministro','Lider','Teacher']
        self.comboRan = ttk.Combobox(self.w, value=self.valrang, width=62)
        self.comboRan.place(x=175, y=210)
        self.comboRan["state"]="readonly"
        self.comboRan.current(2)
        
        self.valS = ['Masculino', 'Femenino']
        self.comboS = ttk.Combobox(self.w, value=self.valS, width=62)
        self.comboS.place(x=175, y=175)
        self.comboS["state"]="readonly"
        self.comboS.current(0)

        #Calendario
        self.cal=DateEntry(self.w,width=30)
        self.cal.place(x=295,y=140)

        #Botones
        self.Guardar = self.btn(975, 600, 'guardar', '#000000', '#FF4e10', self.agregarRegistro,'Arial', 12,'bold',18,2)
        self.GuardarTel = self.btn(self.posx+230,361,'guardar telefono','#000000','#FF4e10',self.agregarTelefono,'Arial',12,'bold',13,1)
        self.GuardarAl = self.btn(self.posx+230,431,'guardar alergia','#000000','#FF4e10',self.agregarAlergia,'Arial',12,'bold',13,1)
        self.Borrar = self.btn(575, 600, 'Borrar', '#000000', '#FF4e10', self.borrarRegistro,'Arial', 12,'bold',18,2)
        self.Editar = self.btn(775, 600, 'Editar', '#000000', '#FF4e10', self.editarRegistro,'Arial', 12,'bold',18,2)
        self.GuardarTelCol = self.btn(self.posx+230,233,'guardar telefono','#000000','#FF4e10',self.agregarTelefonoCol,'Arial',12,'bold',13,1)

        #Listas
        self.listaTelefono=self.tb(450,365)
        self.listaAlergia=self.tb(450,435)
        self.listaTelefonoColab=self.tb(450,240)

        #Tablas
        self.tabladata = ttk.Treeview(self.w)
        self.tabladata=ttk.Treeview(self.w,columns=("col1","col2","col3"), height=21)
        self.tabladata.column("#0", width=80)
        self.tabladata.column("col1",width=240, anchor=CENTER)
        self.tabladata.column("col2",width=100, anchor=CENTER)
        self.tabladata.column("col3",width=80, anchor=CENTER)
        self.tabladata.heading("#0",text="Id",anchor=CENTER)
        self.tabladata.heading("col1",text="Nombre",anchor=CENTER)
        self.tabladata.heading("col2",text="Genero",anchor=CENTER)
        self.tabladata.heading("col3",text="Edad",anchor=CENTER)
        self.tabladata.place(x=620,y=100)
        self.tabladata.bind("<Double-Button-1>",self.doubleClickTabla)
        
    def cmd(self):
        self.conn.commit()
        self.w.destroy()

    #Labels formulario
    def lab(self,text, font, bg, fg, x, y):
        labe = Label(self.w,text=text, font=font, bg=bg, foreground=fg)
        labe.pack()
        labe.place(x=x, y=y)
    
    #Cuadros de Texto
    def Ent(self, width, x, y):
        Entr = Entry(self.w,width=width)
        Entr.pack()
        Entr.place(x=x, y=y)
        return Entr

    #Funcion para crear botones
    def btn(self, x, y, text, bcolor, fcolor, command, font, siz, tipe,wdt,ht):
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
    
    def tb(self,x,y):
        tabla=Listbox(self.w)
        tabla.place(x=x,y=y)
        tabla.config(height=1)
        return tabla
    
    
    def agregarTelefono(self):
        if len(self.Telefono1.get())!=0:
            self.listaTelefono.insert(END,self.Telefono1.get())

    def agregarTelefonoCol(self):
        if len(self.telefonoColab.get())!=0:
            self.listaTelefonoColab.insert(END,self.telefonoColab.get())

    def agregarAlergia(self,):
        if len(self.alergia.get())!=0:
            self.listaAlergia.insert(END,self.alergia.get())

    def mayus(self,nombreB):
        result=""
        for i in range ( len (nombreB) ):
            if(ord(nombreB[i])>96 and ord(nombreB[i])<122):
               result+=chr(ord(nombreB[i])-32)
            else:
                result+=nombreB[i]
        return result
    
    
    def mostrarDatos(self,where=""):
        registro=self.tabladata.get_children()
        for registro in registro:
            self.tabladata.delete(registro)
        if len(where)>0:
            cur=self.conn.consultaBD("SELECT id,FechaNacimiento , Nombre, Genero FROM iglesia.colaborador " + where)
        else:
            cur=self.conn.consultaBD(" SELECT id,FechaNacimiento , Nombre, Genero FROM iglesia.colaborador ;")
        for (id,fechanacimiento,nombre,genero) in cur:
            self.tabladata.insert('',0,text=id,values=[nombre,genero,fechanacimiento])
            
    def agregarRegistro(self,):
        if len(self.nombre.get())!=0 and len(self.contacto.get())!=0 and len(self.tipoSangre.get())!=0:
            query="call InsertarColab('" + self.nombre.get() + "', '" + self.comboS.get() + "','" + str(self.cal.get_date()) + "','"+self.comboRan.get()+"');"
            self.conn.consultaBD(query)
            query="call InsertarIEC('" + self.nombre.get() + "', '" + self.tipoSangre.get() + "', '" + self.contacto.get() + "');"
            self.conn.consultaBD(query)
            for telefono in self.listaTelefono.get(0,END):
                query="call InsertarTIEC('" + self.nombre.get() + "', '" + telefono + "');"
                self.conn.consultaBD(query)
            for telefono in self.listaTelefonoColab.get(0,END):
                query="call InsertarTC('" + self.nombre.get() + "', '" + telefono + "');"
                self.conn.consultaBD(query)
            for alergia in self.listaAlergia.get(0,END):
                query="call InsertarAC('" +self.nombre.get() + "', '" + alergia + "');"
                self.conn.consultaBD(query)
            self.conn.consultaBD("SAVEPOINT identifier")
        self.nombre.focus()
        self.mostrarDatos()

    def doubleClickTabla(self,event):
        self.idViejo=str(self.tabladata.item(self.tabladata.selection())["text"])
        self.nombre.delete(0,END)
        self.comboS.current(0)
        self.tipoSangre.delete(0,END)
        self.contacto.delete(0,END)
        self.listaTelefono.delete(0,END)
        self.listaTelefonoColab.delete(0,END)
        self.listaAlergia.delete(0,END)
        self.alergia.delete(0,END)
        self.Telefono1.delete(0,END)
        self.telefonoColab.delete(0,END)
        self.mostrarDatos()
        self.Guardar["state"]="disable"
        self.GuardarTel["state"]="normal"
        self.GuardarTelCol["state"]="normal"
        self.GuardarAl["state"]="normal"
        self.Editar["state"]="normal"
        self.Borrar["state"]="normal"
        
        cur=self.conn.consultaBD("SELECT colaborador.nombre, colaborador.genero, colaborador.fechanacimiento, infoemergencia.tiposangre, infoemergencia.encargado FROM iglesia.colaborador JOIN iglesia.infoemergencia ON colaborador.id = infoemergencia.colaborador_id WHERE colaborador.id = '" + self.idViejo + "';")
        for (nombre,genero,fechanacimiento,tiposangre,encargado) in cur:
            self.nombre.insert(0,nombre)
            self.comboS.insert(0,genero)
            self.cal.set_date(fechanacimiento)
            self.tipoSangre.insert(0,tiposangre)
            self.contacto.insert(0,encargado)

    def borrarRegistro(self, where = ""):
        if len(self.nombre.get())!=0 and len(self.contacto.get())!=0 and len(self.tipoSangre.get())!=0:
            query="call BorrarColaborador('" + self.mayus(self.nombre.get()) + "');"
            self.conn.consultaBD(query)
            self.nombre.delete(0,END)
            self.comboS.current(0)
            self.tipoSangre.delete(0,END)
            self.contacto.delete(0,END)
            self.listaTelefono.delete(0,END)
            self.listaTelefonoColab.delete(0,END)
            self.listaAlergia.delete(0,END)
            self.nombre.focus()
            self.alergia.delete(0,END)
            self.Telefono1.delete(0,END)
            self.telefonoColab.delete(0,END)
            self.mostrarDatos()
            self.conn.consultaBD("SAVEPOINT identifier")
        self.Guardar["state"]="normal"
        self.GuardarTel["state"]="normal"
        self.GuardarTelCol["state"]="normal"
        self.GuardarAl["state"]="normal"
        self.Editar["state"]="disable"
        self.Borrar["state"]="disable"
        
    def editarRegistro(self, where = ""):
        if len(self.nombre.get())!=0 and len(self.contacto.get())!=0 and len(self.tipoSangre.get())!=0:
            query="UPDATE iglesia.Colaborador SET nombre='" + self.mayus(self.nombre.get()) + "', genero='" + self.mayus(self.comboS.get()) + "', fechanacimiento='" + str(self.cal.get_date()) + "' where id='" + self.idViejo + "';"
            self.conn.consultaBD(query)
            query="UPDATE iglesia.infoemergencia SET tiposangre='" + self.mayus(self.tipoSangre.get()) + "', encargado='" + self.mayus(self.contacto.get()) +"' where Colaborador_id='" + self.idViejo + "';"
            self.conn.consultaBD(query)
            for telefono in self.listaTelefono.get(0,END):
                query="call InsertarTIEC('" + self.mayus(self.nombre.get()) + "', '" + telefono + "');"
                self.conn.consultaBD(query)
            for alergia in self.listaAlergia.get(0,END):
                query="call InsertarAC('" + self.mayus(self.nombre.get()) + "', '" + self.mayus(alergia) + "');"
                self.conn.consultaBD(query)
            self.nombre.delete(0,END)
            self.comboS.current(0)
            self.tipoSangre.delete(0,END)
            self.contacto.delete(0,END)
            self.listaTelefono.delete(0,END)
            self.listaTelefonoColab.delete(0,END)
            self.listaAlergia.delete(0,END)
            self.nombre.focus()
            self.alergia.delete(0,END)
            self.Telefono1.delete(0,END)
            self.telefonoColab.delete(0,END)
            self.mostrarDatos()
        self.Guardar["state"]="normal"
        self.GuardarTel["state"]="normal"
        self.GuardarTelCol["state"]="normal"
        self.GuardarAl["state"]="normal"
        self.Editar["state"]="disable"
        self.Borrar["state"]="disable"
    
    

