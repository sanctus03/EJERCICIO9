class rueda:

    def __init__(self):
        self.ancho=input("Ingrese el ancho de la rueda:")
        self.rodadura=input("Ingrese la rodadura de la rueda:")
        self.diametro=input("ingrese el diametro de la rueda:")
        self.presion= 0
    def set_pressure(self):
        self.presion= input("ingrese la presión de la rueda:")

    def print_info(self):
        print(self.ancho,"/",self.rodadura,"R",self.diametro)
    def print_pressure(self):
        self.pressure= self.presion
        print(self.pressure, "bares")

# bloque principal

rueda1= rueda()
rueda1.set_pressure()
rueda1.print_info()
rueda1.print_pressure()

