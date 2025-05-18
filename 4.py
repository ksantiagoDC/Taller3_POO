class Persona():
    def __init__(self,nombre:str,direccion:str):
        self.nombre:str = nombre
        self.direccion:str = direccion
    def getNombre(self):
        print(f"{self.nombre}")
    def getDireccion(self):
        print(f"{self.direccion}")
    def setNombre(self,nombre:str):
        self.nombre = nombre
        return
    def setDireccion(self,direccion:str):
        self.direccion = direccion
        return
    
class Profesor(Persona):
    def __init__(self, nombre, direccion,departamento:str,categoria:str):
        super().__init__(nombre, direccion)
        self.departamento:str = departamento
        self.categoria:str = categoria
    def getDepartamento(self):
        print(f"{self.departamento}")
    def getCategoria(self):
        print(f"{self.categoria}")
    def setDepartamento(self,departamento:str):
        self.departamento = departamento
        return
    def setCategoria(self,categoria:str):
        self.categoria = categoria
        return
    
class Estudiante(Persona):
    def __init__(self, nombre, direccion,carrera:str,semestre:int):
        super().__init__(nombre, direccion)
        self.carrera:str = carrera
        self.semestre:int = semestre
    def getCarrera(self):
        print(f"{self.carrera}")
    def getSemestre(self):
        print(f"{self.semestre}")
    def setCarrera(self,carrera:str):
        self.carrera = carrera
        return
    def setSemestre(self,semestre:int):
        self.semestre = semestre
        return