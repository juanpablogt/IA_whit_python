class Persona():
    def __init__(self, name, edad):
        self.name = name 
        self.edad = edad
    
    def trabajar(self):
        print(self.name.title()+" esta Trabajando!")

    def descanzar(self):
        print(self.name.title()+" esta Descanzando")

persona1= Persona('Martb', 23)
persona1.trabajar()
persona1.descanzar()