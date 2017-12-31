import csv

class Buscar():

    def buscarPrecio(codigo, nombre, color):

        # Leer csv
        base_datos = csv.DictReader(open("aluminio-db.csv", "r", encoding="utf-8-sig"))

        # Columnas en csv
        CODIGO_C = "CODIGO"
        NOMBRE_C = "NOMBRE"
        COLOR_C = color

        # Buscar material por codigo y nombre.
        for fila in base_datos:
            print(fila)
            if fila[CODIGO_C] == codigo and fila[NOMBRE_C] == nombre:
                return fila[COLOR_C]
                
