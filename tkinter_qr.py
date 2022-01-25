#author: luis javier rubio martinez
#version 1.0

import tkinter as tk
from tkinter import Checkbutton, Label, PhotoImage, filedialog
from tkinter import ttk
import qrcode
import os



ventana = tk.Tk()
ventana.geometry('700x600')
ventana.title('Generador wifi Qr')
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=3)


#funciones
def enviar():
    qr= qrcode.make(f"WIFI:S:{SSID.get()};T:WPA;P:{var_pass.get()};;")
    f = open("wifi_Qr.png","wb")
    qr.save(f)
    f.close()
    imagen()

def imagen():
    imagen = PhotoImage(file="wifi_Qr.png")
    imagenqr = Label(ventana,image=imagen).place(x=150,y=150)
    texto = Label(ventana,text='Escanea el codigo Qr').place(x=250,y=120)
    ventana.mainloop()
    
def guardar():
    boton_guardar.config(text='guardado') 
    fichero = filedialog.asksaveasfilename(title="guardar",filetypes=[("PNG",".png")])
    os.rename('wifi_Qr.png',fichero)

# variables de entrada
var_SSID = tk.StringVar()
var_pass= tk.StringVar()
# datos de red
SSID = ttk.Entry(ventana,textvariable=var_SSID,justify=tk.CENTER)
SSID.grid(row=0,column=1,sticky=tk.W,pady=5,padx=5)
#etiquetas
etiqueta_SSID = tk.Label(ventana,text='Nombre de la red: ')
etiqueta_SSID.grid(row=0,column=0,sticky=tk.E,pady=5,padx=5)

# datos contraseña
entrada_pass = ttk.Entry(ventana,textvariable=var_pass,show='*')
entrada_pass.grid(row=1,column=1,sticky=tk.W,pady=5,padx=5)

#etiqueta
etiqueta_pass = tk.Label(ventana,text='Contraseña: ')
etiqueta_pass.grid(row=1,column=0,sticky=tk.E,pady=5,padx=5)

#boton generar
boton = ttk.Button(ventana,text='Generar',command=enviar)
boton.grid(row=3,column=1,sticky=tk.W,pady=5,padx=5)

#boton guardar
boton_guardar = ttk.Button(ventana,text='Guardar',command=guardar)
boton_guardar.grid(row=3,column=1,pady=5,padx=5)


ventana.mainloop()