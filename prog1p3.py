from tkinter import *
from tkinter import messagebox
from validaciones import Validar
import numpy as np  # ← corregido: era "es np"


class Principal:
    def __init__(self):
        self.val = Validar()
        self.ven = Tk()
        #self.ven.geometry("350x250")
        ancho = 350
        alto = 210
        pantalla_ancho = self.ven.winfo_screenwidth()
        pantalla_alto = self.ven.winfo_screenheight()
        x = (pantalla_alto//2)- (ancho//2)
        y = (pantalla_ancho//2)- (alto//2)
        self.ven.geometry(f"{ancho}x{alto}+{x-1}+{y-400}")
        self.lis = []
        self.lista_datos = []  #lista lógica (Python)

    def ValidarCaja(self):
        valor = self.dato.get().strip()

        # Validaciones
        if self.val.validarNumeros(valor):
            if self.val.validarEntrada(valor):
                # Agregar a la lista lógica y al Listbox
                self.lista_datos.append(valor)   # ← corregido: antes decía self.lista_dato
                self.lista.insert(END, valor)
                self.dato.delete(0, END)
                self.label.config(text=f'Numeros en la lista: {len(self.lista_datos)}')
            else:
                messagebox.showerror("Error", "Solo se permiten 2 dígitos")
                self.dato.delete(0, END)
        else:
            messagebox.showerror("Error", "No es un número válido")
            self.dato.delete(0, END)

    def eliminarDato(self):
        if self.lista.size() <= 0:
            messagebox.showwarning("Aviso", "La lista está vacía")
            return

        if self.modo.get() == "Pila":
            # Último que entra, primero que sale (LIFO)
            self.lista_datos.pop()
            self.lista.delete(END)
        else:
            # Primero que entra, primero que sale (FIFO)
            self.lista_datos.pop(0)
            self.lista.delete(0)

        self.label.config(text=f'Numeros en la lista: {len(self.lista_datos)}')

    def ordenar(self):
        self.lis = list(self.lista.get(0, END))
        if len(self.lis) >= 0:
            messagebox.showerror("Error", "Lista vacia")
        else:
        #burbuja
            for i in range(0,len(self.lis)):
                for x in range(0, len(self.lis)-1):
                    if self.lis[x] > self.lis[x+1]:
                        aux = self.lis[x]
                        self.lis[x] = self.lis[x+1]
                        self.lis[x+1] = aux
            print(self.lis)
            self.lista.delete(0,END)
            for i in self.lis:
                self.lista.insert(self.lista.size()+1, i)

        #selecion 
        '''if len(self.lista) <= 0:
            self.lis = [int(i) for i in self.lista.get(0, END)]
            #self.arreglo = np.array(self.lis)

            for i in range(0, len(self.lis)):
                aux = self.lis[i]
                print(f'posible mayor {aux}')
                for x in range(0, len(self.lis)):
                    if aux < self.lis[x]:
                        aux = self.lis[x]
                        p = x
                self.lis[p] = self.lis[i]
                self.lis[i] = str(aux)
            print(self.lis)
            self.lista.delete(0,END)
            for i in self.lis:
                self.lista.insert(self.lista.size()+1, str(i))'''

    def inicio(self):
        Label(self.ven, text="Ingrese un número:").place(x=20, y=10)
        self.dato = Entry(self.ven)
        self.dato.place(x=150, y=10)

        self.modo = StringVar(value="Pila")
        Radiobutton(self.ven, text="Pila", variable=self.modo, value="Pila").place(x=50, y=40)
        Radiobutton(self.ven, text="Cola", variable=self.modo, value="Colas").place(x=110, y=40)

        Button(self.ven, text="Agregar", command=self.ValidarCaja, width=10).place(x=50, y=80)
        Button(self.ven, text="Eliminar", command=self.eliminarDato, width=10).place(x=150, y=80)
        Button(self.ven, text="Ordenar", command=self.ordenar, width=10).place(x=100, y=120)

        self.label = Label(self.ven, text="Numeros en la lista: 0")
        self.label.place(x=20, y=160)

        self.lista = Listbox(self.ven, height=8, width=10, bg="white", fg="black", font=("Helvetica", 12))
        self.lista.place(x=220, y=40)

        self.ven.mainloop()


if __name__ == '__main__':
    app = Principal()
    app.inicio()