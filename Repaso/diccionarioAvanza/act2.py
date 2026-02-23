#Ejercicio 2
#Normalización de datos de usuarios
#Una aplicación almacena información de usuarios en un diccionario donde las claves son los IDs 
# y los valores son tuplas con la edad y el ingreso mensual de cada usuario. Escribe un programa 
# que recorra el diccionario y cree una nueva lista de tuplas, donde la edad e ingreso mensual 
# estén normalizados entre 0 y 1 con respecto al máximo encontrado en cada categoría.

#Nota sobre la normalización de datos:

#La normalización es un proceso matemático utilizado para escalar valores dentro de un rango común, 
#generalmente entre 0 y 1.
#Este proceso asegura que todos los valores estén representados proporcionalmente entre 0 y 1, 
# preservando las relaciones relativas entre ellos.
#La fórmula básica para normalizar un valor ( x ) es:

#xnormalizado=x−xmín/xmáx−xmín 

#Donde:

#x  es el valor original.
#xmín  es el valor mínimo en la serie de datos.
#xmáx  es el valor máximo en la serie de datos.
#En situaciones donde no hay valores negativos, la formula sería:
#xnormalizado=xxmáx 
#Esta última fórmula es válida si todos los valores son positivos y la escala de interés se centra en el máximo.


usuarios = {
    1: (25, 3000),
    2: (0, 4500),  
    3: (22, 0),    
    4: (30, 3800),
    5: (0, 0),  
    6: (27, 5000),
}

# Encontramos el máximo de edad e ingreso mensual
maxEdad = max(edad for edad, ingreso in usuarios.values())
maxIngreso = max(ingreso for edad, ingreso in usuarios.values())
# Creamos una nueva lista de tuplas con edad e ingreso normalizados
usuariosNormalizados = []
for edad, ingreso in usuarios.values():
    edadNormalizada = edad / maxEdad if maxEdad > 0 else 0
    ingresoNormalizado = ingreso / maxIngreso if maxIngreso > 0 else 0
    usuariosNormalizados.append((edadNormalizada, ingresoNormalizado))
print(usuariosNormalizados)

