import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
w = int(2000)
h = int(864)
def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Welcome!")
   w.setGeometry(0, 0, 1536, 864)
   b.move(50, 20)
   w.setWindowTitle("PyQt5")
   w.showMaximized()
   
   sys.exit(app.exec_())


if __name__ == '__main__':
   window()
