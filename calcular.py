from PyQt5.QtWidgets import QTableWidget


class Calcular():

    def calcularSubtotal(tabla_material, contador_tabla):

        # Sumar todos los valores de la columna Importe.
        IMPORTE = 5
        subtotal = 0

        for fila in range(0, contador_tabla + 1):
            subtotal += float(tabla_material.item(fila, IMPORTE).text()) 
        
        return subtotal

#    def calcularNeto(subtotal, descuento):
#
#        # Restar el porcentaje del Descuento al Subtotal. 
#        print("Calcular neto")
#
#    def calcularTotal():
#        print("Calcular total")
