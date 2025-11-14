"""
# definicion de una clase

class estudiantes:
    def __init__ (self, nombre, edad, programa_formacion):
        self.nombre = nombre
        self.edad = edad
        self.programa_formacion = programa_formacion
    def mostrar_informacion(self):
        print(f"nombre:{self.nombre}")
        print(f"edad:{self.edad}")
        print(f"programa de formacion:{self.programa_formacion}")



est1 = estudiantes("laura gomez", 20, "programacion de software")
est2 = estudiantes("clara perez", 24, "programacion de software")

# mostrar informacion

est1.mostrar_informacion()
est2.mostrar_informacion()
"""








# clase
class Empleados:
    def __init__ (self, nombre_completo, edad, identificacion, area):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.identificacion = identificacion
        self.area = area
    def mostrar_empleados(self):
        print("- - - - - - - - - - -")
        print(f"nombres y apellidos: {self.nombre_completo}")
        print(f"edad: {self.edad}")
        print(f"identificacion: {self.identificacion}")
        print(f"area: {self.area}")

# crear objeto
emp1 = Empleados("luis David Riveros Orozco", 16, 1114244100, "programacion")
emp2 = Empleados("Lauren Michell Gutierrez Chapid", 16, 1086419727, "diseño grafico")

# mostrar
emp1.mostrar_empleados()
emp2.mostrar_empleados()
