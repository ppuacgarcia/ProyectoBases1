from tkinter import *
from PIL import Image, ImageTk

def menu(pw):
    
    def cmd1():
        print('registro adolescentes')
        
    def cmd2():
        print('registro colaboradores')

    def cmd3():
        print('Eventos')
        
    def cmd4():
        print('Informacion adolescentes')
        
    def cmd5():
        print('Infomracion colaboradores')
        
    def btnmenu(f1, x, y, text, bcolor, fcolor, command, font, siz, tipe):
        #Botones para menu
        def on_enter(e):
            buttons['background'] = bcolor
            buttons['foreground'] = fcolor
            
        def on_leave(e):
            buttons['background'] = fcolor
            buttons['foreground'] = bcolor
            
            
        buttons = Button(f1, width=35, height=2, text= text, fg  = bcolor, bg=fcolor, command=command, border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
        buttons.bind("<Enter>", on_enter)
        buttons.bind("<Leave>", on_leave)
        buttons.place(x=x, y=y)
        


    def VentanaMenu():
        f1 = Frame(pw,width=350,height=675,bg='#707070')
        f1.place(x=0, y=0)
        
        
        
        btnmenu(f1, 0, 100, 'registro adolescentes', '#000000', '#FFFFFF', cmd1,'Comic Sans', 12,'bold',)
        btnmenu(f1, 0, 155, 'registro colaboradores', '#000000', '#FFFFFF', cmd2,'Comic Sans', 12,'bold', )
        btnmenu(f1, 0, 210, 'Eventos', '#000000', '#FFFFFF', cmd3,'Comic Sans', 12,'bold',)
        btnmenu(f1, 0, 265, 'Informacion adolescentes', '#000000', '#FFFFFF', cmd4,'Comic Sans', 12,'bold',)
        btnmenu(f1, 0, 320, 'Informacion colaboradores', '#000000', '#FFFFFF', cmd5,'Comic Sans', 12,'bold',)
        
        def delete():
            f1.destroy()
            
        global img2
        img2 = ImageTk.PhotoImage(Image.open('Images/X.png'))
        
        #Boton cerrar menu
        Button(f1,image=img2, command=delete, border=0, activebackground='#707070',bg='#707070').place(x=5, y = 10)

    global img1
    img1 = ImageTk.PhotoImage(Image.open('Images/HM.png'))
    Button(pw, command = VentanaMenu, image=img1, border=0,activebackground='#000000', bg='#000000').place(x=5, y = 10)



