from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QPushButton
from random import randrange
import sys


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setPen(QColor(255, 244, 0))
        qp.setBrush(QColor(255, 244, 0))
        for i in range(3):
            radius = randrange(0, 50)
            x = randrange(0 + radius, self.x() - radius)
            y = randrange(0 + radius, self.y() - radius)
            while (self.button.x() <= x + radius <= self.button.size().width() + self.button.x()) or \
                    (self.button.x() <= x - radius <= self.button.size().width() + self.button.x()) or \
                    (self.button.x() <= x <= self.button.size().width() + self.button.x()) or \
                    (self.button.x() <= y + radius <= self.button.size().height() + self.button.x()) or \
                    (self.button.x() <= y - radius <= self.button.size().height() + self.button.x()) or \
                    (self.button.x() <= y <= self.button.size().height() + self.button.x()):
                radius = randrange(0, 50)
                x = randrange(0 + radius, self.x() - radius)
                y = randrange(0 + radius, self.y() - radius)
            qp.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.exit(app.exec())
