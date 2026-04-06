# -*- coding: utf-8 -*-


import json

# --- Inicialización ---
macros_totales = {
    "Calorias": 0.0,
    "Proteinas": 0.0,
    "Grasas": 0.0,
    "Carbohidratos": 0.0
}

dias = []  # Lista para guardar todos los días
dia_actual = 1

# Intentamos cargar datos guardados si existen
try:
    with open("macros_semana.json", "r") as f:
        dias = json.load(f)
        if dias:
            dia_actual = len(dias) + 1
except FileNotFoundError:
    pass

# --- Objetivos diarios (ejemplo) ---
objetivo_calorias = 3000
objetivo_proteinas = 150

# --- Menú principal ---
while True:
    print(f"\n--- DIA {dia_actual} ---")
    print("1. Añadir comida")
    print("2. Finalizar día")
    print("3. Mostrar resumen diario")
    print("4. Mostrar resumen semanal")
    print("5. Reiniciar semana")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    # --- 1. Añadir comida ---
    if opcion == "1":
        comida = input("Nombre de la comida: ")
        macros_tomadas = {
            "Calorias": float(input("Calorias: ")),
            "Proteinas": float(input("Proteinas: ")),
            "Grasas": float(input("Grasas: ")),
            "Carbohidratos": float(input("Carbohidratos: "))
        }

        for clave in macros_totales:
            macros_totales[clave] += macros_tomadas[clave]

        print(f"\nComida añadida: {comida}")
        for clave, valor in macros_totales.items():
            print(f"{clave}: {valor}")

    # --- 2. Finalizar día ---
    elif opcion == "2":
        print(f"\nResumen del día {dia_actual}:")
        for clave, valor in macros_totales.items():
            print(f"{clave}: {valor}")

        # Guardar día en lista
        dias.append(macros_totales.copy())

        # Guardar en archivo
        with open("macros_semana.json", "w") as f:
            json.dump(dias, f)

        # Resetear día
        macros_totales = dict.fromkeys(macros_totales, 0.0)
        dia_actual += 1

    # --- 3. Mostrar resumen diario ---
    elif opcion == "3":
        print(f"\nResumen del día {dia_actual}:")
        for clave, valor in macros_totales.items():
            print(f"{clave}: {valor}")

    # --- 4. Mostrar resumen semanal ---
    elif opcion == "4":
        print("\nResumen semanal acumulado:")
        if not dias:
            print("No hay días registrados.")
        else:
            resumen_semanal = dict.fromkeys(macros_totales, 0.0)
            for dia in dias:
                for clave in dia:
                    resumen_semanal[clave] += dia[clave]
            for clave, valor in resumen_semanal.items():
                print(f"{clave}: {valor}")

    # --- 5. Reiniciar semana ---
    elif opcion == "5":
        dias = []
        dia_actual = 1
        macros_totales = dict.fromkeys(macros_totales, 0.0)
        with open("macros_semana.json", "w") as f:
            json.dump(dias, f)
        print("Semana reiniciada.")

    # --- 6. Salir ---
    elif opcion == "6":
        print("¡Hasta luego! Datos guardados en macros_semana.json")
        break

    else:
        print("Opción no válida, prueba de nuevo.")


with open("macros_app.py", "w") as f:
    f.write(codigo)

for clave in macros_totales:
  print(clave)

for valor in macros+totales.value():
  print(valor)

for valor, clave in macros_totales.items():
  print(f"{clave}: {valor}")

for clave in macros_totales:
  macros_totales += macros_tomadas
  print(clave[macros_totales])
