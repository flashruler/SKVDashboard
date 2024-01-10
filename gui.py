from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SKVDashboard V0.01 BETA")
        self.resize(960, 540)
        button = QPushButton("CLICK", self) 
        button.setGeometry(200, 150, 100, 40) 
        self.setCentralWidget(button)
        self.show()

app = QApplication(sys.argv)
w = MainWindow()
app.exec()