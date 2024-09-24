import tkinter as tk
ventana = tk.Tk ()
ventana.title("Mi Primer Ventana")
ventana.geometry("600x400+450+200")
ventana.minsize(400,200)
ventana.maxsize(800,600)
ventana.iconbitmap("perro.ico")
ventana.configure(bg="lightgreen")
ventana.resizable(False,False) #Horizontal y Vertical
ventana.attributes("-alpha", 0.9)

ventana.mainloop()