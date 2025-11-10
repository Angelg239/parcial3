# ==============================
#   PROGRAMA: PILAS Y COLAS CON ORDENAMIENTO
#   Autor: (Tu nombre si deseas)
#   Descripción: Programa con interfaz gráfica (Tkinter)
#   que permite ingresar números, validarlos, eliminarlos
#   (como pila o cola) y ordenarlos con métodos burbuja o selección.
# ==============================

from tkinter import *            # Tkinter: para crear la interfaz gráfica
from tkinter import messagebox   # messagebox: para mostrar mensajes emergentes
from validar2p3 import validar2     # Importa la clase Validar desde el archivo validar2.py
import numpy as np               # Librería para operaciones numéricas (no se usa mucho aquí, pero puede servir)

# ==============================
#   CLASE PRINCIPAL DE LA APLICACIÓN
# ==============================
class Principal:
    def __init__(self):
        self.val = validar2 ()           # Instancia de la clase Validar (control de entrada de datos)
        self.ven = Tk()                # Crea la ventana principal

        # Tamaño de la ventana
        ancho = 310
        alto = 210

        # Calcula la posición centrada en pantalla
        ventana_ancho = self.ven.winfo_screenwidth()
        ventana_alto = self.ven.winfo_screenheight()
        x = (ventana_ancho // 2) - (ancho // 2)
        y = (ventana_alto // 2) - (alto // 2)

        # Configuración de tamaño y posición
        self.ven.geometry(f"{ancho}x{alto}+{x-200}+{y-150}")
        self.ven.title("Pilas y Colas")   # Título de la ventana
        
        # Listas para almacenar los datos
        self.lis = []            # Lista auxiliar
        self.lista_datos = []    # Lista lógica (Python), contiene los datos ingresados

    # ==============================
    #   FUNCIÓN PARA VALIDAR Y AGREGAR DATOS
    # ==============================
    def ValidarCaja(self):
        valor = self.dato.get().strip()   # Obtiene el texto ingresado y elimina espacios

        # Si el valor es un número válido
        if self.val.ValidarNumeros(valor):
            # Verifica si tiene máximo 2 dígitos (según ValidarEntrada)
            if self.val.ValidarEntrada(valor):
                self.lista_datos.append(valor)            # Lo agrega a la lista lógica
                self.lista.insert(END, valor)             # Lo agrega al Listbox (interfaz)
                self.dato.delete(0, END)                  # Limpia la caja
                # Actualiza el contador de elementos
                self.label.config(text=f'Numeros en la lista: {len(self.lista_datos)}')
            else:
                messagebox.showerror("Error", "Solo se permiten 2 dígitos")
                self.dato.delete(0, END)
        else:
            messagebox.showerror("Error", "No es un número válido")
            self.dato.delete(0, END)

    # ==============================
    #   FUNCIÓN PARA ELIMINAR DATOS (PILA O COLA)
    # ==============================
    def eliminarDato(self):
        # Si la lista está vacía
        if self.lista.size() <= 0:
            messagebox.showwarning("Aviso", "La lista está vacía")
            return

        # Si el modo es "Pila" → elimina el último elemento (LIFO)
        if self.modo.get() == "Pila":
            self.lista_datos.pop()
            self.lista.delete(END)
        # Si el modo es "Cola" → elimina el primer elemento (FIFO)
        else:
            self.lista_datos.pop(0)
            self.lista.delete(0)

        # Actualiza el texto del contador
        self.label.config(text=f'Numeros en la lista: {len(self.lista_datos)}')

    # ==============================
    #   ORDENAMIENTO BURBUJA
    # ==============================
    def ordenar_burbuja(self):
        # Obtiene todos los elementos actuales del Listbox
        self.lis = list(self.lista.get(0, END))

        if len(self.lis) <= 0:
            messagebox.showerror('Error', 'Lista vacía')
        else:
            print("\n--- ORDENAMIENTO BURBUJA ---")
            print("Lista original:", self.lis)

            # Convierte a enteros
            self.lis = [int(i) for i in self.lis]

            # Algoritmo de burbuja
            for i in range(0, len(self.lis)):
                for x in range(0, len(self.lis) - 1):
                    if self.lis[x] > self.lis[x + 1]:
                        aux = self.lis[x]
                        self.lis[x] = self.lis[x + 1]
                        self.lis[x + 1] = aux
                        print(f"Intercambio: {self.lis}")

            print("Lista ordenada (burbuja):", self.lis)

            # Limpia el Listbox y muestra la lista ordenada
            self.lista.delete(0, END)
            for i in self.lis:
                self.lista.insert(self.lista.size() + 1, str(i))

    # ==============================
    #   ORDENAMIENTO POR SELECCIÓN
    # ==============================
    def ordenar_seleccion(self):
        self.lis = list(self.lista.get(0, END))

        if len(self.lis) <= 0:
            messagebox.showerror('Error', 'Lista vacía')
        else:
            print("\n--- ORDENAMIENTO POR SELECCIÓN ---")
            print("Lista original:", self.lis)

            self.lis = [int(i) for i in self.lis]

            # Algoritmo de selección
            for i in range(len(self.lis)):
                minimo = i
                for j in range(i + 1, len(self.lis)):
                    if self.lis[j] < self.lis[minimo]:
                        minimo = j
                # Intercambio de valores
                if minimo != i:
                    self.lis[i], self.lis[minimo] = self.lis[minimo], self.lis[i]
                    print(f"Intercambio: {self.lis}")

            print("Lista ordenada (selección):", self.lis)

            self.lista.delete(0, END)
            for i in self.lis:
                self.lista.insert(self.lista.size() + 1, str(i))

    # ==============================
    #   INTERFAZ GRÁFICA
    # ==============================
    def Inicio(self):
        # Etiqueta y caja de texto
        Label(self.ven, text="Ingrese un número:").place(x=20, y=10)
        self.dato = Entry(self.ven)
        self.dato.place(x=150, y=10)

        # RadioButtons: seleccionar modo de eliminación (Pila o Cola)
        self.modo = StringVar(value="Pila")
        Radiobutton(self.ven, text="Pila", variable=self.modo, value="Pila").place(x=50, y=40)
        Radiobutton(self.ven, text="Cola", variable=self.modo, value="Cola").place(x=110, y=40)

        # Botones principales
        Button(self.ven, text="Agregar", command=self.ValidarCaja, width=10).place(x=50, y=80)
        Button(self.ven, text="Eliminar", command=self.eliminarDato, width=10).place(x=150, y=80)

        # Botones de ordenamiento
        Button(self.ven, text="Burbuja", command=self.ordenar_burbuja, width=8).place(x=30, y=120)
        Button(self.ven, text="Selección", command=self.ordenar_seleccion, width=8).place(x=170, y=120)

        # Etiqueta que muestra el número de elementos
        self.label = Label(self.ven, text="Numeros en la lista: 0")
        self.label.place(x=20, y=160)

        # Listbox para mostrar los datos ingresados
        self.lista = Listbox(self.ven, height=8, width=10, bg="white", fg="black", font=("Helvetica", 12))
        self.lista.place(x=220, y=40)

        # Inicia el bucle principal
        self.ven.mainloop()

# ==============================
#   PUNTO DE ENTRADA
# ==============================
if __name__ == '__main__':
    app = Principal()
    app.Inicio()
