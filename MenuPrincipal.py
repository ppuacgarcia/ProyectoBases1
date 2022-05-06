from tkinter import *
from PIL import Image, ImageTk

from InfoColaboradores import colabinfo
from Colabform import ColForm
from InfoAdol import adolinfo
from Adolescentes import *
from Eventos import EvtForm



def MenP(pw):

    fMenuP = Frame(pw,width=1200,height=675,bg='#707070')
    fMenuP.place(x=0, y=0)

    def cmd1():
        AdolForm(pw).mostrarDatos()
        
    def cmd2():
        ColForm(pw)

    def cmd3():
        EvtForm(pw).mostrarDatos()
        
    def cmd4():
        adolinfo(pw).mostrarDatos()
        
    def cmd5():
        colabinfo(pw).mostrarDatos()
        
    def btnmenu(pw, x, y, text, bcolor, fcolor, command, font, siz, tipe):
        #Botones para menu
        def on_enter(e):
            buttons['background'] = bcolor
            buttons['foreground'] = fcolor
            
        def on_leave(e):
            buttons['background'] = fcolor
            buttons['foreground'] = bcolor
            
            
        buttons = Button(pw, width=30, height=2, text= text, fg  = bcolor, bg=fcolor, command=command, border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
        buttons.bind("<Enter>", on_enter)
        buttons.bind("<Leave>", on_leave)
        buttons.place(x=x, y=y)
        
    Label(fMenuP, text='Menú',bg='#707070',fg='#FFFFFF', font=('Arial', 42,'bold') ).place(x=525,y=10)
    btnmenu(fMenuP, 400, 150, 'registro adolescentes', '#FF4e10', '#FFFFFF', cmd1,'Arial', 16,'bold',)
    btnmenu(fMenuP, 400, 250, 'registro colaboradores', '#FF4e10', '#FFFFFF', cmd2,'Arial', 16,'bold', )
    btnmenu(fMenuP, 400, 350, 'Eventos', '#FF4e10', '#FFFFFF', cmd3,'Arial', 16,'bold',)
    btnmenu(fMenuP, 400, 450, 'Informacion adolescentes', '#FF4e10', '#FFFFFF', cmd4,'Arial', 16,'bold',)
    btnmenu(fMenuP, 400, 550, 'Informacion colaboradores', '#FF4e10', '#FFFFFF', cmd5,'Arial', 16,'bold',)
