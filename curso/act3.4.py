#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por 
# un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas 
# las notas, la nota media, la nota más alta que ha sacado y la menor.
notas = []
for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1} (entre 0 y 10): "))
    while nota < 0 or nota > 10:
        print("Nota inválida. Intente nuevamente.")
        nota = float(input(f"Ingrese la nota {i+1} (entre 0 y 10): "))
    notas.append(nota)
print("Notas ingresadas:", notas)
nota_media = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)
print(f"Nota media: {nota_media}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")