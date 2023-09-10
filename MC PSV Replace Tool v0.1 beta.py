import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MC PSV Replace Tool")
        self.setGeometry(300, 300, 300, 300)

        layout = QVBoxLayout()

        # Botón 1 - Seleccionar bloque
        btn_bloque = QPushButton("Selecciona el bloque", self)
        self.bloque_combo = QComboBox(self)
        self.bloque_combo.addItem("Mesa de crafteo")
        self.bloque_combo.addItem("Bloque de limo")
        btn_bloque.clicked.connect(self.agregar_bloque)
        layout.addWidget(btn_bloque)
        layout.addWidget(self.bloque_combo)

        # Botón 2 - Seleccionar objeto
        btn_objeto = QPushButton("Selecciona el objeto", self)
        self.objeto_combo = QComboBox(self)
        self.objeto_combo.addItem("Bloque de comandos")
        self.objeto_combo.addItem("Portal de Nether")
        btn_objeto.clicked.connect(self.agregar_objeto)
        layout.addWidget(btn_objeto)
        layout.addWidget(self.objeto_combo)

        # Botón 3 - Crear truco
        btn_crear_truco = QPushButton("Crear truco", self)
        btn_crear_truco.clicked.connect(self.unir_textos)
        layout.addWidget(btn_crear_truco)

        # Cuadro de texto para mostrar el resultado
        self.resultado_texto = QTextEdit(self)
        self.resultado_texto.setReadOnly(True)  # Deshabilitar edición
        layout.addWidget(self.resultado_texto)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.bloque_seleccionado = ""
        self.objeto_seleccionado = ""

        self.show()

    def agregar_bloque(self):
        self.bloque_seleccionado = "834D810C"

    def agregar_objeto(self):
        if self.objeto_combo.currentText() == "Portal de Nether":
            self.objeto_seleccionado = "0000005A"
        elif self.objeto_combo.currentText() == "Otra opción":
            self.objeto_seleccionado = "00000089"
        else:
            self.objeto_seleccionado = "000000A5"

    def unir_textos(self):
        truco = f"_V0 Remplace cheat\n$0200 {self.bloque_seleccionado} {self.objeto_seleccionado}"
        self.resultado_texto.setPlainText(truco)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
