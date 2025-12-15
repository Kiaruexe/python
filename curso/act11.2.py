#El día juliano correspondiente a una fecha es un número entero que indica 
# los días que han transcurrido desde el 1 de enero del año indicado. 
# Queremos crear un programa principal que al introducir una fecha nos diga 
# el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:

#LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
#DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
#EsBisiesto: Recibe un año y nos dice si es bisiesto.
#Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.
def LeerFecha():
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    return dia, mes, anio
def EsBisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
def DiasDelMes(mes, anio):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if EsBisiesto(anio) else 28
    else:
        return 0
def CalcularDiaJuliano(dia, mes, anio):
    diaJuliano = 0
    for m in range(1, mes):
        diaJuliano += DiasDelMes(m, anio)
    diaJuliano += dia
    return diaJuliano
dia, mes, anio = LeerFecha()
diaJuliano = CalcularDiaJuliano(dia, mes, anio)
print(f"La fecha {dia}/{mes}/{anio} corresponde al día juliano: {diaJuliano}")
