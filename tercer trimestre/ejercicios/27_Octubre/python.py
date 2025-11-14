class Figura:
    def area(self):
        pass

class cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado

class triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2

while True:
    print("1) cuadrado")
    print("2) triangulo")
    print("3) salir")
    opcion = input("elige una opcion: ")


    if op == "1":
        lado = float(input("ingresa el lado: "))
        c = cuadrado(lado)
        print(f"el area del cuadrado es {c.area()}")
    elif op == "2":
        base = float(input("ingresa la base: "))
        altura = float(input("ingresa la altura: "))
        t = triangulo(base, altura)
        print(f"el area del triangulo es {t.area()}")
    elif op == "3":
        break
    else:
        print("opcion no valida")