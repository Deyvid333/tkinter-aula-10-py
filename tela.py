import tkinter as tk

from tkinter import *
from tkinter import ttk

janela = Tk() 
janela.geometry("1920x1080")
titulo = janela.title("A mais")
caixa = ttk.Frame(janela, padding=160,  width=1920, height=1080, )
caixa.grid()
ttk.Label(caixa, text="Hello World!").grid(column=0, row=0)
ttk.Button(caixa, text="Quit", command=janela.destroy).grid(column=1, row=0)
janela.mainloop()