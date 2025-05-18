class cuenta():
    _saldo:float= 0.0
    _numCon:int= 0
    _numRet:int= 0
    _tasAnu:float= 0.0
    _comMen:float= 0.0

    def __init__(self,saldo:float,tasAnu:float):
        self._saldo= saldo
        self._tasAnu= tasAnu

    def consignar(self, cantidad: float):
        self._saldo +=cantidad

        self._numCon+=1

    def retirar(self, cantidad:float):
        if cantidad  < self._saldo and cantidad > 0:
            self._saldo-=cantidad
            self._numRet+=1

        else:
            return "La cantidad a retirar excede el saldo actual"
        
    def calcularInt(self):
        tasMen:float=self._tasAnu/12
        intMen:float=tasMen*self._saldo
        self._saldo+=intMen

    def extractoMen(self):
        self._saldo-=self._comMen
        self.calcularInt()

class CuentaAhorros(cuenta):
    _activa:bool

    def __init__(self, saldo, tasAnu):
        super().__init__(saldo, tasAnu)
        self._activa=self._saldo>=10000
    
    def consignar(self, cantidad):
        if self._activa:
            super().consignar(cantidad)
            self._activa=self._saldo>=10000
    
    def retirar(self, cantidad):
        if self._activa:
            super().retirar(cantidad)
            self._activa=self._saldo>=10000
    
    def extractoMen(self):
        if self._numRet>4:
            self._comMen+=(self._numRet-4)*1000
        super().extractoMen()
        self._activa=self._saldo>=10000

    def imprimir(self):
        total_Transacciones=self._numCon+self._numRet
        print(f"Cuenta de ahorros:\nSaldo: ${self._saldo:.2f}\nComisión mensual: ${self._comMen:.2f}\nTransacciones: {total_Transacciones}\nActiva: {self._activa}")


class CuentaCorriente(cuenta):
    _sobregiro:float

    def __init__(self, saldo, tasAnu):
        super().__init__(saldo, tasAnu)
        self._sobregiro=0
    
    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad<= self._saldo:
                self._saldo-=cantidad
            
            else:
                self._sobregiro += (cantidad-self._saldo)
                self._saldo=0
            self._numRet+=1
    
    def consignar(self, cantidad):
        if cantidad > 0:
            if self._sobregiro > 0:
                if cantidad >= self._sobregiro:
                    cantidad-=self._sobregiro
                    self._sobregiro -=cantidad
                    self._sobregiro=0
                else:
                    self._cantidad-=self._sobregiro
                    cantidad=0
            self._saldo+=cantidad
            self._numCon+=1

    def imprimir(self):
        total_Transacciones=self._numCon+self._numRet
        print(f"Cuenta corriente:\nSaldo: ${self._saldo:.2f}\nSobregiro: ${self._sobregiro:.2f}\nTransacciones: {total_Transacciones}")

if __name__ == "__main__":
    cuenta1 = cuenta(0,10)
    cuenta1.consignar(100)
    cuenta1.retirar(40)
    cuenta1.calcularInt()
    cuenta1.extractoMen()
    print(f"Saldo: {cuenta1._saldo:.2f}\n Número de consignaciones: {cuenta1._numCon}\n Número de retiros: {cuenta1._numRet}\n Tasa Anual: {cuenta1._tasAnu}\n Comision Mensual: {cuenta1._comMen} ")
    cuenta2 = CuentaAhorros(12000,10)
    cuenta2.consignar(1000)
    cuenta2.retirar(1000)
    cuenta2.extractoMen()
    cuenta2.imprimir()