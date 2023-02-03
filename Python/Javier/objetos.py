class Usuario:
    def __init__(self, nombre, apellido):
        
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print('Hola, mi nombre es', self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print('Hola, me llamo', self.nombre, ' y soy administrador')


usuario = Usuario('Felipe', 'Fernandez')
# usuario2 = Usuario('Juan', 'Lopez')

usuario.saludo()
admin = Admin('Super', 'Super Feliz')
admin.saludo()
admin.superSaludo()
usuario.superSaludo() # error, la casle Usuario no tiene definido el método superSaludo


#print(usuario.nombre, usuario.apellido)
#del usuario.nombre
#print(usuario.nombre, usuario.apellido)
# usuario2.saludo()

# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)