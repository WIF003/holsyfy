from tkinter import*
import tkinter as tk
from tkinter import ttk
ventana=Tk()
ventana.geometry("60x60+15+5")
ventana.config(bg="whitesmoke")
ventana.title("ventana con imagen")
mi_Frame=Frame()
mi_Frame.pack()
mi_texto1=Label(mi_Frame,text="AUTOLAVADO")
mi_texto1.pack()
mi_texto1.config(bg="white")
mi_texto1.config(font=('Arial',10))
mi_texto1.config(fg="blue")

mi_Frame=Frame()
mi_Frame.pack()
mi_texto2=Label(mi_Frame,text="20 Lib. Instituto Politécnico Nacional")
mi_texto2.pack()
mi_texto2.config(bg="white")
mi_texto2.config(font=('Arial',10))
mi_texto2.config(fg="purple")
my_ima=PhotoImage(file="descarga (1).png")
Etiqueta=Label(ventana,image=my_ima).place(x=250,y=100)

def abrirVentana2():
  #ventana.withdraw()#cierra la ventana principal
 ventana2=tk.Toplevel()#crea una nueva ventana
 ventana2.geometry("380x300+150+50")
 ventana2.config(bg="dark turquoise")
 ventana2.title("Boton")
#programar el boton
boton=tk.Button(ventana,text="Nueva Ventana",fg="blue",command=abrirVentana2)
boton.place(x=254,y=400)

lista_desplegable= ttk.Combobox (ventana,width=17)
lista_desplegable.place(x=200,y=600)

opciones= ["Auto","Camioneta","Moto"]
lista_desplegable['values']=opciones

Button(ventana,text="obtener",bg='orange',command='obtener_info').place(x=250,y=700)




ventana.mainloop()