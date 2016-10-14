import sys
from PySide.QtCore import *
from PySide.QtGui import *


class ZeroSpinBox(QSpinBox):
    zeros = 0

    def __init__(self):
        super().__init__()

        self.connect(self, SIGNAL("valueChanged(int)"), self.checkzero)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.emit(SIGNAL("atzero(int)"), self.zeros)


class Form(QDialog):
    def __init__(self):
        super().__init__()

        dial = QDial()
        dial.setNotchesVisible(True)

        zerospinbox = ZeroSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(zerospinbox)
        self.setLayout(layout)

        self.connect(dial, SIGNAL("valueChanged(int)"), zerospinbox.setValue)
        self.connect(zerospinbox, SIGNAL("valueChanged(int)"), dial.setValue)
        self.connect(zerospinbox, SIGNAL("atzero(int)"), self.announce)

        self.setWindowTitle("Signals and Slots")
        self.setGeometry(300, 300, 300, 300)

    def announce(self, zeros):
        print("ZeroSpinbox has been at zero {0} time.".format(str(zeros)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
