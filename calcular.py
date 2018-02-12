from PyQt5.QtWidgets import QTableWidget


class Calcular():

    def calcularSubtotal(tabla_material, contador_tabla):

        # Sumar todos los valores de la columna Importe.
        IMPORTE = 5
        subtotal = 0

        for fila in range(0, contador_tabla + 1):
            subtotal += float(tabla_material.item(fila, IMPORTE).text()) 
        
        return subtotal

    def calcularNeto(subtotal_textbox, descuento_textbox, neto_textbox):

        # Restar el porcentaje del Descuento al Subtotal. 
        subtotal_txt = subtotal_textbox.text()
        subtotal = float(subtotal_txt)
        descuento_txt = descuento_textbox.text()

        if descuento_txt:
            descuento_porcentaje = float(descuento_txt)
            descuento = subtotal * descuento_porcentaje / 100
        else:
            descuento = 0

        neto = subtotal - descuento 
        return neto
        

    def calcularIVA(neto_textbox):

        # Calcular el IVA (16%) al valor neto.
        neto_txt = neto_textbox.text()
        neto = float(neto_txt)

        iva = neto * 0.16
        return iva

#    def calcularTotal():
#        print("Calcular total")
