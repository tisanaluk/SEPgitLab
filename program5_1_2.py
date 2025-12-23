import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/about-pusheen.webp")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0xFF, 0xFE, 0xE0))
        p.setBrush(QColor(0xFF, 0xFE, 0xE0))
        p.drawEllipse(0, 0, 100, 100)
        p.drawEllipse(300, 400, 100, 100)
        p.drawEllipse(400, 250, 100, 100)
        
        p.setPen(QColor(0xEB, 0xCC, 0xFF))
        p.setBrush(QColor(0xEB, 0xCC, 0xFF))
        p.drawEllipse(200, 200, 100, 100)
        p.drawEllipse(100, 350, 100, 100)
        p.drawEllipse(500, 150, 100, 100)
        
        p.setPen(QColor(0xA4, 0xD8, 0xD8))
        p.setBrush(QColor(0xA4, 0xD8, 0xD8))
        p.drawEllipse(200, 0, 100, 100)
        p.drawEllipse(0, 400, 100, 100)
        p.drawEllipse(350, 50, 100, 100)
        
        p.drawPixmap(QRect(150, 100, 300, 300), self.rabbit)
        p.end()


def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())


