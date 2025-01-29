import tkinter as tk
from tkinter import messagebox

#construir mi ventana

ventana = tk.Tk()
ventana.title('Sistema de resgistro de clientes')
ventana.geometry('300x200')
#crear variables
cedula = tk.StringVar()
nombre = tk.StringVar()
apellido = tk.StringVar()
telefono = tk.StringVar()
direccion = tk.StringVar()

#crear etiquetas

etiqueta_cedula = tk.Label(ventana, text='Cédula:')
etiqueta_nombre = tk.Label(ventana, text='Nombre:')
etiqueta_apellido = tk.Label(ventana, text='Apellido:')
etiqueta_telefono = tk.Label(ventana, text='Teléfono:')
etiqueta_direccion = tk.Label(ventana, text='Dirección:')

#crear entradas

entrada_cedula = tk.Entry(ventana, textvariable=cedula)
entrada_nombre = tk.Entry(ventana, textvariable=nombre)
entrada_apellido = tk.Entry(ventana, textvariable=apellido)
entrada_telefono = tk.Entry(ventana, textvariable=telefono)
entrada_direccion = tk.Entry(ventana, textvariable=direccion)

#crear botones

boton_guardar = tk.Button(ventana, text='Guardar', command=guardar_datos)
boton_borrar = tk.Button(ventana, text='Borrar', command=borrar_datos)

#posicionar etiquetas

etiqueta_cedula.grid(row=0, column=0)
etiqueta_nombre.grid(row=1, column=0)
etiqueta_apellido.grid(row=2, column=0)
etiqueta_telefono.grid(row=3, column=0)
etiqueta_direccion.grid(row=4, column=0)

#posicionar entradas

entrada_cedula.grid(row=0, column=1)
entrada_nombre.grid(row=1, column=1)
entrada_apellido.grid(row=2, column=1)
entrada_telefono.grid(row=3, column=1)
entrada_direccion.grid(row=4, column=1)

#posicionar botones

boton_guardar.grid(row=5, column=0, columnspan=2)
boton_borrar.grid(row=6, column=0, columnspan=2)

#funcion para guardar datos

def guardar_datos():
    #validar datos
    if cedula.get() == '' or nombre.get() == '' or apellido.get() == '' or telefono.get() == '' or direccion.get() == '':
        messagebox.showerror('Error', 'Todos los campos son obligatorios')
        return
    
    #guardar datos en un archivo
    try:
        with open('clientes.txt', 'a') as archivo:
            archivo.write(f'{cedula.get()}|{nombre.get()}|{apellido.get()}|{telefono.get()}|{direccion.get()}\n')
        messagebox.showinfo('Correcto', 'Datos guardados correctamente')
    except Exception as e:
        messagebox.showerror('Error', f'Error al guardar los datos: {str(e)}')

#funcion para borrar datos

def borrar_datos():
    cedula.set('')
    nombre.set('')
    apellido.set('')
    telefono.set('')
    direccion.set('')
    messagebox.showinfo('Correcto', 'Datos borrados correctamente')
    
#limpiar entrada de cedula
    entrada_cedula.delete(0, tk.END)
    #mostrar mensaje de borrado en pantalla
    messagebox.showinfo('Correcto', 'Datos borrados correctamente')
    #limpiar entrada de nombre
    entrada_nombre.delete(0, tk.END)
    #mostrar mensaje de borrado en pantalla
    messagebox.showinfo('Correcto', 'Datos borrados correctamente')
    #limpiar entrada de apellido
    entrada_apellido.delete(0, tk.END)
    #mostrar mensaje de borrado en pantalla
    messagebox.showinfo('Correcto', 'Datos borrados correctamente')
    #limpiar entrada de telefono
    entrada_telefono.delete(0, tk.END)
    #mostrar mensaje de borrado en pantalla
    messagebox.showinfo('Correcto', 'Datos borrados correctamente')
    #limpiar entrada de direccion
    entrada_direccion.delete(0, tk.END)
    #mostrar mensaje de borrado en pantalla
    messagebox.showinfo('Correcto', 'Datos borrados correctamente')
  
ventana.mainloop()