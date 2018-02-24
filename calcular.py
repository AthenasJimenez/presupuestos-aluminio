from PyQt5.QtWidgets import QTableWidget


class Calcular():

    def calcularSubtotal(tabla_material, contador_tabla):

        # Declarar la posicion de la columna "IMPORTE" e
        # inicializar el valor de subtotal en 0.
        COLUMNA_IMPORTE = 5
        subtotal = 0

        # Convertir todos los valores de la columna "IMPORTE"
        # a flotantes y sumarlos.
        for fila in range(0, contador_tabla + 1):
            subtotal += float(tabla_material.item(fila, COLUMNA_IMPORTE).text())

        # Convertir el flotante a texto.
        subtotal = round(subtotal, 2)
        subtotal_txt = str(subtotal)

        return subtotal_txt


    def calcularNeto(subtotal_textbox, descuento_textbox, neto_textbox):

        # Restar el porcentaje del Descuento al Subtotal. 
        subtotal_txt = subtotal_textbox.text()
        subtotal = float(subtotal_txt)
        descuento_txt = descuento_textbox.text()

        # Revisar si hay que aplicar un descuento.
        if descuento_txt:
            descuento_porcentaje = float(descuento_txt)
            descuento = subtotal * descuento_porcentaje / 100
        else:
            descuento = 0

        neto = subtotal - descuento 

        # Convertir el flotante a texto.
        neto = round(neto, 2)
        neto_txt = str(neto)

        return neto_txt
        

    def calcularIVA(neto_textbox):

        # Calcular el IVA (16%) al valor neto.
        neto_txt = neto_textbox.text()
        neto = float(neto_txt)

        iva = neto * 0.16

        # Convertir el flotante a texto.
        iva = round(iva, 2)
        iva_txt = str(iva)

        return iva_txt


    def calcularTotal(neto_textbox, iva_textbox):

        # Sumar el valor Neto e IVA.
        neto_txt = neto_textbox.text()
        neto = float(neto_txt)
        iva_txt = iva_textbox.text()
        iva = float(iva_txt)

        total = neto + iva

        # Convertir el flotante a texto.
        total = round(total, 2)
        total_txt = str(total)

        return total_txt

