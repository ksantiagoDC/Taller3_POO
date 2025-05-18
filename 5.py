class Profesor():
    def _imprimir(self):
        print("Es un profesor")

class ProfesorTitular(Profesor):
    def _imprimir(self):
        print("Es un profesor titular")

class Prueba():
    if __name__ == "__main__":
        profesor1 = ProfesorTitular()
        profesor1._imprimir()
        profesor2 = profesor1  
        profesor2._imprimir()
# En python no hay casting.

