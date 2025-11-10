Nota1 = float(input("Ingrese su primer nota: "))
Nota2 = float(input("Ingrese su segunda nota: "))
Nota3 = float(input("Ingrese su tercer nota: "))
Nota4 = float(input("Ingrese su cuarta nota: "))
Nota5 = float(input("Ingrese su quinta nota: "))

NotaDefinitiva = (Nota1 + Nota2 + Nota3 + Nota4 + Nota5)/5
if NotaDefinitiva >= 3.5:
    print(f"Felicidades, pasaste el curso con: {NotaDefinitiva}")
else:
    print("Repites la materia, LOL que mal")