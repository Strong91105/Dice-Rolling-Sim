from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load UI file
        uic.loadUi("Dice.ui", self)

        self.show()

# Initialise the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()