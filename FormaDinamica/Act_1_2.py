
N = int(input("Ingrese el número de denominaciones de monedas: "))
denominaciones = sorted([int(input(f"Ingrese la denominación de la moneda {i + 1}: ")) for i in range(N)])
P = int(input("Ingrese el precio del artículo: "))
Q = int(input("Ingrese la cantidad pagada: "))
vuelto = Q - P

if vuelto < 0:
    print("Error: El pago es menor que el precio.")

if vuelto == 0:
    for _ in range(len(denominaciones)):
        print("No hay vuelto")

ArrayMonedas = [float('inf')] * (vuelto + 1)
monedasUsadas = [-1] * (vuelto + 1)
ArrayMonedas[0] = 0

for i in range(1, vuelto + 1):
    for moneda in denominaciones:
        if moneda <= i:
            if ArrayMonedas[i - moneda] + 1 < ArrayMonedas[i]:
                ArrayMonedas[i] = ArrayMonedas[i - moneda] + 1
                monedasUsadas[i] = moneda
        else:
            break
cambioMonedas = {}
for coin in denominaciones:
    cambioMonedas[coin] = 0

temp = vuelto
while temp > 0:
    coin = monedasUsadas[temp]
    cambioMonedas[coin] += 1
    temp -= coin

for coin in sorted(denominaciones, reverse=True):
    print(str(cambioMonedas[coin]) + " monedas de " + str(coin)) 