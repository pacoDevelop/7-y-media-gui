import tkinter as tk
from random import randint
from tkinter import Label, Image, messagebox
from tkinter import Tk

from PIL import Image, ImageTk


# Clase carta que usaremos en la baraja
class Carta:
    palo = ["oro", "basto", "copa", "espada"]
    figura = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

    def __init__(self, numero=figura[randint(0, 11)], palo=palo[randint(0, 3)]):
        self.numero = numero
        self.palo = palo


# Clase baraja encargada de llevar el conjunto de cartas
class BarajaDeCartas:
    def __init__(self, baraja_size, app):
        self.baraja_size = baraja_size
        self.carta_actual = randint(0, baraja_size - 1)
        self.baraja = []
        self.inicializar()
        self.layout = app

    def inicializar(self):
        palo = ["oro", "basto", "copa", "espada"]
        figura = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        for h in palo:
            for i in figura:
                self.baraja.append(Carta(i, h))

    def barajar(self, root, carta):
        self.layout.puntos = 0
        if len(self.baraja) > 1:
            i = len(self.baraja) - 1
            while i > 0:
                h = randint(0, i)
                self.baraja[i], self.baraja[h] = self.baraja[h], self.baraja[i]
                i -= 1
            self.layout.mostrar_carta(root, carta)

    def repartir_carta(self, root):
        cartaActual = "images/" + str(self.baraja[self.carta_actual].palo) + "/" + str(
            self.baraja[self.carta_actual].numero) + ".jpg"
        self.layout.mostrar_carta(root, cartaActual)
        self.layout.juego()
        if self.carta_actual == 0:
            self.carta_actual = self.baraja_size - 1
        else:
            self.carta_actual = self.carta_actual - 1


# Interfaz grafica
class App:
    def __init__(self):
        self.b = BarajaDeCartas(40, self)
        self.puntos = 0
        self.puntuacion = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0.5, 0.5, 0.5]

    def interfaz(self):
        reverso = "images/BarajaReverso.png"
        root = Tk()
        label = tk.Label(root, text="JUEGO DE LAS SIETE Y MEDIA")
        label.grid()
        tk.Button(root, text="Barajar", command=lambda: self.b.barajar(root, reverso)).grid()
        tk.Button(root, text="Repartir", command=lambda: self.b.repartir_carta(root)).grid()
        for child in root.winfo_children(): child.grid_configure(padx=5, pady=25)
        root.mainloop()

    def juego(self):
        self.puntos = self.puntos + self.puntuacion[int(self.b.baraja[self.b.carta_actual].numero) - 1]
        if self.puntos > 7.5:
            messagebox.showinfo("RESULTADO", f"Pierdes has sacado {self.puntos}")
            self.puntos = 0
        else:
            if self.puntos == 7.5:
                messagebox.showinfo("RESULTADO", f"Ganas has sacado {self.puntos}")
                self.puntos = 0

    def mostrar_carta(self, root, carta):
        # usamos PIL (PILLOW)
        img = Image.open(str(carta))
        img = img.resize((200, 260), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        l_img = Label(root, image=img)
        l_img.image = img  # mantener referencia a la imagen
        # l_img.place(x=200-pos-10, y=40)
        l_img.grid(column=1, row=1)
        root.update()
