#Vamos a crear un programa en python donde vamos a declarar un 
# diccionario para guardar los precios de las distintas frutas. El programa 
# pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará 
# el precio final de la fruta a partir de los datos guardados en el diccionario. 
# Si la fruta no existe nos dará un error. Tras cada consulta el programa nos 
# preguntará si queremos hacer otra consulta.
precioFrutas = {
    "manzana": 2.5,
    "platano": 1.8,
    "naranja": 3.0,
    "pera": 2.2,
    "uva": 4.0
}
while True:
    fruta = input("Ingrese el nombre de la fruta (o 'salir' para terminar): ").lower()
    if fruta == 'salir':
        break
    if fruta in precioFrutas:
        cantidad = float(input(f"Ingrese la cantidad de {fruta} vendida (en kg): "))
        precioFinal = precioFrutas[fruta] * cantidad
        print(f"El precio final de {cantidad} kg de {fruta} es: {precioFinal:.2f} euros")
    else:
        print("Error: La fruta no existe en el diccionario.")
    otraConsulta = input("¿Desea hacer otra consulta? (s/n): ").lower()
    if otraConsulta != 's':
        break

