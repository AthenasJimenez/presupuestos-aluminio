import sys
from interfaz import Interfaz
from PyQt5.QtWidgets import *
from buscar import Buscar

# ----------------------------------------------------------
# |   CODIGO  |   NOMBRE  |   MEDIDA  |  COLOR  | CANTIDAD |
# |-----------|-----------|-----------|---------|----------| FORMULARIO 
# |           |           |           |         |          |  MATERIAL
# |--------------------------------------------------------|
# |                                             | AGREGAR  |
# |                                             -----------|
# |--------------------------------------------------------|-----------
# | CLIENTE |             | COLOR |                        | FORMULARIO
# |--------------------------------------------------------|  CLIENTE
# | FECHA   |             | FECHA DE ENTREGA |             |
# |--------------------------------------------------------|-----------
# | CANTIDAD | CODIGO | MEDIDA | NOMBRE | PRECIO | IMPORTE |
# |----------|--------|--------|--------|--------|---------|
# |          |        |        |        |        |         |   TABLA
# |----------|--------|--------|--------|--------|---------|  MATERIAL
# |          |        |        |        |        |         |
# |----------|--------|--------|--------|--------|---------|
# |          |        |        |        |        |         |
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

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Interfaz()
   sys.exit(app.exec_())
