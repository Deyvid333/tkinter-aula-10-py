import tkinter as tk

from tkinter import *
from tkinter import ttk

janela = Tk()
caixa = ttk.Frame(janela, padding=100)
caixa.grid()
ttk.Label(caixa, text="Hello World!").grid(column=0, row=0)
ttk.Button(caixa, text="Quit", command=janela.destroy).grid(column=1, row=0)
janela.mainloop()