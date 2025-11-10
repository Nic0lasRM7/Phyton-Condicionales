Precio = float(input("Introduzca el precio de su producto"))
Num1 = float(input("Ingrese su tipo de producto"))

N2 = Precio - (Precio * 0.125)
N3 = Precio - (Precio * 0.083)
N4 = Precio - (Precio * 0.032)

if Num1 == 1:
    print("Su descuento es del 12.5%")
    print(f"El valor de su producto con descuento aplicado es: {N2}")
elif Num1 == 2:
    print("Su descuento es del 8.4%")
    print(f"El valor de su producto con su descuento aplicado es: {N3}")
elif Num1 == 3:
    print("Su descuento es del 3.2%")
    print(f"El valor de su producto con descuento aplicado es de: {N4}")
else:
    print("Su descuento es del 0.0%")