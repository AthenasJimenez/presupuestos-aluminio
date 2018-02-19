import csv

class Buscar():

    def buscarPrecio(codigo, nombre, color, mensajeError):

        # Leer csv
        base_datos = csv.DictReader(open("aluminio-db.csv", "r", encoding="utf-8-sig"))

        # Columnas en csv
        CODIGO_C = "CODIGO"
        NOMBRE_C = "NOMBRE"
        COLOR_C = color

        # Iniciar precio como None.
        precio = None

        # Verificar que el color sea valido.
        COLORES = ["N1", "N2", "N3", "G1", "G2", "G3", "H1", "H2", "H3", "B1", "B2", "B3", "E1", "E2", "E3"]
        if not color or color not in COLORES:
            # Enviar mensaje de error.
            mensajeError("Color no valido")
            return precio

        # Buscar material por codigo y nombre.
        if codigo and nombre:
            for fila in base_datos:
                if fila[CODIGO_C] == codigo and fila[NOMBRE_C] == nombre:
                    precio = fila[COLOR_C]

        # Buscar material por codigo.
        elif codigo and not nombre:
            for fila in base_datos:
                if fila[CODIGO_C] == codigo:
                    precio = fila[COLOR_C]

        # Buscar material por nombre.
        elif not codigo and nombre:
            for fila in base_datos:
                if fila[NOMBRE_C] == nombre:
                    precio = fila[COLOR_C]

        # Mostrar error si no hay codigo ni nombre.
        else:
            mensajeError("Debes proveer Codigo y/o Nombre")

        return precio
