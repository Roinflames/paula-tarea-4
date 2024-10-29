# Archivo main.py
import parametros as p
import random
# from parametros import RESISTENCIA

# Clase Rueda implementada (no modificar)
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
        if self.resistencia_actual <= 0:
            self.estado = "Rota"
        elif self.resistencia_actual <= self.resistencia_total * 0.5:
            self.estado = "Gastada"
        else:
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

# Función avanzar
def avanzar(velocidad, tiempo):
    return (velocidad * tiempo) / 1000

# Clase Automovil
class Automovil:
    def __init__(self, kilometraje, ano):
        self.kilometraje = kilometraje
        self.ano = ano
        self.ruedas = [Rueda() for _ in range(4)]
        self.aceleracion = 0
        self.velocidad = 0

    def avanzar(self, tiempo):
        velocidad_ms = self.velocidad / 3.6
        self.kilometraje += avanzar(velocidad_ms, tiempo)

    def acelerar(self, tiempo):
        tiempo_horas = tiempo / 3600
        self.aceleracion += tiempo_horas * 0.5
        self.velocidad += self.aceleracion * tiempo_horas
        self.avanzar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar("acelerar", "automovil")
        self.aceleracion = 0

    def frenar(self, tiempo):
        tiempo_horas = tiempo / 3600
        self.aceleracion -= tiempo_horas * 0.5
        self.velocidad += self.aceleracion * tiempo_horas
        if self.velocidad < 0:
            self.velocidad = 0
        self.avanzar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar("frenar", "automovil")
        self.aceleracion = 0

    def obtener_kilometraje(self):
        return self.kilometraje

    def reemplazar_rueda(self):
        rueda_menor_resistencia = min(self.ruedas, key=lambda r: r.resistencia_actual)
        self.ruedas.remove(rueda_menor_resistencia)
        self.ruedas.append(Rueda())

# Clase Moto
class Moto(Automovil):
    def __init__(self, kilometraje, ano, cilindrada):
        super().__init__(kilometraje, ano)
        self.ruedas = [Rueda() for _ in range(2)]
        self.cilindrada = cilindrada

    def acelerar(self, tiempo):
        tiempo_horas = tiempo / 3600
        self.aceleracion += (tiempo_horas * 0.8) + (self.cilindrada * 0.2)
        self.velocidad += self.aceleracion * tiempo_horas * 3
        self.avanzar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar("acelerar", "moto")
        self.aceleracion = 0

    def frenar(self, tiempo):
        tiempo_horas = tiempo / 3600
        self.aceleracion -= (tiempo_horas * 0.8) + (self.cilindrada * 0.2)
        self.velocidad += self.aceleracion * tiempo_horas * 2
        if self.velocidad < 0:
            self.velocidad = 0
        self.avanzar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar("frenar", "moto")
        self.aceleracion = 0

    def reemplazar_rueda(self):
        ruedas_a_reemplazar = [rueda for rueda in self.ruedas if rueda.resistencia_actual < rueda.resistencia_total * 0.5]
        for rueda in ruedas_a_reemplazar:
            self.ruedas.remove(rueda)
            self.ruedas.append(Rueda())

# Función accion
def accion(vehiculo, opcion):
    if opcion == 2:  # Acelerar
        tiempo = float(input("Ingrese el tiempo para acelerar en segundos: "))
        vehiculo.acelerar(tiempo)
        print(f"Se ha acelerado por {tiempo} segundos, llegando a una velocidad de {vehiculo.velocidad} km/h")
    elif opcion == 3:  # Frenar
        tiempo = float(input("Ingrese el tiempo para frenar en segundos: "))
        vehiculo.frenar(tiempo)
        print(f"Se ha frenado por {tiempo} segundos, llegando a una velocidad de {vehiculo.velocidad} km/h")
    elif opcion == 4:  # Avanzar
        tiempo = float(input("Ingrese el tiempo para avanzar en segundos: "))
        vehiculo.avanzar(tiempo)
        print(f"Se ha avanzado por {tiempo} segundos a una velocidad de {vehiculo.velocidad} km/h")
    elif opcion == 5:  # Cambiar rueda
        vehiculo.reemplazar_rueda()
        print("Se han reemplazado las ruedas con éxito")
    elif opcion == 6:  # Mostrar estado
        print(f"Año: {vehiculo.ano}, Velocidad: {vehiculo.velocidad} km/h, Kilometraje: {vehiculo.obtener_kilometraje()} km")
        for i, rueda in enumerate(vehiculo.ruedas):
            print(f"Rueda {i + 1}: Estado {rueda.estado}, Resistencia Actual: {rueda.resistencia_actual}, Resistencia Total: {rueda.resistencia_total}")

def main():
    # vehiculos = [
    #     "automovil",
    #     "moto"
    # ]

    vehiculos = [
        Automovil(kilometraje=1000, ano=2015),
        Moto(kilometraje=500, ano=2018, cilindrada=150)
    ]
    print(vehiculos)
    
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