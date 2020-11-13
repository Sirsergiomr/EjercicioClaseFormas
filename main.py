class  punto():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def muestra(self):
        print(self.x,self.y)
class forma():
    def __init__(self, Color, punto,Nombre):
        self.Color = Color
        self.punto = punto
        self.Nombre = Nombre
    def muestra(self):
        print(self.Color,self.Nombre)
        print(self.punto.muestra())
    def CambiaColor(self):
        try:
            x = int(input("Escribe el color >> "))
            self.Color =x
        except ValueError:
            print("Los colores van con numeros")
    def CambiaPunto(self):
        try:
            x = int(input("Escribe x >> "))
            y = int(input("Escribe y >> "))
            self.punto =  punto(x,y)
        except ValueError:
            print("Los puntos van con numeros")


class rectangulo(forma):
    def __init__(self,Color,punto,Nombre,lado_mayor,lado_menor):
        self.lado_menor = lado_menor
        self.lado_mayor = lado_mayor
        self.Color = Color
        self.punto = punto
        self.Nombre = Nombre

    def muestraLados(self):
        print("lados")
        print(self.lado_mayor, self.lado_menor)
    def area(self):
        a = self.lado_mayor * self.lado_menor
        print("Area:")
        print(a)
    def perimeter(self):
        p = (2* self.lado_menor)+(2*self.lado_mayor)
        print("Perimetro")
        print(p)
    def redimensionar(self, factor):

        a = self.lado_mayor * self.lado_menor
        ra =a * factor
        p = (2 * self.lado_menor*factor) + (2 * self.lado_mayor*factor)
        print("Area:")
        print(ra)
        print("Perimetro:")
        print(p)

class cuadrado(rectangulo):
    def __init__(self,Color,punto,Nombre,lado_mayor,lado_menor):
        self.lado_menor = lado_menor
        self.lado_mayor = lado_mayor
        self.Color = Color
        self.punto = punto
        self.Nombre = Nombre

class elipse(forma):
    def __init__(self,Color,punto,Nombre,R,r):
        self.Color = Color
        self.punto = punto
        self.Nombre = Nombre
        self.R = R
        self.r = r
    def areaElipse(self):
        a = 3.14*(self.R*self.r)
        print("Area:")
        print(a)

class circulo(elipse):
        def AreaCirculo(self):
            a = 3.14*(self.R)
            print("Area Circulo")
            print(a)




if __name__ == '__main__':
    opcion = 1
    while(opcion!=0):
        try:
            print("1-> Rectangulo  3-> Elipse")
            print("2-> Cuadrado    4-> Circulo    0 ->salir")
            opcion = int(input("Elige una opcion: "))
            if(opcion == 1):
                print("rectangulo elegido")
                print("Punto del rectangulo")
                x = int(input("Escribe x >> "))
                y = int(input("Escribe y >> "))
                p = punto(x, y)

                print("Color en numero")

                color = int(input(">> "))

                lm = int(input("lado mayor >> "))
                lmn = int(input("lado menor >>"))
                while(lm == lmn):
                    print("Recuerda, un lado tiene que ser menor sino no es un rectangulo")
                    lm = int(input("lado mayor >> "))
                    lmn = int(input("lado menor >>"))

                rec1 = rectangulo(color,p,"Rectangulo",lm,lmn)
                print("Objeto Rectangulo creado")
                print("contructor padre")
                rec1.muestra()
                print("contructor hijo")
                rec1.muestraLados()
                rec1.area()
                rec1.perimeter()
                print("Redimensionar")
                r = int(input(">> "))
                rec1.redimensionar(r)
            elif(opcion == 2):
                print("cuadrado elegido")
                print("Punto del cuadrado")
                x = int(input("Escribe x >> "))
                y = int(input("Escribe y >> "))
                p = punto(x, y)

                print("Color en numero")

                color = int(input(">> "))

                lm = int(input("lado mayor >> "))
                lmn = int(input("lado menor >>"))
                while (lm != lmn):
                    print("Recuerda, los lados tienen que se iguales")
                    lm = int(input("lado mayor >> "))
                    lmn = int(input("lado menor >>"))

                cuad = cuadrado(color, p, "Cuadrado", lm, lmn)
                print("Objeto Cuadrado creado")
                print("contructor padre")
                cuad.muestra()
                print("contructor hijo")
                cuad.muestraLados()
                cuad.area()
                cuad.perimeter()
                print("Redimensionar")
                r = int(input(">> "))
                cuad.redimensionar(r)
            elif(opcion == 3):
                print("Elipse elegida")
                print("Punto de la elipse")
                x = int(input("Escribe x >> "))
                y = int(input("Escribe y >> "))
                p = punto(x, y)

                print("Color en numero")

                color = int(input(">> "))

                R = int(input("Radio mayor >> "))
                r = int(input("radio menor >>"))
                while(R <= r | r >= R):
                    print("Recuerda, R es mayor que r")
                    R = int(input("Radio mayor >> "))
                    r = int(input("radio menor >>"))
                elip = elipse(color,p,"Elipse",R,r)
                print("Objeto elipse creado")
                elip.muestra()
                elip.areaElipse()
            elif(opcion == 4):
                print("Circulo elgido")

                print("Elipse elegida")
                print("Punto de la circunferencia")
                x = int(input("Escribe x >> "))
                y = int(input("Escribe y >> "))
                p = punto(x, y)

                print("Color en numero")

                color = int(input(">> "))

                R = int(input("Radio mayor >> "))

                cir = circulo(color,p,"Circulo",R,0)
                print("Objeto circulo creado")
                cir.muestra()
                cir.AreaCirculo()

        except ValueError:
            print("Los puntos van con numeros")