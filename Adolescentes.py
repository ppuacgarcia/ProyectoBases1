from asyncio.windows_events import NULL
from optparse import Values
from tkinter import *
from PIL import Image, ImageTk
from Menu import *
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
import mariadb
class AdolForm:
    
    def __init__(self,ventanaPrincipal):
        self.w = Frame(ventanaPrincipal,width=1200,height=675,bg='#707070')
        self.w.place(x=0, y=0)
        self.fuenteG = font=('Comic Sans MS', 19,'bold')
        self.fuenteP = font=('Comic Sans MS', 15,'bold')
        self.bglabel = '#707070'
        self.fglabel = '#FFFFFF'
        self.posx = 80
        self.img1 = ImageTk.PhotoImage(Image.open('Images/HM.png')) 
        Button(self.w, command = self.cmd, image=self.img1, border=0,activebackground='#000000', bg='#707070').place(x=5, y = 10)

        #Etiquetas
        self.lab('Registro Adolescentes', self.fuenteG, self.bglabel, self.fglabel, 490, 10)
        self.lab('Datos Generales', self.fuenteG, self.bglabel, self.fglabel, self.posx, 55)
        self.lab('Nombre', self.fuenteP, self.bglabel, self.fglabel, self.posx, 95)
        self.lab('Fecha de Nacimiento', self.fuenteP, self.bglabel, self.fglabel, self.posx, 130)
        self.lab('Genero', self.fuenteP, self.bglabel, self.fglabel, self.posx, 165)
        self.lab('Telefono', self.fuenteP, self.bglabel, self.fglabel, self.posx, 200)
        self.lab('Informacion de Enmergencia', self.fuenteG, self.bglabel, self.fglabel, self.posx, 240)
        self.lab('Contacto', self.fuenteP, self.bglabel, self.fglabel, self.posx, 290)
        self.lab('Telefono', self.fuenteP, self.bglabel, self.fglabel, self.posx, 325)
        self.lab('Tipo de Sangre', self.fuenteP, self.bglabel, self.fglabel, self.posx, 360)
        self.lab('Alergias', self.fuenteP, self.bglabel, self.fglabel, self.posx, 395)

        #Cuadros de texto
        self.nombre=self.Ent(self.w,65,175,105)
        #self.genero=self.Ent(self.w,155,175,175)
        self.contacto=self.Ent(self.w,65, 175, 300)
        self.telefono=self.Ent(self.w,20, 175, 335)
        self.tipoSangre=self.Ent(self.w,55, 240, 370)
        self.alergia=self.Ent(self.w,20, 175, 405)
        self.telefonoadol=self.Ent(self.w,20, 175, 210)

        #ComboBox
        self.genero=ttk.Combobox(self.w,width=62)
        self.genero['values']=('MASCULINO','FEMENINO')
        self.genero.current(0)
        self.genero["state"]="readonly"
        self.genero.pack()
        self.genero.place(x=175,y=175)

        #Calendario
        self.calendario=DateEntry(self.w,width=30)
        self.calendario.place(x=295,y=140)

        #Botones
        self.guardarAdolecente=self.btn(self.w, 975, 600, 'Guardar', '#000000', '#FF4e10', self.agregarRegistro,'Arial', 12,'bold',18,2)
        self.guardarTelefono=self.btn(self.w,self.posx+230,331,'Guardar Telefono','#000000','#FF4e10',self.agregarTelefono,'Arial',12,'bold',13,1)
        self.guardarAlergia=self.btn(self.w,self.posx+230,401,'Guardar Alergia','#000000','#FF4e10',self.agregarAlergia,'Arial',12,'bold',13,1)
        self.borrar=self.btn(self.w, 575, 600, 'Borrar', '#000000', '#FF4e10', self.borrarRegistro,'Arial', 12,'bold',18,2)
        self.editar=self.btn(self.w, 775, 600, 'Editar', '#000000', '#FF4e10', self.editarRegistro,'Arial', 12,'bold',18,2)
        self.guardarTelefonoAdo=self.btn(self.w,self.posx+230,200,'Guardar Telefono','#000000','#FF4e10',self.agregarTelefono,'Arial',12,'bold',13,1)
        
        #Listas
        self.listaTelefono=self.tb(self.w,450,335)
        self.listaAlergia=self.tb(self.w,450,405)
        self.listaTelefonoAdol=self.tb(self.w,450,210)
        
        #Tabla
        self.tabla=ttk.Treeview(self.w,columns=("col1","col2","col3"),height=21)
        self.tabla.column("#0", width=40)
        self.tabla.column("col1",width=225, anchor=CENTER)
        self.tabla.column("col2",width=100, anchor=CENTER)
        self.tabla.column("col3",width=150, anchor=CENTER)
        self.tabla.heading("#0",text="Id",anchor=CENTER)
        self.tabla.heading("col1",text="Nombre",anchor=CENTER)
        self.tabla.heading("col2",text="Genero",anchor=CENTER)
        self.tabla.heading("col3",text="Fecha Nacimiento",anchor=CENTER)
        self.tabla.place(x=620,y=100)
        self.tabla.bind("<Double-Button-1>",self.doubleClickTabla)
        
        
   
    

    def Sav(self):
        None
        
    def cmd(self):
        self.w.destroy()

    #Metodos para objetos del frame
    def lab(self,text, font, bg, fg, x, y):
        labe = Label(self.w,text=text, font=font, bg=bg, foreground=fg)
        labe.pack()
        labe.place(x=x, y=y)

    def Ent(self,w, width, x, y):
        Entr = Entry(w, width=width)
        Entr.pack()
        Entr.place(x=x, y=y)
        return Entr
        
    def btn(self,w, x, y, text, bcolor, fcolor, command, font, siz, tipe,wdt,ht):
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
        return buttons

    def tb(self,w,x,y):
        tabla=Listbox(w)
        tabla.place(x=x,y=y)
        tabla.config(height=1)
        return tabla

    #Agregar datos a las listas
    def agregarTelefono(self):
        if len(self.telefono.get())!=0:
            self.listaTelefono.insert(END,self.telefono.get())

    def agregarAlergia(self):
        if len(self.alergia.get())!=0:
            self.listaAlergia.insert(END,self.alergia.get())

    #Llenar cuadros de texto

    #Convertir cadenas a mayuscula
    def mayus(self,nombreB):
        result=""
        for i in range ( len (nombreB) ):
            if(ord(nombreB[i])>96 and ord(nombreB[i])<122):
               result+=chr(ord(nombreB[i])-32)
            else:
                result+=nombreB[i]
        return result


    #Metodos para ingresar a la base de datos
    def consultaBD(self,query):
        try:
            conn=mariadb.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="iglesia",
                autocommit=True
            )
        except mariadb.Error as e:
            print("Error al conectarse a la bd",e)
        cur = conn.cursor()
        id2=cur.execute(query)
        print("PRIMERO   "+str(id2))
        return cur

    def obtenerID(self,query):
        id = str(self.consultaBD(query))
        records = self.consultaBD(query).fetchall()
        print("\nPrinting each row")
        for row in records:
            print("Id = ", row[0], )
            permaID=row[0]
        return str(permaID)

    def agregarRegistro(self):
        if len(self.nombre.get())!=0 and len(self.contacto.get())!=0 and len(self.tipoSangre.get())!=0:
            query="call InsertarAdolescente('" + self.mayus(self.nombre.get()) + "', '" + self.mayus(self.genero.get()) + "','" + str(self.calendario.get_date()) + "');"
            self.consultaBD(query)
            query="call InsertarIEA('" + self.mayus(self.nombre.get()) + "', '" + self.mayus(self.tipoSangre.get()) + "', '" + self.mayus(self.contacto.get()) + "');"
            self.consultaBD(query)
            for telefono in self.listaTelefono.get(0,END):
                query="call InsertarTIEA('" + self.mayus(self.nombre.get()) + "', '" + telefono + "');"
                self.consultaBD(query)
            for alergia in self.listaAlergia.get(0,END):
                query="call InsertarAA('" + self.mayus(self.nombre.get()) + "', '" + self.mayus(alergia) + "');"
                self.consultaBD(query)
        self.nombre.delete(0,END)
        self.genero.current(0)
        self.tipoSangre.delete(0,END)
        self.contacto.delete(0,END)
        self.listaTelefono.delete(0,END)
        self.listaAlergia.delete(0,END)
        self.nombre.focus()
        self.alergia.delete(0,END)
        self.telefono.delete(0,END)
        self.mostrarDatos()

    def mostrarDatos(self,where=""):
        registro=self.tabla.get_children()
        for registro in registro:
            self.tabla.delete(registro)
        if len(where)>0:
            cur=self.consultaBD("SELECT id, Nombre, Genero, FechaNacimiento FROM iglesia.adolescente " + where)
        else:
            cur=self.consultaBD("SELECT id, nombre, genero, fechanacimiento FROM iglesia.adolescente")
        for (id,nombre,genero,fechanacimiento) in cur:
            self.tabla.insert('',0,text=id,values=[nombre,genero,fechanacimiento])

    def doubleClickTabla(self,event):
        self.idViejo=str(self.tabla.item(self.tabla.selection())["text"])
        self.nombre.delete(0,END)
        self.genero.current(0)
        self.tipoSangre.delete(0,END)
        self.contacto.delete(0,END)
        self.listaTelefono.delete(0,END)
        self.listaAlergia.delete(0,END)
        self.alergia.delete(0,END)
        self.telefono.delete(0,END)
        self.mostrarDatos()
        self.guardarAdolecente["state"]="disable"
        self.guardarTelefono["state"]="normal"
        self.guardarAlergia["state"]="normal"
        self.editar["state"]="normal"
        self.borrar["state"]="normal"
        
        cur=self.consultaBD("SELECT adolescente.nombre, adolescente.genero, adolescente.fechanacimiento, infoemergencia.tiposangre, infoemergencia.encargado FROM iglesia.adolescente JOIN iglesia.infoemergencia ON adolescente.id = infoemergencia.adolescente_id WHERE adolescente.id = '" + self.idViejo + "';")
        for (nombre,genero,fechanacimiento,tiposangre,encargado) in cur:
            self.nombre.insert(0,nombre)
            self.genero.insert(0,genero)
            self.calendario.set_date(fechanacimiento)
            self.tipoSangre.insert(0,tiposangre)
            self.contacto.insert(0,encargado)

    def borrarRegistro(self, where = ""):
        if len(self.nombre.get())!=0 and len(self.contacto.get())!=0 and len(self.tipoSangre.get())!=0:
            query="call BorrarAdolescente('" + self.mayus(self.nombre.get()) + "');"
            self.consultaBD(query)
            self.nombre.delete(0,END)
            self.genero.current(0)
            self.tipoSangre.delete(0,END)
            self.contacto.delete(0,END)
            self.listaTelefono.delete(0,END)
            self.listaAlergia.delete(0,END)
            self.nombre.focus()
            self.alergia.delete(0,END)
            self.telefono.delete(0,END)
            self.mostrarDatos()
        self.guardarAdolecente["state"]="normal"
        self.guardarTelefono["state"]="normal"
        self.guardarAlergia["state"]="normal"
        self.editar["state"]="disable"
        self.borrar["state"]="disable"
        
    def editarRegistro(self, where = ""):
        if len(self.nombre.get())!=0 and len(self.contacto.get())!=0 and len(self.tipoSangre.get())!=0:
            query="UPDATE iglesia.adolescente SET nombre='" + self.mayus(self.nombre.get()) + "', genero='" + self.mayus(self.genero.get()) + "', fechanacimiento='" + str(self.calendario.get_date()) + "' where id='" + self.idViejo + "';"
            self.consultaBD(query)
            query="UPDATE iglesia.infoemergencia SET tiposangre='" + self.mayus(self.tipoSangre.get()) + "', encargado='" + self.mayus(self.contacto.get()) +"' where adolescente_id='" + self.idViejo + "';"
            self.consultaBD(query)
            for telefono in self.listaTelefono.get(0,END):
                query="call InsertarTIEA('" + self.mayus(self.nombre.get()) + "', '" + telefono + "');"
                self.consultaBD(query)
            for alergia in self.listaAlergia.get(0,END):
                query="call InsertarAA('" + self.mayus(self.nombre.get()) + "', '" + self.mayus(alergia) + "');"
                self.consultaBD(query)
            self.nombre.delete(0,END)
            self.genero.current(0)
            self.tipoSangre.delete(0,END)
            self.contacto.delete(0,END)
            self.listaTelefono.delete(0,END)
            self.listaAlergia.delete(0,END)
            self.nombre.focus()
            self.alergia.delete(0,END)
            self.telefono.delete(0,END)
            self.mostrarDatos()
        self.guardarAdolecente["state"]="normal"
        self.guardarTelefono["state"]="normal"
        self.guardarAlergia["state"]="normal"
        self.editar["state"]="disable"
        self.borrar["state"]="disable"
    