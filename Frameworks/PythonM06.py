import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QGridLayout, QLabel, QMainWindow, QWidget

# trabalhando com PYQT5 em interfaçe grafica Exemplo

class HelloWindow(QMainWindow):
   def __init__(self):
      QMainWindow.__init__(self)

      self.setMinimumSize(QSize(280, 120))
      self.setWindowTitle("Olá, Mundo!")

      centralWidget = QWidget(self)
      self.setCentralWidget(centralWidget)

      gridLayout = QGridLayout(self)
      centralWidget.setLayout(gridLayout)

      title = QLabel("Olá Mundo para PyQt", self)
      title.setAlignment(QtCore.Qt.AlignCenter)
      gridLayout.addWidget(title, 0, 0)

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   mainWin = HelloWindow()
   mainWin.show()
   sys.exit( app.exec_() )