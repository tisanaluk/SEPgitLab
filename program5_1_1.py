import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(255, 255, 0))
        p.setBrush(QColor(255, 255, 0))
        p.drawEllipse(0, -50, 600, 600)
        
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawEllipse(50, 0, 500, 500)
        
        p.setPen(QColor(255, 0, 0))
        p.setBrush(QColor(255, 0, 0))
        #p.drawPie(300, 250, 100, 400, 0, 360)
        p.drawEllipse(100, 50, 400, 400)
        #p.drawPolygon( [QPoint(50, 200), QPoint(150, 200),
        #   QPoint(100, 400),] )
        p.drawPixmap(QRect(150, 100, 300, 300), self.rabbit)
        p.end()


def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())


