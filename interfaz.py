import sys
from buscar import Buscar
from calcular import Calcular
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class Interfaz(QWidget):


    def __init__(self):
        super().__init__()
        self.title = 'Presupuestos de aluminio'
        self.left = 10
        self.top = 10
        self.width = 700
        self.height = 600
        self.initUI()

 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Creacion de segmentos.
        self.formularioMaterial()
        self.formularioCliente()
        self.tablaMaterial()
        self.formularioSumatoria()
 
	# Agregar segmentos a la ventana.
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.material_group_box)
        windowLayout.addWidget(self.cliente_group_box)
        windowLayout.addWidget(self.tabla_material)
        windowLayout.addWidget(self.sumatoria_group_box)

        self.setLayout(windowLayout)
        self.show()
 

    def formularioMaterial(self):

        # Crea formulario de material para agregar elementos a la tabla.
        # ----------------------------------------------------------
        # |   CODIGO  |   NOMBRE  |   MEDIDA  |  COLOR  | CANTIDAD |
        # |-----------|-----------|-----------|---------|----------| FORMULARIO
        # |           |           |           |         |          |  MATERIAL
        # |--------------------------------------------------------|
        # |                                             | AGREGAR  |
        # |                                             -----------|

        # Crea el grupo para el formulario del material.
        self.material_group_box = QGroupBox("")
        self.material_layout = QGridLayout()

        # Crea las etiquetas y cajas de texto 
        self.codigo_label = QLabel('CODIGO', self)
        self.codigo_textbox = QLineEdit(self)
        self.nombre_label = QLabel('NOMBRE', self)
        self.nombre_textbox = QLineEdit(self)
        self.medida_label = QLabel('MEDIDA', self)
        self.medida_textbox = QLineEdit(self)
        self.color_label = QLabel('COLOR', self)
        self.color_textbox = QLineEdit(self)
        self.cantidad_label = QLabel('CANTIDAD', self)
        self.cantidad_textbox = QLineEdit(self)

        # Crea boton de "Agregar".
        self.agregar_button = QPushButton('AGREGAR', self)
        self.agregar_button.setToolTip('Agregar material')
        self.agregar_button.clicked.connect(self.agregar_on_click)
 
        # Acomoda todos los elementos (etiquetas, cajas de texto y boton)
        # en el layout. 
        self.material_layout.addWidget(self.codigo_label, 0, 0) 
        self.material_layout.addWidget(self.nombre_label, 0, 1) 
        self.material_layout.addWidget(self.medida_label, 0, 2) 
        self.material_layout.addWidget(self.color_label, 0, 3) 
        self.material_layout.addWidget(self.cantidad_label, 0, 4) 
        self.material_layout.addWidget(self.codigo_textbox, 1, 0) 
        self.material_layout.addWidget(self.nombre_textbox, 1, 1) 
        self.material_layout.addWidget(self.medida_textbox, 1, 2) 
        self.material_layout.addWidget(self.color_textbox, 1, 3) 
        self.material_layout.addWidget(self.cantidad_textbox, 1, 4) 
        self.material_layout.addWidget(self.agregar_button, 2, 4) 
 
        # Agregar el layout al grupo.
        self.material_group_box.setLayout(self.material_layout)
        
 
    def formularioCliente(self):

        # Crear formulario de cliente.
        # |--------------------------------------------------------|-----------
        # | CLIENTE |             | COLOR |                        | FORMULARIO
        # |--------------------------------------------------------|  CLIENTE
        # | FECHA   |             | FECHA DE ENTREGA |             |
        # |--------------------------------------------------------|-----------

        # Crea el grupo para el formulario del material.
        self.cliente_group_box = QGroupBox("")
        self.cliente_layout = QGridLayout()

        # Crea las etiquetas y cajas de texto.
        self.cliente_label = QLabel('CLIENTE', self)
        self.cliente_textbox = QLineEdit(self)
        self.color_label_cl = QLabel('COLOR', self)
        self.color_textbox_cl = QLineEdit(self)
        self.fecha_label = QLabel('FECHA', self)
        self.fecha_textbox = QLineEdit(self)
        self.fecha_entrega_label = QLabel('FECHA DE ENTREGA', self)
        self.fecha_entrega_textbox = QLineEdit(self)

        # Acomoda todos los elementos (etiquetas y cajas de texto) 
        self.cliente_layout.addWidget(self.cliente_label,0,0) 
        self.cliente_layout.addWidget(self.cliente_textbox,0,1) 
        self.cliente_layout.addWidget(self.color_label_cl,0,2) 
        self.cliente_layout.addWidget(self.color_textbox_cl,0,3) 
        self.cliente_layout.addWidget(self.fecha_label,1,0) 
        self.cliente_layout.addWidget(self.fecha_textbox,1,1) 
        self.cliente_layout.addWidget(self.fecha_entrega_label,1,2) 
        self.cliente_layout.addWidget(self.fecha_entrega_textbox,1,3) 
 
        # Agregar el layout al grupo
        self.cliente_group_box.setLayout(self.cliente_layout)
 

    def tablaMaterial(self):

        # Crea una tabla donde se ira agregando el material .
        # |--------------------------------------------------------|-----------
        # | CANTIDAD | CODIGO | MEDIDA | NOMBRE | PRECIO | IMPORTE |
        # |----------|--------|--------|--------|--------|---------|
        # |          |        |        |        |        |         |   TABLA
        # |----------|--------|--------|--------|--------|---------|  MATERIAL
        # |          |        |        |        |        |         |
        # |----------|--------|--------|--------|--------|---------|
        # |          |        |        |        |        |         |
        # |--------------------------------------------------------|----------

        # Crea tabla con 0 filas y 6 columnas.
        self.tabla_material = QTableWidget()
        self.tabla_material.setRowCount(0)
        self.tabla_material.setColumnCount(6)
        self.tabla_material.setHorizontalHeaderLabels(['CANTIDAD', 'CODIGO', 'MEDIDA', 'NOMBRE', 'PRECIO', 'IMPORTE'])

        # table selection change
        self.tabla_material.doubleClicked.connect(self.on_click) 


    def formularioSumatoria(self):

        # |--------------------------------------------------------|----------
        # |  OBSERVACIONES            SUBTOTAL  |                  |
        # |-------------------------            -------------------| FORMULARIO
        # |                        |  DESCUENTO |                  | SUMATORIA
        # |                        |            -------------------|
        # |                        |    NETO    |                  |
        # |                        |            -------------------|
        # |                        |    IVA     |                  |
        # |                        |            -------------------|
        # |                        |   TOTAL    |                  |
        # ----------------------------------------------------------

        # Crea el formulario con la sumatoria final.
        self.sumatoria_group_box = QGroupBox("")
        self.sumatoria_layout = QGridLayout()

        # Crea las etiquetas y cajas de texto.
        self.observaciones_label = QLabel('OBSERVACIONES', self)
        self.observaciones_textbox = QLineEdit(self)
        self.subtotal_label = QLabel('SUBTOTAL', self)
        self.subtotal_textbox = QLineEdit(self)
        self.descuento_label = QLabel('DESCUENTO', self)
        self.descuento_textbox = QLineEdit(self)
        self.neto_label = QLabel('NETO', self)
        self.neto_textbox = QLineEdit(self)
        self.iva_label = QLabel('IVA', self)
        self.iva_textbox = QLineEdit(self)
        self.total_label = QLabel('TOTAL', self)
        self.total_textbox = QLineEdit(self)
       
        # Acomoda todos los elementos etiquetas y cajas de texto.
        self.sumatoria_layout.addWidget(self.observaciones_label, 0, 0)
        self.sumatoria_layout.addWidget(self.subtotal_label, 0, 1)
        self.sumatoria_layout.addWidget(self.subtotal_textbox, 0, 2)
        self.sumatoria_layout.addWidget(self.observaciones_textbox, 1, 0)
        self.sumatoria_layout.addWidget(self.descuento_label, 1, 1)
        self.sumatoria_layout.addWidget(self.descuento_textbox, 1, 2)
        self.sumatoria_layout.addWidget(self.neto_label, 2, 1)
        self.sumatoria_layout.addWidget(self.neto_textbox, 2, 2)
        self.sumatoria_layout.addWidget(self.iva_label, 3, 1)
        self.sumatoria_layout.addWidget(self.iva_textbox, 3, 2)
        self.sumatoria_layout.addWidget(self.total_label, 4, 1)
        self.sumatoria_layout.addWidget(self.total_textbox, 4, 2)
 
        # Agregar el layout al grupo
        self.sumatoria_group_box.setLayout(self.sumatoria_layout)
 

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    @pyqtSlot()
    def agregar_on_click(self):
    
        # Obtener los valores escritos en el formulario del material.
        codigo_txt = self.codigo_textbox.text()
        nombre_txt = self.nombre_textbox.text()
        medida_txt = self.medida_textbox.text()
        color_txt = self.color_textbox.text()
        cantidad_txt = self.cantidad_textbox.text()
    
        # Buscar el precio en la base de datos del material.
        precio_txt = Buscar.buscarPrecio(codigo_txt, nombre_txt, color_txt)

	# Calcular importe y redondear los decimales.
        importe = float(cantidad_txt) * float(precio_txt)
        importe = round(importe, 2)
        importe_txt = str(importe)
    
        # Agregar material a la tabla.
        contador_tabla = self.tabla_material.rowCount()
        self.tabla_material.insertRow(contador_tabla)
        self.tabla_material.setItem(contador_tabla, 0, QTableWidgetItem(cantidad_txt))
        self.tabla_material.setItem(contador_tabla, 1, QTableWidgetItem(codigo_txt))
        self.tabla_material.setItem(contador_tabla, 2, QTableWidgetItem(medida_txt))
        self.tabla_material.setItem(contador_tabla, 3, QTableWidgetItem(nombre_txt))
        self.tabla_material.setItem(contador_tabla, 4, QTableWidgetItem(precio_txt))
        self.tabla_material.setItem(contador_tabla, 5, QTableWidgetItem(importe_txt))

        # Calcular subtotal y ponerlo en la caja de texto.
        subtotal = Calcular.calcularSubtotal(self.tabla_material, contador_tabla)
        subtotal = round(subtotal, 2)
        subtotal_txt = str(subtotal)
        self.subtotal_textbox.setText(subtotal_txt)

        # Calcular el neto y ponerlo en la caja de texto.
        neto = Calcular.calcularNeto(self.subtotal_textbox, self.descuento_textbox, self.neto_textbox)
        neto = round(neto, 2)
        neto_txt = str(neto)
        self.neto_textbox.setText(neto_txt)

        # Calcular el IVA y ponerlo en la caja de texto.
        iva = Calcular.calcularIVA(self.neto_textbox)
        iva = round(iva, 2)
        iva_txt = str(iva)
        self.iva_textbox.setText(iva_txt)

        # Calcular el total y ponerlo en la caja de texto.
        total = Calcular.calcularTotal(self.neto_textbox, self.iva_textbox)
        total = round(total, 2)
        total_txt = str(total)
        self.total_textbox.setText(total_txt)
