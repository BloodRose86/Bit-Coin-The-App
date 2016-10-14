import sys
from math import *
from PySide.QtCore import *
from PySide.QtGui import *


# noinspection PyBroadException
class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)

        self.lineedit.setFocus()

        self.connect(self.lineedit, SIGNAL("returnPressed()"), self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        # noinspection PyBroadException
        try:
            text = self.lineedit.text()
            self.browser.append("{} = <b>{}</b>".format(text, eval(text)))
        except:
            self.browser.append("<font color=red>{} is invalid</font>".format(text))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()