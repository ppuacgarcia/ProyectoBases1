import tkinter as tk
from turtle import bgcolor, width
from tkinter import *
from PIL import Image, ImageTk
class Frame(tk.Frame):
    
    def __init__(self, root=None):
        
        super().__init__(root,width=1200, height=675)
        
        self.root=root
        self.pack()
        self.Login()
    def Login(self):
        fonttxt = 'Arial'
        posx=430
        posy=100
        colorbg="#ABB2B9"
        #Labels
        #imagenes
        global logoH
        lgimg=Image.open('Images/Teen.ICO')
        lgimg.resize((100,100),Image.ANTIALIAS)
        logoH = ImageTk.PhotoImage(lgimg)
        self.bglabel=tk.Label(self,image=logoH, border=0,bg=colorbg).place(x=posx, y = posy)
        #labels
        #user label
        self.UserLabel=tk.Label(self,text='Usuario')
        self.UserLabel.place(x=posx,y=posy+260)
        self.UserLabel.config(bg=colorbg,font=(fonttxt,15,'bold'))
        #password label
        self.PasswordLabel=tk.Label(self,text='Clave')      
        self.PasswordLabel.place(x=posx,y=posy+315)
        self.PasswordLabel.config(bg=colorbg,font=(fonttxt,15,'bold'))
        #login label
        self.LoginLablel=tk.Label(self,text='Inicio')
        self.LoginLablel.place(x=posx+80,y=0)
        self.LoginLablel.config(bg=colorbg,font=(fonttxt,40,'bold'))
       
        #entradas

        #username enrty
        self.Username=tk.StringVar()
        self.EnrtyUsername=tk.Entry(self)
        self.EnrtyUsername.config(width=30,font=(fonttxt,12),textvariable=self.Username
        )
        self.EnrtyUsername.place(x=posx,y=posy+290)
        #password entry
        self.Password=tk.StringVar()
        self.EntryPassword=tk.Entry(self)
        self.EntryPassword.config(width=30,font=(fonttxt,12),textvariable=self.Password,show='■')
        self.EntryPassword.place(x=posx,y=posy+340)
        #button
        self.Enter=tk.Button(self,text="Entrar")
        self.Enter.config(font=(fonttxt,13,'bold'),width=10,command=self.Correcto)
        self.Enter.place(x=posx,y=posy+370)
    def Correcto(self):
        if(self.Username.get()=="admin" and self.Password.get()=="1234"):
            
            print("entro")
        else:
            
            print("no entro")

        
def  main():
    
    root=tk.Tk()
    root.resizable(0,0) 
    root.title('Inicio de sesion')
    root.geometry('1200x675')
    root.iconbitmap('Images/TEEN.ICO')
    app= Frame(root=root)
    app.config(bg='#ABB2B9')
    app.mainloop()

if __name__=='__main__':
    main()