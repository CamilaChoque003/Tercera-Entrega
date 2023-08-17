class Auto:
    def __init__(self, marca, modelo, año, disponible=True):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.disponible = disponible

    def __str__(self):
        disponible_str = "Disponible" if self.disponible else "No disponible"
        return f"{self.marca} {self.modelo} ({self.año}) - {disponible_str}"

class Cliente:
    def __init__(self, nombre, apellido, edad, licencia):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.licencia = licencia

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Edad: {self.edad}"

class Alquiler:
    def __init__(self, auto, cliente, dias):
        self.auto = auto
        self.cliente = cliente
        self.dias = dias

    def calcular_costo(self, costo_diario):
        return self.dias * costo_diario


auto1 = Auto("Peugeot", "208", 2015)
auto2 = Auto("Peugeot", "3008", 2022, False)

cliente1 = Cliente("Matias", "Perez", 40, "20345")
cliente2 = Cliente("Araceli", "Martinez", 25, "24855")

alquiler1 = Alquiler(auto1, cliente1, 5)
alquiler2 = Alquiler(auto2, cliente2, 3)

costo_diario = 90000
costo_alquiler1 = alquiler1.calcular_costo(costo_diario)
costo_alquiler2 = alquiler2.calcular_costo(costo_diario)

print("Autos disponibles:")
print(auto1)
print(auto2)

print("\nClientes:")
print(cliente1)
print(cliente2)

print("\nAlquileres:")
print(alquiler1.auto)
print(alquiler1.cliente)
print(f"Días: {alquiler1.dias}")
print(f"Costo total: ${costo_alquiler1}")

print("\n")
print(alquiler2.auto)
print(alquiler2.cliente)
print(f"Días: {alquiler2.dias}")
print(f"Costo total: ${costo_alquiler2}")
