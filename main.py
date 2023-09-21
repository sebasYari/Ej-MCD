from logica.NumeroNatural import NumeroNatural

if __name__ == '__main__':
    numero = NumeroNatural()

    a, b = numero.validarTipo()

    resultado= numero.divisores(a, b)

    print(f"Su MCD es: {resultado}")





