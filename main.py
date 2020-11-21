from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QPushButton
from random import randrange
import sys
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        color = QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256))
        qp.setPen(color)
        qp.setBrush(color)
        for i in range(3):
            radius = randrange(0, 50)
            x = randrange(0 + radius, self.x() - radius)
            y = randrange(0 + radius, self.y() - radius)
            while (self.button.x() <= x + radius <= self.button.size().width() + self.button.x()) or \
                    (self.button.x() <= x - radius <= self.button.size().width() + self.button.x()) or \
                    (self.button.x() <= x <= self.button.size().width() + self.button.x()) or \
                    (self.button.y() <= y + radius <= self.button.size().height() + self.button.y()) or \
                    (self.button.y() <= y - radius <= self.button.size().height() + self.button.y()) or \
                    (self.button.y() <= y <= self.button.size().height() + self.button.y()):
                radius = randrange(0, 50)
                x = randrange(0 + radius, self.x() - radius)
                y = randrange(0 + radius, self.y() - radius)
            qp.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.exit(app.exec())
