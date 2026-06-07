# ejercicio 1: calcular velocidad final del automovil
# datos proporcionados
velocidad_inicial=0
aceleracion=0.8
tiempo =30

#calculo
velocidad_final=velocidad_inicial+aceleracion*tiempo
velocidad_final_kmh=velocidad_final*3.6

# resultados
print("===EJERCICIO 1: VELOCIDAD FINAL===")
print(f"velocidad inicial:{velocidad_inicial}m/s")
print(f"aceleracion:{aceleracion}m/s²")
print(f"tiempo transcurido:{tiempo}segundos")
print(f"velocidad final:{velocidad_final}m/s")
print(f"equivale a:{velocidad_final_kmh}km/h")