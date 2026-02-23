#Ejercicio 2 - Numero de vocales en un texto
#Desarrolla un programa que devuelva un diccionario que 
# tenga por claves las vocales y en valor el número de veces 
# que aparece dicha vocal en la frase.

#Para el ejercicio utilizar la siguiente texto:

#En un lugar de la Mancha2, de cuyo nombre no quiero acordarme3, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor4. Una olla de algo más vaca que carnero, salpicón las más noches5, duelos y quebrantos los sábados6, lantejas los viernes7, algún palomino de añadidura los domingos8, consumían las tres partes de su hacienda9. El resto della concluían sayo de velarte10, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo11, y los días de entresemana se honraba con su vellorí de lo más fino12. Tenía en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera13. Frisaba la edad de nuestro hidalgo con los cincuenta años14. Era de complexión recia, seco de carnes, enjuto de rostro15, gran madrugador y amigo de la caza.

#Como puedes observar, algunas palabras contienen referencias 
# bibligráficas(números). En esta ocasión no lo tendremos en 
# cuenta pero en futuros ejercicios, aprenderemos a limpiar 
# un texto y dejarlo acorde a los requerimientos que nos pidan.

texto = "En un lugar de la Mancha2, de cuyo nombre no quiero acordarme3, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor4. Una olla de algo más vaca que carnero, salpicón las más noches5, duelos y quebrantos los sábados6, lantejas los viernes7, algún palomino de añadidura los domingos8, consumían las tres partes de su hacienda9. El resto della concluían sayo de velarte10, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo11, y los días de entresemana se honraba con su vellorí de lo más fino12. Tenía en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera13. Frisaba la edad de nuestro hidalgo con los cincuenta años14. Era de complexión recia, seco de carnes, enjuto de rostro15, gran madrugador y amigo de la caza."

texto = texto.lower()

vocales = "aeiou"

contadorVocales = {}

for letra in texto:
    if letra in vocales:
        if letra in contadorVocales:
            contadorVocales[letra] += 1
        else:
            contadorVocales[letra] = 1
            

print(contadorVocales)