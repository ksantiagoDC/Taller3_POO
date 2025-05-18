class Inmueble:
    
    def __init__(self,id_inmobiliario:int,direccion:str,area:int):
        self._id_inmobiliario = id_inmobiliario
        self._direccion = direccion
        self._area = area
        self._precioVenta:float

    def calcularPrecioVenta(self, valorArea:float):
        self._precioVenta = self._area * valorArea
        print(self._precioVenta)

    def imprimir(self):
        print(f"Dirección: {self._direccion}")
        print(f"Metros cuadrados: {self._area}")
        print(f"Identificación Inmobiliaria: {self._id_inmobiliario}")
        print(f"Precio de venta: {self._precioVenta}")

class InmuebleVivienda(Inmueble):
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones:int, num_banos:int):
        super().__init__(id_inmobiliario, direccion, area)
        self._num_habitaciones = num_habitaciones
        self._num_banos = num_banos

    def imprimir(self):
        print(f"Numero de habitaciones: {self._num_habitaciones}")
        print(f"Numero de baños: {self._num_banos}")
        super().imprimir()

#///////////////////////////////////////////////////////////

class Casa(InmuebleVivienda):
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos:int):
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos)
        self._pisos = pisos

    def imprimir(self):
        print(f"Pisos: {self._pisos}")
        super().imprimir()


class CasaRural(Casa):
    _valorArea:float = 1500000 
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos, distancia_cabecera:int, altitud:int):
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos)
        self._distancia_cabecera = distancia_cabecera
        self._altitud = altitud

    def imprimir(self):
        print(f"Distancia cabecera: {self._distancia_cabecera}")
        print(f"Altitud: {self._altitud}")
        super().imprimir()


class CasaUrbana(Casa):
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos):
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos)
    
    def imprimir(self):
        super().imprimir()

class CasaConjuntoCerrado(CasaUrbana):
    _valorArea = 2500000
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos,valorAdmin:int,tienePiscina:bool,tieneCamposDeportivos:bool):
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos)
        self._valorAdmin = valorAdmin
        self._tienePiscina = tienePiscina
        self._tieneCamposDeportivos = tieneCamposDeportivos

    def imprimir(self):
        print(f"Valor de administración: {self._valorAdmin}")
        print(f"Tiene piscina: {self._tienePiscina}")
        print(f"Tiene campos deportivos: {self._tieneCamposDeportivos}")
        super().imprimir()
    
class CasaIndependiente(CasaUrbana):
    _valorArea:float = 3000000
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos):
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos)

    def imprimir(self):
        super().imprimir()

#///////////////////////////////////////////////////////////

class Apartamento(InmuebleVivienda):
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos):
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos)

    def imprimir(self):
        super().imprimir()


class Apartaestudio(Apartamento):
    _valorArea:float = 1500000
    def __init__(self, id_inmobiliario, direccion, area):
        super().__init__(id_inmobiliario, direccion, area, 1, 1, ) #num_habitaciones y num_banos no es configurable asi

    def imprimir(self):
        super().imprimir()




class ApartamentoFamiliar(Apartamento):
    _valorArea:float = 1500000
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos,valorAdmin):
        self._valorAdmin = valorAdmin
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos)

    def imprimir(self):
        print(f"Valor de administración: {self._valorAdmin}")
        super().imprimir()

#///////////////////////////////////////////////////////////

from enum import Enum

class Local(Inmueble):
    class Tipo(Enum):
        INTERNO = "INTERNO"
        CALLE = "CALLE"
    def __init__(self, id_inmobiliario, direccion, area,tipoLocal:Tipo):
        super().__init__(id_inmobiliario, direccion, area)
        self._tipoLocal = tipoLocal
    
    def imprimir(self):
        print(f"Tipo de local: {self._tipoLocal}")
        return super().imprimir()


class LocalComercial(Local):
    _valorArea:float = 3000000
    def __init__(self, id_inmobiliario, direccion, area, tipoLocal,centroComercial):
        super().__init__(id_inmobiliario, direccion, area, tipoLocal)
        self._centroComercial = centroComercial

    def imprimir(self):
        print(f"Centro comercial: {self._centroComercial}")
        return super().imprimir()


class Oficina(Local):
    _valorArea:float = 3500000
    def __init__(self, id_inmobiliario, direccion, area, tipoLocal,esGobierno:bool):
        super().__init__(id_inmobiliario, direccion, area, tipoLocal)
        self._esGobierno = esGobierno

    def imprimir(self):
        print(f"Es oficina gubernamental: {self._esGobierno}")
        return super().imprimir()
    
#///////////////////////////////////////////////////////////////////

#por fin, la prueba

class Prueba():
    if __name__ == "__main__":
        apto1 = ApartamentoFamiliar(103067,"Avenida-Santander-45-45",120,3,2,200000)
        apto1.calcularPrecioVenta(apto1._valorArea)
        aptestudio1 = Apartaestudio(12354,"Avenida Caracas 30-15",50)
        aptestudio1.calcularPrecioVenta(aptestudio1._valorArea)
        aptestudio1.imprimir()