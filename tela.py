import tkinter as tk

from tkinter import *
from tkinter import ttk

janela = Tk() 
janela.geometry("1920x1080")
janela.configure(bg="#ffffff")
titulo = janela.title("A + mais")

caixa = tk.Frame(janela, bg="#ffffff", padx=160, pady=160)
caixa.place(relx=0.5, rely=0.5, anchor="center")


image = tk.PhotoImage(file="assets/imagens/logo.png")
tk.Label(caixa, image=image).grid(column=0, row=0)
tk.Entry(caixa, width=30).grid(column=0, row=1, pady=10)

janela.mainloop()