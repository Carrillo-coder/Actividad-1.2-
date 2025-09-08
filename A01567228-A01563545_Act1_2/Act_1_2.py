# Actividad 1.2 Implementación de la técnica de programación "Programación dinámica" y "algoritmos avaros" 
# Alejandro Carrillo | A01567228
# Héctor Vargas | A01563545

N = int(input("Ingrese el número de denominaciones de monedas: "))
denominaciones = [int(input(f"Ingrese la denominación de la moneda {i + 1}: ")) for i in range(N)]
P = int(input("Ingrese el precio del artículo: "))
Q = int(input("Ingrese la cantidad pagada: "))
vuelto = Q - P

# Versión de Programación Dinámica
print("\n--- Programación Dinámica ---")

denominaciones_dp = sorted(denominaciones)
if vuelto < 0:
    print("Error: El pago es menor que el precio.")
elif vuelto == 0:
    for _ in range(len(denominaciones_dp)):
        print("0")
else:
    ArrayMonedas = [float('inf')] * (vuelto + 1)
    monedasUsadas = [-1] * (vuelto + 1)
    ArrayMonedas[0] = 0

    for i in range(1, vuelto + 1):
        for moneda in denominaciones_dp:
            if moneda <= i:
                if ArrayMonedas[i - moneda] + 1 < ArrayMonedas[i]:
                    ArrayMonedas[i] = ArrayMonedas[i - moneda] + 1
                    monedasUsadas[i] = moneda
            else:
                break

    cambioMonedas = {m: 0 for m in denominaciones_dp}

    temp = vuelto
    while temp > 0:
        moneda = monedasUsadas[temp]
        if moneda == -1:
            print("¿Será que le pueda pagar con dulces de a peso? (No hay vuelto suficiente en la caja)")
            break
        cambioMonedas[moneda] += 1
        temp -= moneda

for coin in sorted(denominaciones_dp, reverse=True):
    print(f"{cambioMonedas[coin]} monedas de {coin}")


# Versión de Algoritmo Avaro
print("\n--- Algoritmo Avaro ---")

denominaciones_greedy = sorted(denominaciones, reverse=True)
if vuelto < 0:
    print("Error: El pago es menor que el precio.")
elif vuelto == 0:
    for _ in denominaciones_greedy:
        print("0")
else:
    cambioMonedas = {c: 0 for c in denominaciones_greedy}

    temp_vuelto = vuelto
    for coin in denominaciones_greedy:
        count = temp_vuelto // coin
        cambioMonedas[coin] = count
        temp_vuelto %= coin

    if temp_vuelto > 0:
        print("¿Será que le pueda pagar con dulces de a peso? (No hay vuelto suficiente con las denominaciones disponibles en version avaro).")

    for coin in denominaciones_greedy:
        print(f"{cambioMonedas[coin]} monedas de {coin}")
