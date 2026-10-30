import streamlit as st

st.title("Sistema de registro PavimentIQ")

cantidad = st.number_input("¿Cuántos reportes desea ingresar?", min_value=1, max_value=20, value=1, step=1)

calles = []
tipos_daño = []
gravedad = []
flujo_vehicular = []

st.markdown("Ingrese los datos de los reportes:")

for i in range(int(cantidad)):
    st.write(f"--- Reporte {i + 1} ---")
    nombre_calle = st.text_input(f"Nombre de la calle o avenida {i + 1}", key=f"c_{i}")
    tipo = st.text_input(f"Tipo de daño (ej. Bache, Fisura) {i + 1}", key=f"t_{i}")
    grav = st.slider(f"Nivel de gravedad (1 al 5) {i + 1}", 1, 5, 3, key=f"g_{i}")
    flujo = st.selectbox(f"Flujo vehicular {i + 1}", ["Alto", "Medio", "Bajo"], key=f"f_{i}")

    if nombre_calle:
        calles.append(nombre_calle)
        tipos_daño.append(tipo)
        gravedad.append(grav)
        flujo_vehicular.append(flujo)

if st.button("Generar Reporte en Pantalla"):
    if len(calles) > 0:
        salida = []

        salida.append("-" * 50)
        salida.append("Sistema de registro PavimentIQ")
        salida.append("-" * 50)

        salida.append("\n" + "=" * 60)
        salida.append("Control general del estado de las vias")
        salida.append("=" * 60)

        for i in range(len(calles)):
            salida.append(f"[{i + 1}] Calle/Av: {calles[i]}")
            salida.append(f"Tipo de Daño: {tipos_daño[i]}")
            salida.append(f"Nivel de Gravedad (1-5): {gravedad[i]}")
            salida.append(f"Flujo Vehicular: {flujo_vehicular[i]}")
            salida.append("-" * 60)

        salida.append("-" * 60)
        salida.append("Plan de accion en las vias prioritarias de urgencia")
        salida.append("-" * 60)

        contador_urgentes = 0
        for i in range(len(calles)):
            if gravedad[i] >= 4:
                salida.append(f"Prioridad de urgencia en: '{calles[i]}'")
                salida.append(f"Motivo: {tipos_daño[i]} con gravedad {gravedad[i]} y tráfico {flujo_vehicular[i]}.")
                contador_urgentes += 1
                salida.append("-" * 60)

        if contador_urgentes == 0:
            salida.append("No hay calles registradas en estado crítico.")
        else:
            salida.append(f"Total de vías prioritarias a reparar: {contador_urgentes}")

        salida.append("\n" + "-" * 60)
        salida.append("Resumen general de todas las calles")
        salida.append("-" * 60)

        for i in range(len(calles)):
            salida.append(f"Calle: {calles[i]}")
            salida.append(f"Daño registrado: {tipos_daño[i]}")
            salida.append(f"Gravedad: {gravedad[i]}/5")
            salida.append(f"Tráfico vehicular: {flujo_vehicular[i]}")
            salida.append("-" * 60)

        salida.append("Integrantes finales del grupo: ")
        salida.append("Jafar Leopoldo Baldiviezo Apaza")
        salida.append("Miguel Angel Limachi Lopez")
        salida.append("Maykel Nemecio Aranibar Urbano")

        st.text("\n".join(salida))

    else:
        st.error("Por favor completa al menos una calle.")