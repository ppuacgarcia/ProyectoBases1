from optparse import Values
from tkinter import *
from PIL import Image, ImageTk
from Menu import *
from tkinter import ttk
from tkcalendar import *
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
        self.lab('Informacion de Enmergencia', self.fuenteG, self.bglabel, self.fglabel, self.posx, 240)
        self.lab('Contacto', self.fuenteP, self.bglabel, self.fglabel, self.posx, 290)
        self.lab('Telefono', self.fuenteP, self.bglabel, self.fglabel, self.posx, 325)
        self.lab('Tipo de Sangre', self.fuenteP, self.bglabel, self.fglabel, self.posx, 360)
        self.lab('Alergias', self.fuenteP, self.bglabel, self.fglabel, self.posx, 395)

        #Cuadros de texto
        self.nombre=self.Ent(self.w,155,175,105)
        #self.genero=self.Ent(self.w,155,175,175)
        self.contacto=self.Ent(self.w,155, 175, 300)
        self.telefono=self.Ent(self.w,25, 175, 335)
        self.tipoSangre=self.Ent(self.w,144, 240, 370)
        self.alergia=self.Ent(self.w,25, 175, 405)

        #ComboBox
        self.genero=ttk.Combobox(self.w,width=155)
        self.genero['values']=('Masculino','Femenino')
        self.genero.current(0)
        self.genero["state"]="readonly"
        self.genero.pack()
        self.genero.place(x=175,y=175)

        #Calendario
        self.calendario=DateEntry(self.w,width=30)
        self.calendario.place(x=295,y=140)

        #Botones
        self.guardarAdolecente=self.btn(self.w, 980, 600, 'Guardar', '#000000', '#FF4e10', self.agregarRegistro,'Arial', 12,'bold',18,2)
        self.guardarTelefono=self.btn(self.w,self.posx+375,335,'Guardar Telefono','#000000','#FF4e10',self.agregarTelefono,'Arial',12,'bold',13,1)
        self.guardarAlergia=self.btn(self.w,self.posx+375,405,'Guardar Alergia','#000000','#FF4e10',self.agregarAlergia,'Arial',12,'bold',13,1)

        #Listas
        self.listaTelefono=self.tb(self.w,707,335)
        self.listaAlergia=self.tb(self.w,707,405)

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

    #Metodos para ingresar a la base de datos
    def consultaBD(self,query):
        try:
            conn=mariadb.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="baseIglesia",
                autocommit=True
            )
        except mariadb.Error as e:
            print("Error al conectarse a la bd",e)
        cur = conn.cursor()
        #cur.execute(query)
        id2=cur.execute(query)
        print("PRIMERO   "+str(id2))
        return cur


    def agregarRegistro(self):
        if len(self.nombre.get())!=0 and len(self.contacto.get())!=0 and len(self.tipoSangre.get())!=0:
            query="INSERT INTO baseIglesia.adolescente (nombre,genero,fechaNacimiento) VALUES ('" + self.nombre.get() + "', '" + self.genero.get() + "','" + str(self.calendario.get_date()) + "');"
            self.consultaBD(query)
            query="SELECT idAdolescente FROM adolescente where nombre='"+self.nombre.get()+"';"
            print("holaaaaaaaaaaaa")
            id = str(self.consultaBD(query))
            records = self.consultaBD(query).fetchall()
            print("\nPrinting each row")
            for row in records:
                print("Id = ", row[0], )
                
            print("SEGUNDO"+id)
            '''query="INSERT INTO baseIglesia.informacionenmergenica (tipoSangre,encargado,Adolescente_idAdolescente) VALUES ('" + self.tipoSangre.get() + "', '" + self.contacto.get() + "','" + id + "');"
            consultaBD(query)
            query="SELECT idInformacion FROM baseIglesia.informacionenmergenica WHERE Adolescente_idAdolescente='" + id + "'"
            id=consultaBD(query)
            for telefono in self.listaTelefono.get(0,END):
                query="INSERT INTO baseIglesia.telefono (telefono,informacionEnmergencia_idContacto) VALUES ('" + telefono + "', '" + id + "');"
                consultaBD(query)
            for alergia in self.listaAlergia.get(0,END):
                query="INSERT INTO baseIglesia.alergia (nombre,informacionEnmergencia_idContacto) VALUES ('" + alergia + "', '" + id + "');"
                consultaBD(query)'''
            self.nombre.delete(0,END)
            self.nombre.focus()
        else:
            self.mensaje['text']="El nombre y clave no pueden estar vacias"