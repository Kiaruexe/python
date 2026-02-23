#Ejercicio 4
#Procesamiento de ventas por región
#Una empresa tiene un diccionario donde las claves son regiones y los valores 
# son listas de tuplas con información de ventas (producto, cantidad, precio_unitario).

#Escribe un programa que calcule:
#El ingreso total por región y devuelva un nuevo diccionario con las regiones como claves
# y los ingresos como valores. Si en alguna región la venta total supera 10mil unidades monetarias:
#Recalcula los ingresos considerando un descuento del 10% sobre los productos cuyo precio unitario supere 50.

datosVentas = {
    'Norte': [
        ('Producto1', 27, 13.79),
        ('Producto5', 2, 31.87),
        ('Producto5', 3, 74.2),
        ('Producto5', 43, 80.26),
        ('Producto2', 23, 74.13),
        ('Producto2', 29, 49.84)
    ],
    'Sur': [
        ('Producto2', 15, 44.02),
        ('Producto5', 12, 90.66),
        ('Producto1', 33, 18.45),
        ('Producto5', 1, 88.74),
        ('Producto5', 16, 15.71),
        ('Producto3', 49, 94.61),
        ('Producto1', 12, 45.9),
        ('Producto1', 17, 87.96),
        ('Producto3', 36, 50.98),
        ('Producto4', 18, 39.32)
    ],
    'Este': [
        ('Producto3', 43, 95.86),
        ('Producto4', 8, 65.2),
        ('Producto5', 8, 72.66),
        ('Producto2', 12, 73.69),
        ('Producto5', 3, 46.67),
        ('Producto5', 1, 85.29),
        ('Producto5', 21, 94.97),
        ('Producto3', 45, 92.51),
        ('Producto3', 50, 79.64),
        ('Producto3', 4, 24.18)
    ],
    'Oeste': [
        ('Producto3', 6, 14.02),
        ('Producto3', 47, 21.55),
        ('Producto4', 46, 32.02),
        ('Producto3', 45, 46.97),
        ('Producto5', 2, 30.75)
    ],
    'Centro': [
        ('Producto4', 41, 21.6),
        ('Producto3', 20, 64.34),
        ('Producto1', 36, 36.65),
        ('Producto3', 39, 17.97),
        ('Producto5', 8, 67.43),
        ('Producto2', 35, 11.5)
    ]
}

ingresosPorRegion = {}
for region, ventas in datosVentas.items():
    ingresoTotal = 0
    for producto, cantidad, precioUnitario in ventas:
        ingreso = cantidad * precioUnitario
        if ingreso > 10000:
            if precioUnitario > 50:
                ingreso *= 0.9  
        ingresoTotal += ingreso
    ingresosPorRegion[region] = ingresoTotal
    
print(ingresosPorRegion)