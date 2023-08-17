autos = []


def buscar_auto_por_modelo(modelo):
    for auto in autos:
        if auto.modelo == modelo:
            return auto
    return None

def agregar_auto(marca, modelo, año):
    nuevo_auto = autos(marca, modelo, año)
    autos.append(nuevo_auto)
    print("Auto agregado exitosamente.")


while True:
    print("\nMenú:")
    print("1. Buscar auto")
    print("2. Agregar auto")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        modelo_buscar = input("Ingrese el modelo del auto a buscar: ")
        auto_encontrado = buscar_auto_por_modelo(modelo_buscar)
        if auto_encontrado:
            print("Auto encontrado:")
            print(f"Marca: {auto_encontrado.marca}")
            print(f"Modelo: {auto_encontrado.modelo}")
            print(f"Año: {auto_encontrado.año}")
            print(f"Disponible: {'Sí' if auto_encontrado.disponible else 'No'}")
        else:
            print("Auto no encontrado.")

    elif opcion == "2":
        marca = input("Ingrese la marca del auto: ")
        modelo = input("Ingrese el modelo del auto: ")
        año = input("Ingrese el año del auto: ")
        agregar_auto(marca, modelo, año)
        

    elif opcion == "3":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, elija una opción válida.")