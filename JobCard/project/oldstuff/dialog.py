import sys
from PySide.QtGui import *
from PySide.QtCore import *


__appname__ = "Eight Video"


class Program(QDialog):

    def __init__(self):
        super().__init__()

        openButton = QPushButton("Open")
        saveButton = QPushButton("Save")
        dirButton = QPushButton("Other")
        closeButton = QPushButton("Close")

        self.connect(openButton, SIGNAL("clicked()"), self.open)
        self.connect(saveButton, SIGNAL("clicked()"), self.save)

        layout = QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(saveButton)
        layout.addWidget(dirButton)
        layout.addWidget(closeButton)
        self.setLayout(layout)

    def open(self):

        dir = "."

        fileObj = QFileDialog.getOpenFileName(self, __appname__ + " Open file Dialog ", dir=dir, filter="Text file(*.txt)")
        print(fileObj)
        print(type(fileObj))

        fileName = fileObj[0]

        file = open(fileName, "r")
        read = file.read()
        print(read)

    def save(self):

        dir = "."

        fileObj = QFileDialog.getSaveFileName(self, __appname__, dir=dir, filter="Text file(*.txt)")
        print(fileObj)
        print(type(fileObj))

        contents = "Halle from http://py.bo.vc"

        fileName = fileObj[0]

        open(fileName, mode="w").write(contents)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Program()
    form.show()
    app.exec_()