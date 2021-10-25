
class Asiento:
    def __init__(self, color, precio, registro) -> None:
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color: str):
        if color in ['rojo', 'verde', 'amarillo', 'negro', 'blanco']:
            self.color = color


class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro) -> None:
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        count = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                count += 1

        return count

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return 'Las piezas no son originales'
        else:
            for asiento in self.asientos:
                if isinstance(asiento, Asiento) and self.registro != asiento.registro:
                    return 'Las piezas no son originales'

        return 'Auto original'


class Motor:
    def __init__(self, numeroCilindros, tipo, registro) -> None:
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro: int):
        self.registro = registro

    def asignarTipo(self, tipo: str):
        if tipo in ['electrico', 'gasolina']:
            self.tipo = tipo


