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
image = image.subsample(2, 2)  # Reduz o tamanho da imagem para metade


tk.Label(caixa, image=image, bg="#ffffff").grid(column=0, row=0, pady=(0, 45))
tk.Entry(caixa, width=35, bg="#EEEBEB", fg="#937D7D", relief="flat", bd=0, highlightthickness=15, highlightbackground="#EEEBEB", highlightcolor="#EEEBEB", font=("Roboto", 14, "bold")).grid(column=0, row=1, pady=(0, 15), ipady=0)
tk.Entry(caixa, width=35, bg="#EEEBEB", fg="#937D7D", relief="flat", bd=0, highlightthickness=15, highlightbackground="#EEEBEB", highlightcolor="#EEEBEB", font=("Roboto", 14, "bold")).grid(column=0, row=2, pady=(5, 15), ipady=0)

tk.Label(caixa, text="ACESSAR", width=38, bg="#298FC2", fg="#ffffff", relief="flat", bd=0, highlightthickness=0, cursor="hand2", font=("Roboto", 14, "bold")).grid(column=0, row=3, pady=(5, 30), ipady=14)

tk.Label(caixa, text="PRIMEIRO ACESSO", bg="#ffffff", fg="#298FC2", font=("Roboto", 14, "bold")).grid(column=0, row=4)

janela.mainloop()