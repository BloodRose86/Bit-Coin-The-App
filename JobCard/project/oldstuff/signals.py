import sys
import urllib.request

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QSpinBox


def SIGNAL(param):
    pass


class Form(QDialog):
    def __init__(self):
        super().__init__()

        dial = QDial()
        dial.setNotchesVisible(True)

        spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        self.connect(dial, SIGNAL("valueChanged(int)"), spinbox.setValue)
        self.connect(spinbox, SIGNAL("valueChanged(int)"), dial.setValue)

        self.setWindowTitle("Signals and Slots")
        self.setGeometry(300, 300, 300, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
