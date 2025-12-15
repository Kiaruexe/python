#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
esBisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
if mes < 1 or mes > 12:
    print("Fecha incorrecta")
elif dia < 1:
    print("Fecha incorrecta")
elif mes == 2:
    if esBisiesto and dia > 29:
        print("Fecha incorrecta")
    elif not esBisiesto and dia > 28:
        print("Fecha incorrecta")
    else:
        print("Fecha correcta")
elif mes in [4, 6, 9, 11]:
    if dia > 30:
        print("Fecha incorrecta")
    else:
        print("Fecha correcta")
else:
    if dia > 31:
        print("Fecha incorrecta")
    else:
        print("Fecha correcta")
