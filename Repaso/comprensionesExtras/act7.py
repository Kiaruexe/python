#7. Combinando filtros y condicionales.
#¡Este ejercicio de comprensiones combinaremos filtros con expresiones condicionales!
#Tienes algunos datos sobre porcentajes que necesitamos formatear de la misma manera. 
# Ignoraremos aquellos valores a None.
#El formato que queremos conseguir para todos los valores de la lista es:
#Float con dos decimales seguido del %
#Buena suerte 🚀

porcentajes = [12, "23.5", None, 98.125, None, "73", 25.1, "55.238", 87, None, 21.02]
porcentajesFormateados = [f"{float(p):.2f}%" if isinstance(p, str) else f"{p:.2f}%" for p in porcentajes if p is not None]
print(porcentajesFormateados)