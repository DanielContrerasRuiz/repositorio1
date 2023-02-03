from tkinter import *

ventana = Tk()
ventana.title("Resolución ecuaciones de segundo grado")


#Variables que almacenarán los datos
aa = IntVar()
bb = IntVar()
cc = IntVar()

#generación de widgets
#peso
etiqueta_a = Label(ventana, text='Valor de a:')
entrada_a = Entry(ventana, textvariable=aa)
etiqueta_a.grid(row=1, column=1)
entrada_a.grid(row=1, column=2)
a = int(entrada_a.get())

etiqueta_b = Label(ventana, text='Valor de b:')
entrada_b = Entry(ventana, textvariable=bb)
etiqueta_b.grid(row=2, column=1)
entrada_b.grid(row=2, column=2)
b = int(entrada_b.get())

etiqueta_c = Label(ventana, text='Valor de c:')
entrada_c = Entry(ventana, textvariable=cc)
etiqueta_c.grid(row=3, column=1)
entrada_c.grid(row=3, column=2)
c = int(entrada_c.get())
ventana.mainloop()
print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

r1 = ((-b)+((b**2)-(4*a*c))**(1/2))/(a*2)
r2 = ((-b)-((b**2)-(4*a*c))**(1/2))/(a*2)
print(r1)
print(r2)


