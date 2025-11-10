valor1 = float(input("Ingrese su valor del producto"))

porcentaje = valor1 * 0.05
Valorfinal = valor1 + porcentaje
if valor1 > 150000:
    print(f"Tienes un descuento del 5%: {porcentaje}")
    print(f"Tu valor final es de: {Valorfinal}")
else:
    print("No tienes ningun descuento")
    