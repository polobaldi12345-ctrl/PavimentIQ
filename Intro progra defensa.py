calles = []
tipos_daño = []
gravedad = []
flujo_vehicular = []

print("-" * 50)
print("Sistema de registro PavimentIQ")
print("-" * 50)

cantidad = int(input("¿Cuantos reportes desea ingresar?: "))

for i in range(cantidad):
    print(f"\nIngresando datos para el reporte {i + 1}")

    nombre_calle = input("Nombre de la calle o avenida: ")
    tipo = input("Tipo de daño (ej. Bache profundo, Fisura, Hundimiento): ")
    grav = int(input("Nivel de gravedad (escala del 1 al 5): "))
    flujo = input("Flujo vehicular (Alto, Medio, Bajo): ")

    calles.append(nombre_calle)
    tipos_daño.append(tipo)
    gravedad.append(grav)
    flujo_vehicular.append(flujo)

print("\n" + "=" * 60)
print("Control general del estado de las vias")
print("=" * 60)

for i in range(len(calles)):
    print(f"[{i + 1}] Calle/Av: {calles[i]}")
    print(f"Tipo de Daño: {tipos_daño[i]}")
    print(f"Nivel de Gravedad (1-5): {gravedad[i]}")
    print(f"Flujo Vehicular: {flujo_vehicular[i]}")
    print("-" * 60)

print("-" * 60)
print("Plan de accion en las vias prioritarias de urgencia")
print("-" * 60)

contador_urgentes = 0

for i in range(len(calles)):
    if gravedad[i] >= 4:
        print(f"Prioridad de urgencia en: '{calles[i]}'")
        print(f"Motivo: {tipos_daño[i]} con gravedad {gravedad[i]} y tráfico {flujo_vehicular[i]}.")
        contador_urgentes += 1
        print("-" * 60)

if contador_urgentes == 0:
    print("No hay calles registradas en estado crítico.")
else:
    print(f"Total de vías prioritarias a reparar: {contador_urgentes}")


print("\n" + "-" * 60)
print("Resumen general de todas las calles")
print("-" * 60)

for i in range(len(calles)):
    print(f"Calle: {calles[i]}")
    print(f"Daño registrado: {tipos_daño[i]}")
    print(f"Gravedad: {gravedad[i]}/5")
    print(f"Tráfico vehicular: {flujo_vehicular[i]}")
    print("-" * 60)

print("Integrantes finales del grupo: ")
print("Jafar Leopoldo Baldiviezo Apaza")
print("Miguel Angel Limachi Lopez")
print("Maykel Nemecio Aranibar Urbano")