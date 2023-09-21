class NumeroNegativoException(Exception):
    pass

class NumeroNatural():
    def validarTipo(self):
        while True:
            try:
                self.NumeroNatural = int(input("Ingrese un número natural: "))
                self.NumeroNatural1 = int(input("Ingrese un número natural 2: "))

                if self.NumeroNatural < 0 or self.NumeroNatural1 < 0:
                    raise NumeroNegativoException
                break
            except ValueError as err:
                print("Oops! Ingrese un número natural. Intente otra vez...")
            except NumeroNegativoException as err:
                print("Oops! Ingrese un número entero y positivo. Intente otra vez...")
        return self.NumeroNatural, self.NumeroNatural1

    def divisores(self, a, b):
         while b:
             a, b = b, a % b
         return a


