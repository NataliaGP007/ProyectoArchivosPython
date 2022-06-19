from abc import ABC

class Numerologia(ABC):

    @staticmethod
    def numerologia(anioNacimiento, mesNacimiento, diaNacimiento, anioActual, mesActual, diaActual):
        # Este metodo calcula la edad, signo zodiacal y numero de la suerte.

        edad = anioActual - anioNacimiento
        if (mesActual < mesNacimiento) or (mesActual == mesNacimiento and diaActual < diaNacimiento):
            edad = edad - 1
        edad = edad * 8760

        if (mesNacimiento == 12 and diaNacimiento >= 22) or (mesNacimiento == 1 and diaNacimiento <= 20):
            signoZodiacal = 'Capricornio'
        elif (mesNacimiento == 1) or (mesNacimiento == 2 and diaNacimiento <= 19):
            signoZodiacal = 'Acuario'
        elif (mesNacimiento == 2) or (mesNacimiento == 3 and diaNacimiento <= 20):
            signoZodiacal = 'Piscis'
        elif (mesNacimiento == 3) or (mesNacimiento == 4 and diaNacimiento <= 20):
            signoZodiacal = 'Aries'
        elif (mesNacimiento == 4) or (mesNacimiento == 5 and diaNacimiento <= 20):
            signoZodiacal = 'Tauro'
        elif (mesNacimiento == 5) or (mesNacimiento == 6 and diaNacimiento <= 21):
            signoZodiacal = 'Geminis'
        elif (mesNacimiento == 6) or (mesNacimiento == 7 and diaNacimiento <= 22):
            signoZodiacal = 'Cancer'
        elif (mesNacimiento == 7) or (mesNacimiento == 8 and diaNacimiento <= 23):
            signoZodiacal = 'Leo'
        elif (mesNacimiento == 8) or (mesNacimiento == 9 and diaNacimiento <= 22):
            signoZodiacal = 'Virgo'
        elif (mesNacimiento == 9) or (mesNacimiento == 10 and diaNacimiento <= 22):
            signoZodiacal = 'Libra'
        elif (mesNacimiento == 10) or (mesNacimiento == 11 and diaNacimiento <= 22):
            signoZodiacal = 'Escorpio'
        else:
            signoZodiacal = 'Sagitario'

        anio = anioNacimiento
        numeroSuerte = 0
        while anio > 0:
            numeroSuerte = numeroSuerte + anio % 10
            anio = anio // 10

        while numeroSuerte > 9:
            numeroSuerte = numeroSuerte - 9

        listaT = [edad, signoZodiacal, numeroSuerte]

        return listaT


class pruebaArchivos:

    def leerArchivo(self, archivo):
        # Este metodo lee un archivo y convierte su contenido en una lista.

        file = open(archivo, 'r')
        lineas = []
        lineas_archivo = []
        for linea in file.readlines():
            lineas.append(linea.replace('\n', '').split(","))
        file.close()
        for f in range(0, len(lineas)):
            try:
                lineas_archivo.append([int(lineas[f][0]), int(lineas[f][1]), int(lineas[f][2]), int(lineas[f][3]), int(lineas[f][4]), int(lineas[f][5])])
            except ValueError:
                lineas_archivo.append([0,0,0,0,0,0])
        return lineas_archivo

    def calcularNumerologia(self, lista):
        # Este metodo calcula la numerologia con valores de una lista como parametros,
        # y agrega los resultados del metodo a la lista resultados.
        resultados = []
        for f in range(0, len(lista)):
            resultados.append(Numerologia.numerologia(lista[f][0], lista[f][1], lista[f][2], lista[f][3], lista[f][4], lista[f][5]))
        return resultados

    def guardarResultasdos(self, entrada, resultados):
        # Este crea un nuevo archivo, donde guarda los los valores de entrada y los resultados.
        file = open("resultados.csv", 'w')
        file.write('Anio de nacimiento, Mes de nacimiento, Dia de nacimiento, Anio actual, Mes actual, Dia actual, Edad, Signo zodiacal, Numero de la suerte\n')
        for f in range(0, len(entrada)):
            linea = str(entrada[f][0]) + ',' + str(entrada[f][1]) + ',' + str(entrada[f][2]) + ',' + str(entrada[f][3]) + ',' + str(entrada[f][4]) + ',' + str(entrada[f][5]) + ',' + str(resultados[f][0]) + ',' + str(resultados[f][1]) + ',' + str(resultados[f][2]) + '\n'
            file.write(linea)
        file.close()


if __name__ == "__main__":
    prueba = pruebaArchivos()
    archivo = prueba.leerArchivo("DatosEdad.txt")
    print(archivo)
    resultado = prueba.calcularNumerologia(archivo)
    print(resultado)
    prueba.guardarResultasdos(archivo, resultado)
