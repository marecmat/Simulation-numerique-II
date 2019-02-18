

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt  
import numpy as np
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Embed Matplotlib In PyQt5"
        top = 400
        left = 400
        width = 900
        height = 500

        icon = "icon.png"

        self.setWindowTitle(title)
        self.setGeometry(top,left, width, height)
        self.setWindowIcon(QIcon("icon.png"))

        self.MyUI()



    def MyUI(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        canvas = Canvas(self, width=8, height=4)
        canvas.move(5,50)

        button = QPushButton( "Click Me", self)
        button.move(100, 450)

        button = QPushButton("Click Me Two", self)
        button.move(250, 450)


class Canvas(FingureCanvas):
    def __init__(self, parent = None, width =5, height = 5, dpi =100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FingureCanvas.__init__(self, fig)
        self.setParent(parent)


        self.plot()



    def plot(self):
        t = np.linspace(0, 8*np.pi, 200)
        x = np.sin(t)
        ax = self.figure.add_subplot(111)
        ax.set_title('TestetuehfbmkzbgbrMBGHZBRGJZR')
        ax.set_ylabel('lmezhùgrbrnznr')
        ax.set_xlabel('ezjrmbepknrzgemkbjreon')
        #plt.tight_layout()
        ax.plot(t, x, label = 'sinus')
        ax.legend()
        ax.grid()





app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()