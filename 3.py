class TiendaMascota():
    def __init__(self,nombre:str,edad:int,color:str):
        self._nombre:str = nombre
        self._edad:int = edad
        self._color:str = color

class Perros(TiendaMascota):
    def __init__(self, nombre, edad, color,peso:int,muerde:bool):
        super().__init__(nombre, edad, color)
        self._peso:int = peso
        self._muerde:bool = muerde
    #metodo estatico, los perros ladran
    @staticmethod
    def sonido():
        print("Los perros ladran")

class PerroGrande(Perros):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class PerroMediano(Perros):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class PerroPequeno(Perros):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)

class Caniche(PerroPequeno):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class YorkshireTerrier(PerroPequeno):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Schnauzer(PerroPequeno):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Chihuahua(PerroPequeno):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)

class Collie(PerroMediano):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Dalmata(PerroMediano):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Bulldog(PerroMediano):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Galgo(PerroMediano):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Sabueso(PerroMediano):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)

class PastorAleman(PerroGrande):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Doberman(PerroGrande):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Rotweiller(PerroGrande):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)

#/////////////////////////////////////////////////////////////////
class Gatos(TiendaMascota):
    def __init__(self, nombre, edad, color,alturaSalto:float,longitudSalto:float):
        super().__init__(nombre, edad, color)
        self._alturaSalto:float = alturaSalto
        self._longitudSalto:float = longitudSalto
    @staticmethod
    def sonido():
        print("Los gatos maullan y ronronean")

class GatoSinPelo(Gatos):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class GatoPeloLargo(Gatos):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class GatoPeloCorto(Gatos):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)

class Esfinge(GatoSinPelo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Elfo(GatoSinPelo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Donskoy(GatoSinPelo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)

class Angora(GatoPeloLargo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Himalayo(GatoPeloLargo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Balines(GatoPeloLargo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Somali(GatoPeloLargo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)

class AzulRuso(GatoPeloCorto):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Britanico(GatoPeloCorto):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Manx(GatoPeloCorto):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class DevonRex(GatoPeloCorto):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)

