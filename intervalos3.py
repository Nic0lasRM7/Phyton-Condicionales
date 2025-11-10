N1 = float(input("Ingrese el primer numero de su intervalo: "))
N2 = float(input("Ingrese el segundo numero de su intervalo: "))
N3 = float(input("Ingrese el tercer numero de su intervalo: "))
N4 = float(input("Ingrese el cuarto numero de su intervalo: "))
N5 = float(input("Ingrese el quinto numero de su intervalo: "))
N6 = float(input("Ingrese el sexto numero de su intervalo: "))

X = int(input("Ingrese su numero: "))

if X > N1 and X < N2 or X > N3 and X < N4 or X > N5 and X < N6:
    print("Tu numero esta dentr de alguno de los tres intervalos")
else:
    print("Tu numero no esta dentro de ninguno de los tres intervalos")
    