import parametros as p
import random
# NO MODIFICAR
class Rueda:
    def __init__(self):
        self.resistencia_actual = random.randint(*p.RESISTENCIA)
        self.resistencia_total = self.resistencia_actual
        self.estado = "Perfecto"

    def gastar(self, accion, tipo):
        if accion == "acelerar":
            if tipo == "automovil":
                self.resistencia_actual -= 5
            elif tipo == "moto":
                self.resistencia_actual -= 3
        elif accion == "frenar":
            if tipo == "automovil":
                self.resistencia_actual -= 10
            elif tipo == "moto":
                self.resistencia_actual -= 7
        self.actualizar_estado()

    def actualizar_estado(self):
        if self.resistencia_actual < 0:
            self.estado = "Rota"
        elif self.resistencia_actual < self.resistencia_total / 2:
            self.estado = "Gastada"
        elif self.resistencia_actual < self.resistencia_total:
            self.estado = "Usada"

# NO MODIFICAR
def seleccionar(vehiculos):
    if not len(vehiculos):
        print("No hay vehículos instanciados todavía")
        return

    print("Los vehículos disponibles son:")
    for indice in range(len(vehiculos)):
        print(f"[{indice}] {str(vehiculos[indice])}")

    elegido = int(input())
    while elegido < 0 or elegido >= len(vehiculos):
        print("intentelo de nuevo.")
        elegido = int(input())

    vehiculo = vehiculos[elegido]
    print("Se seleccionó el vehículo", str(vehiculo))
    return vehiculo

# Parte 1: Definición de clases
def avanzar(velocidad, tiempo):
    kilometraje = (velocidad * tiempo) / 1000
    return kilometraje

class Automovil:
    def __init__(self):
        self.kilometraje = 0
        self.ano = 0
        self.ruedas = [Rueda(),Rueda(),Rueda(),Rueda(),]
        self.aceleracion = 0
        self.velocidad = 0
    
    def avanzar(self, tiempo):
        self.kilometraje = self.kilometraje / 3.6
    
    def acelerar(self, tiempo):
        tiempo /= 3600
        self.aceleracion += tiempo * 0.5
        self.velocidad += self.aceleracion * tiempo
        avanzar(tiempo)
        Rueda.gastar()
        self.aceleracion = 0

    def frenar(self, tiempo):
        tiempo /= 3600
        self.aceleracion -= tiempo * 0.5
        self.velocidad += self.aceleracion * tiempo
        avanzar(tiempo)
        Rueda.gastar()
        self.aceleracion = 0

    def obtener_kilometraje(self):
        return self.kilometraje

    def reemplazar_rueda(self):
        for indice in self.ruedas:
            self.ruedas.append(Rueda())
            pass
    def __str__(self):
        return f"Automóvil del año {self.ano}."

class Moto:
    def __init__(self):
        self.kilometraje = 0
        self.ano = 0
        self.ruedas = [
            Rueda(),
            Rueda(),
        ]
        self.aceleracion = 0
        self.velocidad = 0
        self.cilindrada = 0

    def avanzar(self, tiempo):
        self.kilometraje = self.kilometraje / 3.6
    
    def acelerar(self, tiempo):
        tiempo /= 3600
        self.aceleracion += tiempo * 0.8 + self.cilindrada * 0.2
        self.velocidad += self.aceleracion * tiempo * 3
        avanzar(tiempo)
        Rueda.gastar()
        self.aceleracion = 0

    def frenar(self, tiempo):
        tiempo /= 3600
        self.aceleracion -= tiempo * 0.8 + self.cilindrada * 0.2
        self.velocidad += self.aceleracion * tiempo * 2
        avanzar(tiempo)
        Rueda.gastar()
        self.aceleracion = 0

    def obtener_kilometraje(self):
        return self.kilometraje

    def reemplazar_rueda(self):
        for indice in self.ruedas:
            if(True):
                Rueda.pop()
                self.ruedas.append(Rueda())
    def __str__(self):
        return f"Moto del año {self.ano}."

# Parte 2: Completar acciones
def accion(vehiculo, opcion):
    # Completar
    if opcion == 2:  # Acelerar
        pass
    elif opcion == 3:  # Frenar
        pass
    elif opcion == 4:  # Avanzar
        texto = "Escoja un tiempo en segundos para avanzar el vehículo: "
        try:
            opcion = int(input(texto))
            print()
            avanzar(opcion, opcion)

        except ValueError:
            print("Ingrese opción válida.")
    elif opcion == 5:  # Cambiar rueda
        pass
    elif opcion == 6:  # Mostrar Estado
        pass

def main():
    vehiculos = [
        "automovil",
        "moto"
    ]
    
    # Parte 3: Completar código principal
    # Completar
    # Aquí debes instanciar los dos objetos pedidos
    # y agregarlos a la lista de vehículos

    # NO MODIFICAR
    vehiculo = None

    dict_opciones = {
        1: ("Seleccionar Vehiculo", seleccionar),
        2: ("Acelerar", accion),
        3: ("Frenar", accion),
        4: ("Avanzar", accion),
        5: ("Reemplazar Rueda", accion),
        6: ("Mostrar Estado", accion),
        0: ("Salir", None)
    }

    opcion = -1
    while opcion != 0:

        for llave, valor in dict_opciones.items():
            print(f"{llave}: {valor[0]}")

        try:
            opcion = int(input("Opción: "))
            print()

        except ValueError:
            print("Ingrese opción válida.")
            opcion = -1

        if opcion != 0 and opcion in dict_opciones.keys():
            if opcion == 1:
                vehiculo = dict_opciones[opcion][1](vehiculos)
            else:
                if vehiculo is None and vehiculos:
                    vehiculo = vehiculos[0]
                if vehiculo is None:
                    print("Aún no hay vehículos...")
                else:
                    dict_opciones[opcion][1](vehiculo, opcion)
        elif opcion == 0:
            pass
        else:
            print("Ingrese opción válida.")
            opcion = -1

        print()


if __name__ == "__main__":
    main()
