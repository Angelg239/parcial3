
'''Hacer un programa que lea nombre apellido paterno y materno en 3 cajas separadas a demas leer dia mes y año de 
nacimiento en 3 cajas separadas.
el precioner un boton se agregara al lisbox el rfc de a presona, 
ademas contendra 2 botones para eliminar 
elemenentos del limbos mediante filas y colas'''

from tkinter import *
from tkinter import messagebox
from validar2p3 import validar2
import numpy as np

class Principal:
    def __init__(self):
        self.val = validar2()
        self.ven = Tk()
        ancho = 350
        alto = 210
        pantalla_ancho = self.ven.winfo_screenwidth()
        pantalla_alto = self.ven.winfo_screenheight()
        x = (pantalla_alto//2)- (ancho//2)
        y = (pantalla_ancho//2)- (alto//2)
        self.ven.geometry(f"{ancho}x{alto}+{x-1}+{y-400}")
        self.lis = []
        self.lista_datos = []
        self.ven.mainloop()

    def inicio(self):
        l1 = Label(self.ven, text="Escribe un nombre").place(y=10, x=20)
        l2 = Label(self.ven, text="Apellido paterno").place(y=50, x=20)

        self.n1 = Entry(self.ven)
        self.n1.place(y=10, x=130)
        self.n2 = Entry(self.ven)
        self.n2.place(y=50, x=130)

        l3 = Label(self.ven, text="Apellido materno").place(y=90, x=20)
        self.n3 = Entry(self.ven)
        self.n3.place(y=90, x=130)
        
if __name__=='__main__':
    app = Principal()
    app.inicio()